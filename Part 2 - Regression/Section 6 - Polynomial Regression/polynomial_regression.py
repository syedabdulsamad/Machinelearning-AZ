#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:48:00 2018

@author: abdulsamad
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.preprocessing import Imputer

dataset = pd.read_csv('Position_Salaries.csv')
features = dataset.iloc[:, 1:2].values
result = dataset.iloc[:,(np.shape(dataset)[1] - 1)].values
#result = dataset.iloc[:,(np.shape(dataset)[1] - 1)].values

from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
features[:, 0] = labelEncoder.fit_transform(features[:, 0])

# training and test sample data
from sklearn.model_selection import train_test_split
feature_train, feature_test, result_train, result_test = train_test_split(features, result, test_size = 0.2, random_state = 0)

# feature scaling
"""from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
feature_train =  scaler.fit_transform(feature_train)
feature_test =  scaler.transform(feature_test)"""

