def scrape_page_category(page_url):
    """
    Scrapes the page category of the fb page available in the page_url.
    Parameters:
    -----------
    page_url: URL of the fb page

    Returns:
    --------
    category: page category
    """

    # simple parsing
    # issue - does not work properly
    try:
        html = requests.get(page_url)
        bs = BeautifulSoup(html.content, 'html.parser')
        possible_links = bs.find_all('a')
        for link in possible_links:
            if link.has_attr('href'):
                if 'category' in link.attrs['href']:
                    category = link.attrs['href'].split('/')[3]
                    return category 
    except:
        # print('Enter URL of a fb page')
        pass
                
def fetch_page_category(details):
    """
    This function fetches the category of the each post released from a fb_page
    Parameters:
    -----------
    details: a dictionary of all details about a number of posts

    Returns:
    --------
    details: a dictionary of all details about a number of posts additionally with page_category (if accountType is fb page)
    """
    # traverse over all the pages
    # check if they are fb_page - if True - then fetch the page_category
    # - if False - then make the page_category = None
    for id, post in list(details.items()):
        try:
            post_type = post['account_details']['type']
            if post_type == 'facebook_page':
                page_category = scrape_page_category(post['account_details']['url'])
                post['account_details']['page_category'] = page_category
            else:
                post['account_details']['page_category'] = None
        except:
            pass
    return details