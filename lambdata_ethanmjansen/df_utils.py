'''
utility functions for working with dataframes
'''

import pandas as pd
import sklearn
import sklearn.model_selection
from sklearn.model_selection import train_test_split
from scipy.stats import ttest_ind
TEST_DF = pd.DataFrame([1, 2, 3])


def split(df):
    '''
    A split function that splits a dataframe into 1/4th and 3/4ths 
    '''
    train, test = train_test_split(df, train_size=.75, random_state=27)
    return train, test


def ttester(df, column1, column2):
    '''
    A ttest function that gives you the ttest score and pvalue of two features
    '''
    ttester = (ttest_ind(df[column1],
                         df[column2],
                         nan_policy='omit'))
    return print(ttester)
