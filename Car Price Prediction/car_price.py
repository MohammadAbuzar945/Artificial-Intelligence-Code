# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 09:01:13 2021

@author: S.R
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
# from sklearn.linear_model import lasso
from sklearn import metrics


car_price = pd.read_csv('CarPrice_Assignment.csv')

print(car_price.head())
print(car_price.describe())



car_price = car_price.select_dtypes(include=[np.number]).dropna()

# print(car_price.head())
print(car_price.nunique())


x = car_price.drop(columns=['car_ID' ,'price'] , axis=1)
y=car_price['price']


# print(x)
# print(y)

X_train , X_test , Y_train,Y_test = train_test_split(x,y,test_size=0.3 , random_state=2)

model = LinearRegression()

model = model.fit(X_train ,Y_train)

prediction  = model.predict(X_train)

print("Training Auuracy:" ,model.score(X_train , Y_train) *100 ,"%")

prediction  = model.predict(X_test)
print("Testing Acuracy:" ,model.score(X_test , Y_test) *100 ,"%")



plot_confusion_matrix(model, X_train, Y_train)
plt.show()





