#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:19:06 2018

@author: abdulsamad
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.preprocessing import Imputer

dataset = pd.read_csv('Data.csv')
features = dataset.iloc[:, :-1].values
result = dataset.iloc[:,3].values

# missing data
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(features[:, 1:3])
features[:, 1:3] = imputer.transform(features[:, 1:3])

# categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Encoding input features
labelEncoder_input  = LabelEncoder()
features[:, 0] = labelEncoder_input.fit_transform(features[:, 0]) 
hotEncoder = OneHotEncoder(categorical_features = [0])
features = hotEncoder.fit_transform(features).toarray()

# Encoding output features
labelEncoder_output = LabelEncoder()
result = labelEncoder_output.fit_transform(result)

# training and test sample data
from sklearn.model_selection import train_test_split
feature_train, feature_test, result_train, result_test = train_test_split(features, result, test_size = 0.2, random_state = 0)


