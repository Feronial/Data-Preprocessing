# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:07:25 2017

@author: Soner Can KALKAN
"""

from sklearn import preprocessing
import pandas as pd


path = "Your Source Path"
Ds = pd.read_csv(path + "Ds.csv")  #To read csv file
min_max_norm = preprocessing.MinMaxScaler(feature_range=(0,10)) #Creating obejct to normalize values between the range  with preprocessing library
min_max_norm1 = preprocessing.MinMaxScaler(feature_range=(0,100))
Ds_norm = min_max_norm.fit_transform(Ds['Attribute 1'])# Actuel Normalization
Ds_norm1 = min_max_norm1.fit_transform(Ds['Attribute 2'])
Ds['Normalized Attribute 1 '] = Ds_norm
Ds['Normalized Attribute 2'] = Ds_norm1
Ds['Normalized Attribute 1 Rounded']=Ds['Normalized Attribute 1'].round(0) # Rounding Optional
Ds['Normalized Attribute 2 Rounded']=Ds['Normalized Attribute 2'].round(0)
Ds = Ds.drop(Ds.columns[[0,1,2]],1)
#Ds.to_csv(path + "Full_ReadyForPredict_Normalized Attribute(Final).csv") #To print csv file