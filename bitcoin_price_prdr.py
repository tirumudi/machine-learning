# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:53:02 2018

@author: tirumudi
"""

import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

price_source_link="https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20180101&end="+time.strftime("%Y%m%d")
price_source = pd.read_html()
