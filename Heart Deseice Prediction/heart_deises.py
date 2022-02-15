# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 22:31:28 2021

@author: S.R
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.linear_model import lasso
from sklearn import metrics

House = pd.read_csv('train.csv')

print(House.head())
