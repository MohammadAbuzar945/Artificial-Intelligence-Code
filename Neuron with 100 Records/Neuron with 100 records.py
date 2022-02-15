
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:04:15 2021

@author: S.R
"""

import numpy as np
import random

class Neuron():
    def __init__(self,no_of_inputs):
        self.bias = 0.2
        self.weights = [0.65,0.30]
        self.learning_rate = 0.1
        
    def predict(self,input1,input2):
        summation = input1*self.weights[0] + input2*self.weights[1] + self.bias
        if summation >= 0 :
            return 1
        else:
            return 0
        
    def train(self,training_ex,actual_label):
        predicted_label = self.predict(training_ex[0],training_ex[1])
        print("Predicted_label is:",predicted_label,",Bias is",self.bias)
        if(predicted_label != actual_label):
            error = actual_label - predicted_label
            delta_W = self.learning_rate * error
            self.weights[0] += delta_W
            self.weights[1] += delta_W
            self.bias += delta_W
            print("Error is:",error,"\nNew bias:",self.bias,",Predicted label is:",predicted_label)
            self.train(training_ex,actual_label)
        return actual_label



epoch = range(20)
n= Neuron(2)
inputs =[[0,1,1],[1,0,1]]
for ep in epoch:
    for data in inputs:
        inputs = np.array([data[0] , data[1]])
        decision = n.train(inputs, data[2])
        print("Decision is :" , decision)
        
        
    inputs = [[random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)],[random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)] ]   
    
print("Epochs" ,ep)










     