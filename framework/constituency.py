def strip_constituency(constituency_link_list):
    """
    Strips the number from the initials of a constituency. Also makes the constituency upper case to match later with the LokDhaba data
    Parameters:
    -----------
    constituency_link_list: list of (constituency, link) tuples

    Returns:
    --------
    constituency_link_list: list of (constituency, link) tuples; here constituency has been structured than input
    """

    # strip the numbers from the initials of each constituency
    # make the constituency name as Upper Case
    constituency_link_list = [(x[0].split('_')[1].upper(), x[1]) for x in constituency_link_list]
    return constituency_link_list

def constituency_links(constituency_link_list, constituency_name):
    """
    Filters all the links as per input constituency_name
    Parameters:
    -----------
    constituency_link_list: list of (constituency, link) tuples
    constituency_name: name of a constituency

    Returns:
    --------
    links: list of (constituency_name, link) tuples
    """

    # define links
    links = []

    # iterate over constituency_link_list
    for name, constituency_link in constituency_link_list:
        # if the name of constituency equals constituency_name
        # appends the (name, constituency_link) to links
        if name == constituency_name:
            links.append((name, constituency_link))

    return links

def obtain_constituency_posts(details, constituency_link_list, constituency_name, print_count=False):
    """
    Obtain all the posts related to constituency_name
    Parameters:
    -----------
    details: dictionary of all details about a number of posts
    constituency_link_list: list of (constituency, link) tuples
    constituency_name: name of a constituency
    print_count: boolean to indicate print or not print the count of posts related to constituency_name

    Returns:
    --------
    const_dictionary: dictionary for posts related to contituency_name with format {id: post}
    """

    # obtain all the constituency links for constituency name
    const_links = constituency_links(constituency_link_list, constituency_name)

    # obtain all the posts from const_links
    const_dictionary = obtain_posts_from_link(details, [x[1] for x in const_links])
    # if print_count is true
    # print the count of number of posts in const_dictionary
    if print_count:
        print('Available Posts: {}'.format(count_total_posts(const_dictionary)))
    return const_dictionary

# replace details with the party_dictionary (can be obtained from party_post_dictionary[party_name])
# the following function can also be implemented with obtain_constituency_posts()
def obtain_party_constituency_posts(constituency_dictionary, party_dictionary):
    """
    Obtain posts common to constituency_dictionary and party_dictionary
    Parameters:
    -----------
    constituency_dictionary: dictionary for a particular constituency
    party_dictionary: dictionary for a particular party

    Returns:
    --------
    party_constituency_posts: dictionary [format - {id: post}] of posts common to constituency_dictionary and party_dictionary
    """

    # define party_constituency_posts
    party_constituency_posts = {}

    # fetch the ids for constituency_dictionary and party_dictionary
    constituency_dict_id = list(constituency_dictionary.keys())
    party_dict_id = list(party_dictionary.keys())

    # if the id is present in both id list
    for id in party_dict_id:
        if id in constituency_dict_id:
            party_constituency_posts[id] = party_dictionary[id]

    return party_constituency_posts

def constituency_statistics(details, constituency_link_list, constituency_names):
    """
    Obtain a dictionary with the count of posts for each constituency
    Parameters:
    -----------
    details: dictionary of all details about a number of posts
    constituency_link_list: list of (constituency, link) tuples
    constituency_name: list of constituency names

    Returns:
    --------
    constituency_post_number: dictionary with format {constituency_name: count of posts related to constituency_name}
    """

    # define constituency_post_number
    constituency_post_number = {}

    # for each constituency
    # obtain the count of posts related to that constituency
    # assign the count to constituency name as key in constituency_post_number dictionary
    for name in set(constituency_names):
        dictionary = obtain_constituency_posts(details, constituency_link_list, name)
        constituency_post_number[name] = count_total_posts(dictionary)

    return constituency_post_number
