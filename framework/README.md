# Following (long list :smile:) contains a brief description of all functions: 
(**Note**: The function input parameters are not mentioned. Only name of the function and its job.)

## Shortcut Links:
- [basic_analysis.py](#basic_analysispy)
- [captions.py](#captionspy)
- [classifier.py](#classifierpy)
- [constituency.py](#constituencypy)
- [party.py](#partypy)
- [scraping.py](#scrapingpy)
- [topic_modelling.py](#topic_modellingpy)

### `basic_analysis.py`
| **Name of Function** | **Function's Job** |
|:----------:|:---------:|
| *`autolabel()`* | Attach the height above each bar in a barplot |
| *`count_total_posts()`* | Count the total number of posts available in a dictionary |
| *`fetch_post_details()`* | Obtain the non-account related details of a post  |
| *`fetch_post_account_details()`* | Obtain the account related details of a post |
| *`get_data()`* | Combine the dictionaries - non-account and account related details of a post |
| *`plot_post_vs_dates()`* | Plot the number of posts versus dates for the input details dictionary |
| *`reaction_stats()`* | Plot the variation of input reactions over a period <br> Returns the statistics of input reactions |
| *`remove_redundant_keys()`* | Remove all the keys from input dictionary which have None values |
| *`splice_post_date()`* | Collect and return all the posts from start and end (including both) |
| *`trending_post()`* | Return the trending posts (and their types - photo/video etc.) on the basis of input reaction |

### `captions.py`
| **Name of Function** | **Function's Job** |
|:----------:|:---------:|
| *`create_caption_dictionary()`* | For each caption creates a dictionary of posts |
| *`find_all_captions()`* | Return a list of post's caption field for all input posts |

### `classifier.py`
| **Name of Function** | **Function's Job** |
|:----------:|:---------:|
| *`create_mgb_posts()`* | Obtain all the posts related to MGB (RJD + INC + CPIM + CPI) |
| *`create_nda_posts()`* | Obtain all the posts related to NDA (BJP + HAM + JDU + VIP) |
| *`party_classifier_binary()`* | Return the best binary Logoistic Regression classifier for the input two parties <br> Plot the confusion matrix |

### `constituency.py`
| **Name of Function** | **Function's Job** |
|:----------:|:---------:|
| *`constituency_links()`* | Filter all the links as per input constituency name |
| *`constituency_statistics()`* | Obtain a dictionary with the count of posts for each constituency |
| *`obtain_constituency_posts()`* | Obtain all the posts related to input constituency name  |
| *`obtain_party_constituency_posts()`* | Obtain posts common to constituency's dictionary and a party's dictionary |
| *`strip_constituency()`* | Strip the number from the initials of a constituency <br> Make the constituency upper case to match later with the [Lok Dhaba](https://lokdhaba.ashoka.edu.in/browse-data?et=AE&st=Bihar&an=17) data |

### `party.py`
| **Name of Function** | **Function's Job** |
|:----------:|:---------:|
| *`create_final_train_list()`* | Create the training data on the basis of parties provided |
| *`create_party_link_dictionary()`* | Create a dictionary with party as key and list of links related to that party as values |
| *`create_party_post_dictionary()`* | Create a dictionary with party as key and posts related to that party as values |
| *`create_train_data()`* | Create the training data. If required, later, split this into validation and train data set |
| *`find_unused_posts()`* | Collect the posts unavailble in the party_post_dictionary <br> Termed as unused posts, since they are of no use to design the party classifier. Rest are termed as used posts. Termed simply, total = used + unused |
| *`format_link_from_sheet()`* | Strip '?ref=br_rs' from the input link |
| *`obtain_msg_desc_title_combined()`* | Obtain the concatenation of message, description and title of the post |
| *`obtain_posts_from_handle()`* | Fetch all the posts from details dictionary, released from the given handles |
| *`obtain_posts_from_link()`* | Fetch all the posts from details dictionary, released from the given link (url) |
| *`party_links()`* | Obtain the links for an input party |

### `scraping.py` (has certain issues :disappointed:)
| **Name of Function** | **Function's Job** |
|:----------:|:---------:|
| *`fetch_page_category()`* | Fetch and populate the the category of the each input posts |
| *`scrape_page_category()`* | Scrape the page category of the fb page available in input url. |


### `topic_modelling.py`
| **Name of Function** | **Function's Job** |
|:----------:|:---------:|
| *`create_common_corpus_dictionary()`* | Create common corpus and common dictionary for LdaModel |
| *`create_pyldavis_visualization()`* | Design a lda visualization (highly interactive and wonderful for topic visualization) for LdaModel |
| *`filter_language()`* | Remove the messages with predominant languages other than input to keep list |
| *`find_lda_model()`* | Plot the Coherence values for each num_topic in list num_topics <br> Find the num_topic that leads to highest coherence value for the LdaModel |
| *`lda_analysis()`* | Obtain a fit TfIdfVecorizer and transformed corpus |
| *`tokenizer()`* | Tokenize the document |
















