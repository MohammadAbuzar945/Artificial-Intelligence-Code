# -*- coding: utf-8 -*-
"""Drugs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15_WSIPmLHiA8oSCi42C_yHmZGEsW8f3-
"""



import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np
import pandas as p 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from google.colab import drive


drive.mount('/content/drive')
directory = '/content/drive/MyDrive/Drugs/drug200.csv'
result=[]
dataset  = p.read_csv(directory)
dataset['Sex'].replace({'M':1,'F':0}, inplace = True)
dataset['BP'].replace({'LOW':0,'NORMAL':1,'HIGH':2}, inplace = True)
dataset['Cholesterol'].replace({'NORMAL':0,'HIGH':1}, inplace = True)
dataset['Drug'].replace({'drugA':0,'drugB':1,'drugC':2,'drugX':3,'DrugY':4}, inplace = True)

X = dataset.drop('Drug', axis=1)
y = dataset['Drug']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21)

model =LogisticRegression()

model.fit(X_train,y_train)



model1 = GaussianNB()
model1.fit(X_train,y_train)
model2 = tree.DecisionTreeClassifier()
model2.fit(X_train , y_train)
input =(23,0,2,1,25.355)
inputarray = np.asarray(input)
inputreshape = inputarray.reshape(1,-1)


prediction =model.predict(inputreshape)
prediction1 = model1.predict(inputreshape)
prediction2 = model2.predict(inputreshape)
print("The Decision Logistic regression:",prediction)
print("The Decision Guassian NB:",prediction1)
print("The Decision Decision Tree:",prediction2)

plot_confusion_matrix(model,X_test , y_test)
plt.show()

plot_confusion_matrix(model1,X_test , y_test)
plt.show()

plot_confusion_matrix(model2,X_test , y_test)
plt.show()

