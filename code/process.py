from common import *

import os
from scipy.sparse import csr_matrix
import itertools


def _as_list(x):
    return x if type(x) == list else [x]

def _strip(df,columns):
    for c in _as_list(columns):
        df.loc[:,c] = df[c].str.strip()
    return df

def _lower(df,columns):
    for c in _as_list(columns):
        df.loc[:,c] = df[c].str.lower()
    return df


def pack():
    df = pd.read_csv("raw_data/crime.csv")
    df = df.dropna(subset = ['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE'])
    df['DATE'] = df.YEAR.astype('str').map(str) + '/' + df.MONTH.astype('str') + '/' +df.DAY.astype('str') + ' ' + df.HOUR.astype('str') + ':' + df.MINUTE.astype('str')
    df.DATE = df.DATE.apply(pd.to_datetime)
    df = df.drop(labels=['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE'], axis = 1)
    df.to_csv('raw_data/crime_processed.csv')


if __name__ == "__main__":
    pack()