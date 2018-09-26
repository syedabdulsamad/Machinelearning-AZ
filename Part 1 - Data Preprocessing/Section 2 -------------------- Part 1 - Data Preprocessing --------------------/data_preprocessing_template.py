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
input_features = dataset.iloc[:, :-1].values
result = dataset.iloc[:,3].values

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(input_features[:, 1:3])
input_features[:, 1:3] = imputer.transform(input_features[:, 1:3])