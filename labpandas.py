# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:26:49 2018
purpose : to practice pandas

@author: 508561
"""
import numpy as np
import pandas as pd

series_obj = pd.Series(np.random.randn(5),['a','b','c','d','e'])
print(series_obj)
print(series_obj.index)
