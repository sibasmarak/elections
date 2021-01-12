def find_all_captions(details):
    """
    Returns a list of all the captions from details dictionary
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts

    Returns:
    --------
    caption_list: list of different captions available in the details
    """
    
    # define a set caption_list
    caption_list = set()

    # traverse all the keys
    # add to caption_list set
    for id, post in list(details.items()):
        caption_list.add(post['post_details']['caption'])

    return list(caption_list)

def create_caption_dictionary(details, captions=['jansatta.com']):
    """
    For each caption creates a dictionary of posts.
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts
    captions: a list of captions to analyse

    Returns:
    --------
    caption_post_dictionary: a dictionary of the form {caption : {id: post}} 
    """

    # create a dictionary with keys as the captions
    caption_post_dictionary = {}
    for caption in captions:
        caption_post_dictionary[caption] = {}

    # traverse through all the posts
    # if the caption of a post in captions
    # add the post to the dictionary with that caption as key
    for id, post in list(details.items()):
        try:
            # fetch the caption
            post_caption = post['post_details']['caption']
            # add to the dictionary
            if post_caption in captions:
                caption_post_dictionary[post_caption][id] = post
        except:
            # when caption is not available
            pass

    return caption_post_dictionary

