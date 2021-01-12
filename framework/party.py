# the relevant parties grouped together
# keys are party names
# values is a list with different variations of party name avaiable in the parties_fb Google sheet
succint_party_names = {
    'Plurals bihar': [' प्लूरल्स बिहार ', 'पलूरल्स पार्टी बिहार'],
    'Loktantrik Janata Dal bihar': [' लोकतान्त्रिक जनता दाल बिहार ', 'Loktantrik Janata Dal bihar'],
    'CPI (M) bihar': ['cpm bihar', 'cpim bihar', 'Communist Party of India (Marxist–Leninist)'],
    'CPI bihar': ['cpi bihar', 'कम्युनिस्ट पार्टी बिहार'],
    'Hindustani Awam Morcha bihar': ['Hindustani Awam Morcha bihar', ' हिंदुस्तानी एवं मोर्चा बिहार'],
    'Janvadi Party (Socialist) bihar': ['जनवादी पार्टी (सोशलिस्ट) बिहार', 'Janvadi Party (Socialist) bihar'],
    'National Democratic Alliance bihar': ['National Democratic Alliance (bihar)', 'भारतीय जनता पार्टी बिहार ', 'bjp', 'bjp bihar', 'भाजपा बिहार'],
    'PDA bihar': ['PDA bihar'],
    'RLSP bihar': ['RLSP bihar', 'rastriye lock samta party bihar', 'राष्ट्रीय लॉक समता पार्टी बिहार'],
    'SDPI bihar': ['SDPI bihar'],
    'Samajwadi Janata Dal Democratic bihar': ['Samajwadi Janata Dal Democratic bihar', 'समाजवादी जनता दाल डेमोक्रेटिक बिहार'],
    'RJD': ['rjd', 'राष्ट्रीय जनता (बिहार)'], 
    'JDU': ['jdu', 'जदयू  बिहार', 'jdu bihar'],
    'Jan Adhikar Party bihar': ['जन अधिकार पार्टी (लो०)  बिहार', 'jan adhikar party bihar'],
    'Bhakpa bihar': ['भाकपा बिहार'],
    'Aam admi party bihar': ['aam admi party bihar', 'आम आदमी पार्टी बिहार'],
    'Suheldev bihar': ['सुहलदेव भारतीय समाज पार्टी बिहार ', 'suhaldev bhartiye samaj party bihar'],
    'Ralosapa bihar': ['रालोसपा बिहार '],
    'Samajwadi Party': ['समाजवादी पार्टी बिहार'],
    'Vikasheel Insaan Party bihar': ['विकासशील इंसान पार्टी बिहार', 'vip bihar ', 'Vikassheel Insaan Party bihar'],
    'BSP bihar': ['बहुजन समाज पार्टी बिहार', 'bahujan samaj party bihar'],
    'Congress bihar': ['कंग्रेस बिहार', 'indian national congress bihar'],
    'Bahujan Mukti Party bihar': ['bahujan mukti party bihar', 'बहुजन मुक्ति पार्टी बिहार'],
    'Bahujan Kranti Morcha bihar': ['बहुजन क्रांति   मोर्चा  बिहार ', 'bahujan kranti morcha bihar'],
    'Aimim bihar': ['aimim bihar'], 
    'Rastravadi Janlok Party bihar': ['rastrvadi janlok party bihar'],
    'LJP bihar': ['ljp bihar', 'lock jan sakti party bihar'], 
    'Bhartiya Sablog Party': ['भारतीय सब लोग पार्टी बिहार'],
    'NCP bihar': ['ncp party bihar', 'ncp bihar'],
    'Jantantrik Lokahit Party bihar': ['जनतांत्रिक लोकहित पार्टी बिहार ', 'jantantrik party bihar', 'जनतांत्रिक लॉक हिट पार्टी बिहार ', 'jantantrik lockhit party bihar'],
    'Bahujan Party bihar': ['बहुजन पार्टी बिहार'],
    'Bhartiya Insaan Party bihar': ['भारतीय इंसान पार्टी बिहार  ', 'bhartiye insan party bihar'],
    'Shoshit Samaj Dal bihar': ['शोषित समाज दल बिहार'] ,
    'Akhil Bhartiya Ati Pichda Party bihar': ['अखिल भारतीय अति पिछड़ा पार्टी बिहार'],
    'Rashtriya Jan Jan Party bihar': ['राष्ट्रीय जन जन पार्टी बिहार'],
    'Great Democratic Secular Front bihar': ['ग्रेट डेमोक्रेटिक सेक्युलर फ्रंट बिहार ', 'great democretic secular frount bihar'],
    'Bihar Yuva Ekte Party bihar': ['bihar yuva ekte party'],
    'Sanyukt Loktantrik Dharmnirapeksh Gathbandhan bihar': ['संयुक्त लोकतांत्रिक धर्मनिरपेक्ष गठबंधन बिहार'],
    'Nationalist Congress Party bihar': ['नेशनल कांग्रसे पार्टी बिहार'],
    'News Today bihar': ['न्यूज़ टुडे बिहार'],
    'Akhil Bhartiya Party bihar': ['akhil bhartiye party bihar'],
    'Jan Prabhu Party bihar': ['जन प्रभु पार्टी बिहार']
}

def get_msg(post):
    """
    Obtain the message field of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    msg: message of the post
    """

    msg = post['post_details']['message']
    return msg

def get_desc(post):
    """
    Obtain the description field of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    desc: description of the post
    """

    desc = post['post_details']['description']
    return desc

def get_title(post):
    """
    Obtain the title field of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    title: title of the post
    """

    title = post['post_details']['title']
    return title

def get_account_type(post):
    """
    Obtain the account type field of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    account_type: title of the post
    """

    account_type = post['account_details']['type']
    return account_type

def get_account_handle(post):
    """
    Obtain the account handle field of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    handle: handle of the account that released the post
    """

    handle = post['account_details']['handle']
    return handle

# How to create page url to match the links from Google sheets:
# concatenate the page handle to the end of 'https://www.facebook.com/'
def get_page_url(post):
    """
    Obtain the fb page url of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    url: url of the fb page [return a string 'ignore' in exception cases]
    """

    try:
        if post['account_details']['handle'] == '':
            return 'ignore'
        url = 'https://www.facebook.com/' + str(post['account_details']['handle'])
        return url
    except:
        return 'ignore'

# How to create group url to match the links from Google sheets:
# obtain the url field of account_details
def get_group_url(post):
    """
    Obtain the group_url of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    group_url: url of the fb group that released the post
    """

    group_url = post['account_details']['url']
    return group_url

def get_account_platform_id(post):
    """
    Obtain the platform_id [of account] of the post
    Parameters:
    -----------
    post: a post representation obtained from get_data()

    Returns:
    --------
    platform_id: platform_id of the account that released the post
    """

    platform_id = post['account_details']['platform_id']
    return platform_id

def format_link_from_sheet(link):
    '''
    Strips '?ref=br_rs' from the input link
    Parameters:
    -----------
    link: input link (url)

    Returns:
    -------
    link: stripped and converted to original form of link (i.e. if contents were Hindi, then converted back to hindi)
    '''

    # strip '?ref=br_rs' at the right end 
    # strip '/' at right end again
    # unquote and return the link 
    link = link.rstrip('?ref=br_rs').rstrip('/')
    return unquote(link)

def party_links(party_link_list, party_name):
    '''
    Obtains the links for an input party
    Parameters:
    -----------
    party_link_list: a list of (party-name, link) tuples 
    party_names: name of the party whose links are to be ontained 

    Returns:
    --------
    links: a list of links related to the party_name from party_link_list
    '''

    links = []
    # iterate over the party_link_list
    for name, party_link in party_link_list:
        # if name equals the party_name
        # add to the list links
        if name == party_name:
            links.append((name, party_link))

    return links

def create_party_link_dictionary(succint_party_names, party_link_list):
    '''
    Create a dictionary with party [keys of dictionary succint_party_names] as key and list of links related to that party as values
    Parameters:
    -----------
    succint_party_names: dictionary with party names and coresponding variations available in parties_fb Google sheet
    party_link_list: list of (party-name, link) tuples 

    Returns:
    --------
    party_link_dictionary: dictionary with format {party: links}
    '''

    # create the party_link_dictionary
    party_link_dictionary = {}

    # iterate over succint_party_names 
    # fetch links for each variation [available in values of succint_party_names] of a party
    # create the party_name as key
    # assign the corresponding links as values 
    for key, value in list(succint_party_names.items()):
        all_links = []
        for elem in value:
            all_links.extend(party_links(party_link_list, elem))

        # all_links is a list of tuples
        # the second element of each tuple is a link
        party_link_dictionary[key] = [x[1] for x in all_links]

    return party_link_dictionary

def obtain_posts_from_link(details, links):
    '''
    Fetch all the posts from details dictionary, released from the given link (url) 
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts
    links: a list of urls

    Returns:
    --------
    post_dict: dictionary of posts with format = {id: post}
    '''

    # obtain all posts from the link provided
    # define post_dict dictionary
    post_dict = {}

    # iterate over details dictionary
    for id, post in list(details.items()):
        # check the account type of the post
        # url creation approach is different for facebook page and facebook group 
        cat = get_account_type(post)
        is_page = False
        if cat == 'facebook_page':
            is_page = True

        # if post is released by a facebook page
        # create the url of the fb page with get_page_url()
        # if url available in input list links, add the post into post_dict
        if is_page:
            url = get_page_url(post)
            if url in links:
                post_dict[id] = post
        
        # if post is released by a facebook group
        # create the url of the fb group with get_group_url()
        # if url available in input list links, add the post into post_dict
        else:
            url = get_group_url(post)
            if url in links:
                post_dict[id] = post
        
    return post_dict

def create_party_post_dictionary(details, party_link_dictionary):
    """
    Create a dictionary with party [keys of dictionary succint_party_names] as key and posts [from input dictionary details] related to that party as values
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts
    party_link_dictionary: dictionary with format {party-name: links}

    Returns:
    --------
    party_post_dictionary: dictionary with format {party: posts}
    """

    # define the party_post_dictionary
    party_post_dictionary = {}

    # iterate over the party_link_dictionary
    # call obtain_posts_from_link() to obtain the posts corresponding to each list of links for each party
    for party, links in list(party_link_dictionary.items()):
        party_post_dictionary[party] = obtain_posts_from_link(details, links)

    return party_post_dictionary

def find_unused_posts(details, party_post_dictionary):
    """
    Collects the posts unavailble in the party_post_dictionary. 
    Termed as unused posts, since they are of no use to design the party classifier. Rest are termed as used posts.
    Termed simply, total = used + unused
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts
    party_post_dictionary: dictionary with format {party: posts}

    Returns:
    --------
    unused_posts: dictionary of unused posts with format {id: post}
    """

    # define the unused_posts dictionary
    unused_posts = {}

    # ontain the ids of posts available in details
    # obtain the ids of posts available in party_post_dictionary
    details_keys = list(details.keys())
    party_post_dictionary_ids = []
    for party, value in list(party_post_dictionary.items()):
        party_post_dictionary_ids.extend(list(value.keys()))

    # print the length of total posts and used posts
    print(len(details_keys))
    print(len(party_post_dictionary_ids))

    # collect all the ids available in details_keys [total] which are not available in party_post_dictionary_ids [used]
    # simply means collect all the ids of unused posts
    unused_ids = [id for id in details_keys if id not in party_post_dictionary_ids]

    # build the unused_posts dictionary from unused_ids
    for id in unused_ids:
        unused_posts[id] = details[id]

    return unused_posts

def obtain_msg_desc_title_combined(details):
    """
    Obtain the concatenation of message, description and title of the post
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts

    Returns:
    --------
    post_text: list of concatenation of message, description and title of all the posts available in details
    """

    # define list post_text 
    post_text = []

    # iterate over details
    for id, post in list(details.items()):
        # obtain the message, description and title
        msg = get_msg(post)
        desc = get_desc(post)
        title = get_title(post)

        # concatenate the message, description and title
        text = msg + desc + title
        post_text.append(text)

    return post_text

def obtain_posts_from_handle(details, handles):
    """
    Fetch all the posts from details dictionary, released from the given handles
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts
    handles: a list of handle

    Returns:
    --------
    handle_post_dict: dictionary with the format {handle: {id: post}}
    """

    # define handle_post_dict
    handle_post_dict = {}

    # define a dictionary for each handle in the handles list
    for handle in handles:
        handle_post_dict[handle] = {}

    # iterate over details
    for id, post in list(details.items()):
        # check if the handle of post is in input handles list 
        handle = get_account_handle(post)

        # if handle exists in handles
        # add the post into the approriate dictionary
        if handle in handles:
            handle_post_dict[handle][id] = post

    return handle_post_dict

def obtain_posts_from_platform_id(details, platform_ids):
    """
    Fetch all the posts from details dictionary, released from the given platform_ids 
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts
    platform_ids: a list of platform_ids

    Returns:
    --------
    platform_id_post_dict: dictionary with the format {platform_id: {id: post}}
    """

    # define platform_id_post_dict
    platform_id_post_dict = {}

    # define a dictionary for each platform_id in the platform_ids list
    for platform_id in platform_ids:
        platform_id_post_dict[platform_id] = {}

    # iterate over details
    for id, post in list(details.items()):
        # check if the platform_id of post is in input platform_ids list 
        platform_id = get_account_platform_id(post)

        # if handle exists in handles
        # add the post into the approriate dictionary
        if platform_id in platform_ids:
            platform_id_post_dict[platform_id][id] = post

    return platform_id_post_dict

def create_train_data(party_post_dictionary):
    """
    Create the training data. If required, split this into validation and train data set 
    Parameters:
    -----------
    party_post_dictionary: dictionary with format {party: posts}

    Returns:
    --------
    X: enitre training data corpus
    Y: labels corresponding to X 
    """

    # create the X and Y for the model
    X = []
    Y = []

    # iterate over party_post_dictionary
    for party, id_post in list(party_post_dictionary.items()):
        # obtain the text
        model_text = obtain_msg_desc_title_combined(id_post)
        size = len(model_text)

        # add the text
        # add the labels
        X.extend(model_text)
        Y.extend([party] * size)

    return X, Y
    
def create_final_train_list(train_list, parties):
    """
    Create the training_list on the basis of parties provided.
    In simple terms, just filter all the training from train_list examples whose labels are available in input parties
    Paramters:
    ----------
    train_list: list of (text, label) tuples 
    parties: list of parties whose texts are to be obtained

    Returns:
    --------
    X: filtered training data corpus, filtered on the basis of input parties
    Y: labels corresponding to X  
    """

    # define X and Y
    X, Y = [], []

    # iterate over entire train_list
    for y, x in train_list:
        # if label in parties
        if y in parties:
            # append the label to Y
            # append the text to X
            Y.append(y)
            X.append(x)

    return X, Y

