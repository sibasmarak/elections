def create_nda_posts(party_post_dictionary):
    """
    Obtain all the posts related to NDA (BJP + HAM + JDU + VIP)
    Parameters:
    -----------
    party_post_dictionary: dictionary with format {party: posts}

    Returns:
    --------
    nda_posts: dictionary of posts related to NDA with format {id: post}
    """

    # obtain the posts related to each party which is a part of NDA
    bjp = party_post_dictionary['National Democratic Alliance bihar']
    ham = party_post_dictionary['Hindustani Awam Morcha bihar']
    jdu = party_post_dictionary['JDU']
    vip = party_post_dictionary['Vikasheel Insaan Party bihar']

    # define nda_posts
    nda_posts = {}

    # create the entire nda_posts dictionary
    individual = [bjp, ham, jdu, vip]
    for party in individual:
        for id, post in list(party.items()):
            nda_posts[id] = post

    return nda_posts

def create_mgb_posts(party_post_dictionary):
    """
    Obtain all the posts related to MGB (RJD + INC + CPIM + CPI)
    Parameters:
    -----------
    party_post_dictionary: dictionary with format {party: posts}

    Returns:
    --------
    mgb_posts: dictionary of posts related to MGB with format {id: post}
    """

    # obtain the posts related to each party which is a part of MGB
    rjd = party_post_dictionary['RJD']
    inc = party_post_dictionary['Congress bihar']
    cpim = party_post_dictionary['CPI (M) bihar']
    cpi = party_post_dictionary['CPI bihar']

    # define mgb_posts
    mgb_posts = {}

    # create the entire mgb_posts dictionary
    individual = [rjd, inc, cpim, cpi]
    for party in individual:
        for id, post in list(party.items()):
            mgb_posts[id] = post

    # reducing the number of posts available 
    # ensure the nda-mgb binary classifier is trained with almost equal number of training examples from each class
    i = 0
    posts = count_total_posts(mgb_posts)
    while i < posts:
        key = random.choice(list(mgb_posts.keys()))
        del mgb_posts[key]
        i += 1.29
    
    return mgb_posts

def party_classifier_binary(party_post_dictionary ,party1='PDA bihar', party2='RJD'):
    """
    Return the best binary Logoistic Regression classifier for the input party1 and party2. Plots the confusion matrix.
    Parameters:
    -----------
    party_post_dictionary: dictionary with format {party: posts}
    party1: name of party1 [default = 'PDA bihar']
    party2: name of party2 [default = 'RJD']

    Returns:
    --------
    clf: best binary Logoistic Regression classifier for the input party1 and party2 messages
    """

    # obtain the posts related to party 1 and party 2
    party1_posts = party_post_dictionary[party1]
    party2_posts = party_post_dictionary[party2]

    # filter the messages with pre-dominant language to be English and Hindi
    party1_msgs =  filter_language(obtain_msg_desc_title_combined(party1_posts))
    party2_msgs =  filter_language(obtain_msg_desc_title_combined(party2_posts))

    # design the labels (party1 + party2)
    # design the data (party1_msgs + party2_msgs)
    labels = [0] * len(party1_msgs)
    labels.extend([1] * len(party2_msgs))

    data = party1_msgs
    data.extend(party2_msgs)

    # prepare the TfidfVectorizer
    # we capture the best 1000 features
    tfidf = TfidfVectorizer(ngram_range=(1,3), 
                            max_df=20, 
                            min_df=5, 
                            max_features=1000,
                            tokenizer=tokenizer)

    # use in Google Colab
    with tf.device('/GPU:0'):
        corpus = data
        tfidf = tfidf.fit(corpus)
        data = tfidf.transform(corpus).toarray()

    # obtain the train and validation set
    data_train, data_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.1)

    # fit a Logistic Regression
    clf = LogisticRegression(solver='newton-cg')
    clf = clf.fit(data_train, labels_train)

    # print the train and validation sizes
    print('Train Accuracy: {}'.format(clf.score(data_train, labels_train)))
    print('Test Accuracy: {}'.format(clf.score(data_test, labels_test)))

    # plot the confusion matrix
    plot_confusion_matrix(clf, data_test, labels_test, values_format='d', display_labels=[party1, party2], cmap='Blues', xticks_rotation=20.0);

    return clf