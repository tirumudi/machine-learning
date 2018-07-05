# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:45:10 2018

@author: 508561
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import datasets 
from sklearn import linear_model

data = datasets.load_boston()
df = pd.DataFrame(data.data,columns=data.feature_names)
target = pd.DataFrame(data.target,columns=['MEDV'])
x = df['RM']
y = target['MEDV']
model = sm.OLS(y,x).fit()
predictions = model.predict(x)
print(predictions)
print(model.summary())


#using scikit learn

x = df
lm = linear_model.LinearRegression()
lm.fit(x,y)
predictions = lm.predict(x)
print(predictions[0:5])
