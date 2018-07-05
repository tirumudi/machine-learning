# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:05:29 2018

@author: tirumudi
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

dataset_source = 'D:/508561/sb/conda/kaggle/machine/data/winequality-red.csv'
data = pd.read_csv(dataset_source,sep=';')
print(data.shape)
print(data.head())

y = data.quality
x = data.drop('quality',axis=1)
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.2,random_state=0,stratify=y)

