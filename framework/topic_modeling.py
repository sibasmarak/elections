# obtain the lemmatizer and add some stop-words
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')).union({'man', 'woman', 'west', 'south', 'north', 'east'})

# define a tokenizer to use it in TfidfVectorizer
def tokenizer(document):
    # ensure the tokens are in lemmatized, have a length of at least two, are only alphabetic, and not a stop_word
    words = [lemmatizer.lemmatize(words) for words in document.split() if len(words) > 2 and words.isalpha() and not words in stop_words]
    
    # make a mapping of replacing punctuation
    # use to replace punctuation in the words
    table = str.maketrans('', '', punctuation)
    words = [word.translate(table) for word in words]
    
    # return the words (contains the tokens)
    return words

def filter_language(messages, to_keep=['en', 'hi']):
    """
    Remove the messages with predominant languages other than to_keep list
    Parameters:
    -----------
    messages: list of messages (combination of message, title and description)
    to_keep: message languages to keep [default = ['en', 'hi']

    Returns:
    --------
    final_messages: list of messages with predominant languages in to_keep list
    """

    # define the final_message list
    final_messages = []

    # iterate through all the messages
    for msg in messages:
        # obtain the maximum likely language
        lang = langid.classify(str(msg))[0]

        # if lang in to_keep list
        # keep the message and append it to final_messages
        # else discard
        if lang in to_keep:
            final_messages.append(msg)

    return final_messages

def lda_analysis(party_post_dictionary, party_name=None, corpus=None):
    """
    obtain a fit TfIdfVecorizer and transformed corpus
    Parameters:
    -----------
    party_post_dictionary: dictionary with format {party: posts}
    party_name: name of a party (one of the keys of succint_party_names)
    corpus: list of text messages

    Returns:
    --------
    tfidf: TfIdfVectorizer fit to the corpus
    msgs: transformed corpus obtained with fit tfidf
    """

    # fit a TfIdfVecorizer
    # corresponding to a corpus (a list of messages)
    # or to the messages related to party_name
    # error handling
    msgs = []

    # if party_name is given
    # then fetch the messages related to party_name
    # create the corpus
    if party_name:
        posts = party_post_dictionary[party_name]
        msgs = obtain_msg_desc_title_combined(posts)

       
    # prepare the TfidfVectorizer
    # we capture the best 1000 features
    tfidf = TfidfVectorizer(ngram_range=(1,2), 
                            max_df=20, 
                            min_df=5, 
                            max_features=800,
                            tokenizer=tokenizer)

    # use GPU in Google Colab
    # though might not enhance the time factor (since few computation as such)
    # but still use to enhance the time factor for how-so-ever less computations
    with tf.device('/GPU:0'):
        # filter the corpus
        # transform the corpus with the fitted tfidf
        if corpus:
            corpus = filter_language(corpus)
            tfidf = tfidf.fit(corpus)
            msgs = tfidf.transform(corpus).toarray() 
        else:
            corpus = filter_language(msgs)
            tfidf = tfidf.fit(corpus)
            msgs = tfidf.transform(corpus).toarray()

    return msgs, tfidf

def create_common_corpus_dictionary(tfidf, msgs):
    """
    Create common corpus and common dictionary for LdaModel
    Parameters:
    -----------
    tfidf: TfIdfVectorizer fit to a corpus
    msgs: transformed corpus obtained with above tfidf

    Returns:
    --------
    common_corpus: common corpus for LdaModel
    common_dictionary: common dictionary for LdaModel
    """

    # design a preliminary dictionary to create common_dictionary later
    # obtain the id2word in common_dictionary
    dictionary = {}
    for value, key in list(tfidf.vocabulary_.items()):
        dictionary[key] = value
    dictionary = sorted(dictionary.items())

    # define common_dictionary
    common_dictionary = {}
    for key, value in dictionary:
        common_dictionary[key] = value

    # define common_corpus 
    common_corpus = []
    for row in msgs:
        # for each message
        # create a list of (id, occurence) tuples
        common_corpus.append([(id, elem) for id, elem in enumerate(row) if elem > 0])

    return common_corpus, common_dictionary

def find_lda_model(common_corpus, id2word, num_topics=range(5,155,10)):
    """
    Plot the Coherence values for each num_topic in num_topics.
    Find the num_topic that leads to highest coherence value for the LdaModel
    Parameters:
    -----------
    common_corpus: common corpus for LdaModel
    id2word: common dictionary for LdaModel
    num_topics: list of numbers which contains a possible good num_topic parameter for LdaModel [default = range(5,155,10)]

    Returns:
    --------
    num_topic: the number of topics which leads to highest coherence value for LdaModel
    """

    # find the right number of topics
    x_axis, y_axis_umass = [], []
    for num_topic in num_topics:
        lda = LdaModel(common_corpus, num_topics=num_topic, id2word=id2word)                # obtain the LdaModel
        umass= CoherenceModel(model=lda, corpus=common_corpus, coherence='u_mass')          # obtain the CoherenceModel
        temp_umass = umass.get_coherence()                                                  # obtain the Coherence values
        x_axis.append(num_topic)                                                            # append the num_topic value [x-axis]
        y_axis_umass.append(temp_umass)                                                     # append the coherence value [y-axis]
    
    # find the topic num with highest coherence
    coherence_value = max(y_axis_umass)
    index = y_axis_umass.index(coherence_value)
    num_topic = x_axis[index]

    # plot the coherence values vs num_topic
    plt.figure(figsize=(10,10))
    plt.plot(x_axis, y_axis_umass, 'g-')
    plt.xlabel('Num of Topics')
    plt.ylabel('Coherence Value')
    plt.title('Coherence Value vs Num Topics')
    plt.xticks(x_axis, x_axis)

    # return the best num of topics
    return num_topic

# lda_visualization is the returned variable 
# it can be viewed in an interactive way with pyLDAvis.display(lda_visualization)
def create_pyldavis_visualization(lda, common_corpus, common_dictionary):
    """
    Design a lda visualization (highly interactive and wonderful for topic visualization) for lda (LdaModel)
    Parameters:
    -----------
    lda: LdaModel for visualization of topics
    common_corpus: common corpus for LdaModel
    common_dictionary: common dictionary for LdaModel

    Returns:
    --------
    lda_visualization: visualization to visualize in pyLDAvis.display()
    """

    # create corpora_dict
    # gensim.corpora.Dictionary() has two parameters - id2word and token2id
    # essential in visualization
    corpora_dict = gensim.corpora.Dictionary()

    # assign id2word field of corpora_dict
    corpora_dict.id2word=common_dictionary

    # reverse the common_dictionary to obtain token2id
    reverse_common_dictionary = {}
    for key, value in list(common_dictionary.items()):
        reverse_common_dictionary[value] = key

    # assign token2id field of corpora_dict
    corpora_dict.token2id = reverse_common_dictionary

    # preare the lda visualization
    lda_visualization = pyLDAvis.gensim.prepare(lda, common_corpus, corpora_dict, sort_topics=False)
    return lda_visualization

