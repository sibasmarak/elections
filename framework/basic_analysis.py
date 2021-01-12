def fetch_post_details(post):
    """
    Obtain the post details.
    Parameters:
    -----------
    post: post (in JSON format) as obtained from the .txt files provided

    Returns:
    --------
    post_details: a dictionary containing the available post details
    """

    # define a post_details dictionary
    post_details = {}

    # initially populate the keys which are mandatory available
    # date key stores a datetime.date object
    year, month, date = [int(x) for x in post['date'].split()[0].split('-')]
    post_details['date'] = datetime.date(year, month, date)

    post_details['like_count'] = post['statistics']['actual']['likeCount']
    post_details['share_count'] = post['statistics']['actual']['shareCount']
    post_details['comment_count'] = post['statistics']['actual']['commentCount']
    post_details['love_count'] = post['statistics']['actual']['loveCount']
    post_details['wow_count'] = post['statistics']['actual']['wowCount']
    post_details['haha_count'] = post['statistics']['actual']['hahaCount']
    post_details['sad_count'] = post['statistics']['actual']['sadCount']
    post_details['angry_count'] = post['statistics']['actual']['angryCount']
    post_details['thankful_count'] = post['statistics']['actual']['thankfulCount']
    post_details['care_count'] = post['statistics']['actual']['careCount']
    post_details['post_type'] = post['type']
    post_details['post_url'] = post['postUrl']
    post_details['subscriber_count'] = post['subscriberCount']
    post_details['score'] = post['score']

    # collect all the keys of the post
    # assign default values
    post_key_list = list(post.keys())
    post_details['message'], post_details['title'], post_details['description'], post_details['caption'], post_details['link'] = [''] * 5

    # re-assign if the keys are present in the post_key_list
    if 'message' in post_key_list:
        post_details['message'] = post['message']
    if 'title' in post_key_list:
        post_details['title'] = post['title']
    if 'description' in post_key_list:
        post_details['description'] = post['description']
    if 'caption' in post_key_list:
        post_details['caption'] = post['caption']
    if 'link' in post_key_list:
        post_details['link'] = post['link']

    return post_details

def fetch_post_account_details(post):
    """
    Obtain the account details of the fb account that posted the post
    Parameters:
    -----------
    post: post (in JSON format) as obtained from the .txt files provided

    Returns:
    --------
    account_details: a dictionary containing the available post details
    """

    # define a account_details dictionary
    account_details = {}

    # initially fill those keys which are mandatory available
    account_details['url'] = post['account']['url']
    account_details['subscriber_count'] = post['account']['subscriberCount']
    account_details['type'] = post['account']['accountType']

    # obtain the keys of the account from the post
    # assign default values
    account_keys_list = list(post['account'].keys())
    account_details['id'], account_details['handle'], account_details['platform_id'] = None, '', ''

    # re-assign the keys if available in account_key_list
    if 'id' in account_keys_list:
        account_details['id'] = post['account']['id']
    if 'handle' in account_keys_list:
        account_details['handle'] = post['account']['handle']
    if 'platformId' in account_keys_list:
        account_details['platform_id'] = post['account']['platformId']
    
    return account_details

def get_data(file_path=file_path):
    """
    Combines the dictionaries - post_details and account_details
    Parameters:
    ----------
    file_path: the path of the directory which contains the .txt files

    Returns:
    --------
    details: a dictionary of all posts available in files ending with .txt inside the directory referred by file_path
    """

    # obtain the files ending with .txt
    files_in_directory = os.listdir(file_path)
    filtered_files = [file for file in files_in_directory if file.endswith('.txt')]
    
    # create a details dictionary {id: {post_details: {}, account_details: {}}}
    details = {}

    # for all the fetched .txt files 
    for F in filtered_files:
        with open(file_path + '/' + F, 'r', encoding='utf-8') as f:
            # read all the lines in f
            # each line is a collection of 100 posts
            # fetch the posts from result of each line (each line is a dictionary)
            posts = [json.loads(str(line))['result']['posts'] for line in f.readlines() if len(line) > 1]

            # posts is a list
            # each element of the posts list contains 100 fb posts
            for post_set in posts:
                # post_set is a set of 100 posts
                for post in post_set:
                    # get the post id
                    post_id = post['id']
                    if post_id != 0: # they are simly shares of other posts
                        details[post_id] = {} 
                        # get the post_details and account_details
                        # post_details contains the details of the post 
                        # account_details contains the details of the account which posted the post
                        details[post_id]['post_details'] = fetch_post_details(post)
                        details[post_id]['account_details'] = fetch_post_account_details(post)

    return details

def count_total_posts(details):
    """
    Counts the total number of posts available in details
    Parameters:
    ----------
    details: a dictionary of all details about a number of posts [format= {id: post}]

    Returns:
    --------
    length: Number of posts in details
    """

    # details contains post_id as keys
    # total number of keys is going to be same as posts
    length = len(list(details.keys())) 
    return length

def reaction_stats(details, reactions=['like_count'], 
                   plot=False, 
                   interval_days=8, 
                   separate=True, 
                   criterion='sum'):

    """
    Returns the max, min, average, standard deviation of each reaction in reactions (input list) in the details dictionary 
    If plot is true, then plots the stats of reactions vs dates.
    Parameters:
    -----------
    details:  a dictionary of all details about a number of posts
    reactions: a list of reactions which statistics is required [default: ['like_count']]
    plot: boolean to indicate if plotting the reaction stat is required or not [default: False]
    interval_days: the spacing between x_ticks (date) in the plot [default: 8]
    separate: plots separate graph for each reaction [default: True]
    criterion: a string to denote the statistics to be used for plotting the reaction graphs [default: sum, available: sum, mean, max] 

    Returns:
    --------
    reaction_stat_list: a dictionary of reaction and its statistics
    """

    # reaction stat list dictionary = {reaction : reaction_ stats}
    reaction_stat_list = {}

    # set the subplots in case we need to plot
    if plot and separate:
        fig, ax = plt.subplots(len(reactions), 1, figsize=(20,20))
        axis_index = 0
    
    # set the figure size
    if plot and not separate:
        plt.figure(figsize=(10,10))

    # not to make too clumsy
    if interval_days < 5:
        interval_days = 5

    # loop over the reactions
    # fetch the data in a reaction_value_list
    for reaction in reactions:
        reaction_value_list = []
        dates = []
        for id, post in list(details.items()):
            try:
                post_details = post['post_details']
                # if both date and reaction are in the keys of post_details
                # add to the dates and reaction_value list 
                if 'date' in list(post_details.keys()) and reaction in list(post_details.keys()):
                    date = post_details['date']
                    reaction_value = post_details[reaction]
                    dates.append(date)
                    reaction_value_list.append(reaction_value)
            except:
                pass

        # create a dictionary date_react_dict as {date : total reacts on the date}
        date_react_dict = {}
        for i in range(len(dates)):
            # collect the date and reaction_value
            date = dates[i]
            reaction_value = reaction_value_list[i]

            # if date already exists as a key
            # then add the reaction_value to the value corresponding to the date
            if date in date_react_dict:
                date_react_dict[date].append(reaction_value)

            # else create a new key with the date
            else:
                date_react_dict[date] = [reaction_value]

        # evaluate according to criterion for each key (i.e. date)
        for key, value in list(date_react_dict.items()):
            if criterion == 'sum':
                date_react_dict[key] = np.sum(value)
            elif criterion == 'median':
                date_react_dict[key] = np.median(value)
            elif criterion == 'mean':
                date_react_dict[key] = np.mean(value)

        # sort according to the date
        date_react_date = dict(sorted(date_react_dict.items()))
        dates_x_axis = list(date_react_date.keys()) 
        reacts_y_axis = list(date_react_date.values()) 
        
        # designing the plot
        if plot and separate:
            ax[axis_index].plot_date(dates_x_axis, reacts_y_axis, 'g-')         # plot the graph
            ax[axis_index].set_title(str(reaction) + ' vs Dates')               # set title
            ax[axis_index].set_xlabel('Dates')                                  # set x-axis label
            ax[axis_index].set_ylabel('Reacts')                                 # set y-axis label

            # add the x-ticks in the last Axes object
            if axis_index == len(reactions):
                x_ticks = [dates_x_axis[i] for i in range(len(dates_x_axis)) if i % interval_days == 0]
                ax[axis_index].set_xticks(x_ticks)
                fig.autofmt_xdate()
            axis_index += 1

        if plot and not separate:
            plt.plot_date(dates_x_axis, reacts_y_axis, '-', label=str(reaction))    # plot the graph    
            plt.title('Reactions vs Dates')                                         # set title
            plt.xlabel('Dates')                                                     # set x-axis label
            plt.ylabel('Reacts')                                                    # set y-axis label

            # set x-ticks
            x_ticks = [dates_x_axis[i] for i in range(len(dates_x_axis)) if i % interval_days == 0]
            plt.xticks(x_ticks, rotation=45)
            plt.legend(loc='best')

        # add the statistics for the reaction to the reaction_stat_list dictionary
        reaction_stat_list[reaction] = {
            'max': np.max(reacts_y_axis),
            'min': np.min(reacts_y_axis),
            'std_dev': np.std(reacts_y_axis),
            'mean': np.mean(reacts_y_axis)
        }

    return reaction_stat_list

def autolabel(ax, rects):
    """
    Attach a text label above each bar in *rects*, displaying its height.
    Parameters:
    -----------
    ax: Axes object
    rects: list of rectangles in bar plot

    Returns:
    --------
    None 
    """

    # loop over each rectangle
    for rect in rects:
        # obtain the heights of each rectangle
        height = rect.get_height()

        # add the annotation above the rectangles
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        
def trending_post(details, top=0.1, reactions=['like_count']):
    """
    Return the trending posts on the basis of input reaction, maximum used post type (photo/video etc.)
    Parameters:
    -----------
    details:  a dictionary of all details about a number of posts
    top: the percentage of the posts to be considered as trending [default: 0.1]
    reactions: a list of reactions which is used tp define trending posts [default: ['like_count']]
    
    Returns:
    --------
    post_type_tuple: a tuple of posts corresponding post_types on the basis of reaction
    trending_posts: dictionary [format- {id:post}] of trending posts defined as per the input reaction
    """

    # obtain the Figure and Axes objects
    fig, ax = plt.subplots(len(reactions), 1, figsize=(10,10*len(reactions)))
    axis_index = 0

    # define the trending_posts dictionary = {reaction: {id: posts}}
    trending_posts = {}

    # collect all the reaction_values and corresponding post_types
    for reaction in reactions:
        trending_posts[reaction] = {}
        reaction_value_list = []
        post_type_list = []
        id_list = []
        for id, post in list(details.items()):
            try:
                post_details = post['post_details']
                # if both post_type and reaction are in the keys of post_details
                # add to the post_type and reaction_value list 
                if 'post_type' in list(post_details.keys()) and reaction in list(post_details.keys()):
                    post_type = post_details['post_type']
                    reaction_value = post_details[reaction]
                    post_type_list.append(post_type)
                    reaction_value_list.append(reaction_value)
                    id_list.append({id:post})
            except:
                pass

    
        # reaction_value_list = [post['post_details'][reaction] for post in list(details.values())]
        # post_type_list = [post['post_details']['post_type'] for post in list(details.values())]
        # zip the two lists to create a list of tuple
        # collect the top percent posts on the basis of the input reaction
        zipped = list(zip(reaction_value_list, post_type_list, id_list))
        size = len(zipped)
        zipped = sorted(zipped, key = lambda x: x[0])[: int(top * size)]
        id_list = [x[2] for x in zipped]

        # with the help of ids in id_list (of trending posts)
        # design the reaction dictionary of trending_posts dictionary
        for ids in id_list:
            id = list(ids.keys())[0]
            post = list(ids.values())[0]
            trending_posts[reaction][id] = post

        # create a dictionary with different post_type as keys & their count as value
        post_type_list = [x[1] for x in zipped]
        count = Counter(post_type_list)
        labels = [x[0] for x in count.most_common()]
        values = [x[1] for x in count.most_common()]

        # bar plot for the trending posts according to reaction
        rects = ax[axis_index].bar(x=labels, height=values, width=0.5, color='g')                               # plot bar graph
        ax[axis_index].set_title('Number of posts vs post_type (reaction: ' + reaction.split('_')[0] + ')')     # set title
        ax[axis_index].set_ylabel('Number of posts')                                                            # set y-axis label

        # in the last Axes object
        # set the xticks and x-axis labels
        if axis_index == len(reactions) - 1:
            ax[axis_index].set_xticklabels(labels=labels, rotation=60)
            ax[axis_index].set_xlabel('Post_type')
        autolabel(ax[axis_index], rects)
        axis_index += 1

    post_type_tuple = count.most_common()
    return post_type_tuple, trending_posts
     
def plot_post_vs_dates(details, interval_days=2):
    """
    Plots the number of posts vs dates for the input details dictionary
    Parameters:
    -----------
    details:  a dictionary of all details about a number of posts
    interval_days: the spacing between x_ticks (date) in the plot [default: 2]

    Returns:
    --------
    None
    """

    # obtain a list of dates
    # use a counter on them
    dates = []
    for id, post in list(details.items()):
        try:
            # fetch the date
            dates.append(post['post_details']['date'])
        except:
            # when caption is not available
            pass

    # counter counts the number of posts on each date
    date_counter = Counter(dates)
    date_post_tuple = date_counter.most_common()
    date_post_tuple = sorted(date_post_tuple)
    dates = [x[0] for x in date_post_tuple]
    posts = [x[1] for x in date_post_tuple]

    # plot_date()
    plt.figure(figsize=(10,10))
    plt.plot_date(dates, posts, 'g-')
    plt.title('Posts vs Dates')
    plt.xlabel('Dates')
    plt.ylabel('Posts')
    x_ticks = [dates[i] for i in range(len(dates)) if i % interval_days == 0]           # set the xticks at a periodic interval of interval_days
    plt.xticks(x_ticks, rotation=45)

def splice_post_date(details, start, end):
    """
    Collect and return all the posts from start and end (including both start and end)
    Parameters:
    -----------
    details:  a dictionary of all details about a number of posts
    start: a start datetime object
    end: an end datetiem object

    Returns:
    --------
    spliced_post: a dictionary of posts posted between start and end date
       
    """

    # create a spliced post dictionary
    spliced_post = {}

    # try block
    try:
        # check for sanity of start and end
        if start > end:
            print('Error - start date should not be greater than end date')
            return 
        
        # iterate over all the posts
        for id, post in list(details.items()):
            try:
                post_details = post['post_details']
                if 'date' in list(post_details.keys()):
                    date = post_details['date']

                    # if the date is suitable - within the range provided
                    # add it to the spliced_post dict
                    if date >= start and date <= end:
                        spliced_post[id] = post
            except:
                pass

        return spliced_post

    # except block for error in type of range of start and end
    except:
        print('Error - check parameters to the function. start and end should be valid and a datetime.date object')
        return

def remove_redundant_keys(input_dictionary):
    """
    Removes all the keys from input_dictionary which have None values
    Parameters:
    ------------
    input_dictionary: input dictionary

    Returns:
    --------
    return_dictionary: subset of input_dictionary having all the keys which have not None values
    """
    
    # define the return_dictionary
    # it contains all the keys from input_dictionary which have not None values
    return_dictionary = {}
    for key, value in list(input_dictionary.items()):
        # remove the keys which have no values
        if input_dictionary[key]:
            return_dictionary[key] = value

    return return_dictionary