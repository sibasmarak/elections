# use these commands to install pyLDAvis and langid
# '!' implies a bash command in interactive notebook/Google Colab
# !pip install pyLDAvis
# !pip install langid

import os
import json
import langid
import pickle
import random
import urllib
import gensim
import warnings
import requests
import datetime
import numpy as np
import pandas as pd
import pyLDAvis.gensim
import tensorflow as tf
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
from urllib.parse import unquote
from collections import defaultdict
from sklearn.metrics import plot_confusion_matrix
from matplotlib.dates import DayLocator, DateFormatter

import nltk
import keras
from string import punctuation
from nltk.corpus import stopwords
from keras.models import Sequential
from sklearn.pipeline import Pipeline
from nltk.stem import WordNetLemmatizer 
from keras.activations import relu, tanh, sigmoid
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from keras.layers import Dense, Activation, LSTM, Flatten, Embedding

from gensim.test.utils import common_corpus, common_texts, common_dictionary
from gensim.models.ldamodel import LdaModel
from gensim.models.coherencemodel import CoherenceModel

nltk.download('wordnet')
nltk.download('stopwords')
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# connecting with the drive
# file_path is the location of all the .txt files in Google Drive
from google.colab import drive
drive.mount('/content/drive')
file_path = '/content/drive/MyDrive/new_Bihar_data' 