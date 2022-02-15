# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:37:27 2021

@author: S.R
"""

import numpy as np
import matplotlib.pyplot as plt
class Perceptron(object):
    
    def __init__(self , no_of_inputs , learning_rate = 0.01 ,epoch=25):
        self.epoch=epoch
        self.learning_rate= learning_rate
        self.weights = np.zeros(no_of_inputs +1)
    def predict(self, inputs):
        sum = np.dot(inputs ,self.weights[1:] + self.weights[0])
        if sum >=0:
            activation = 1
        else:
            activation = 0
        return activation


    def train(self , training_inputs , labels):
        output =[]
        x_axis=[]
        y_axis=[]
        
        for _ in range(self.epoch):
            output2 =[]
            for inputs , label in zip(training_inputs , labels):
                prediction = self.predict(inputs)
                output2.append([prediction])
                error = label - prediction
                self.weights[1:]+=self.learning_rate * inputs *error
                self.weights[0] +=self.learning_rate *error
                print("Error" , error , "\nLearinig rate : ",self.learning_rate , "Weights :",self.weights[1:] ,"bias :" ,self.weights[0])
            output.append(output2)
        print('Output' , output) 
        i=0
        for n in output:
            count =0
            for i in range(4):
                if(n[i] ==labels[i]):
                    count=count+1
                i=i+1
                
            accuracy = count/4
            y_axis.append(accuracy)
            print('Accuracy',accuracy*100)
        for m in range(1,self.epoch+1):
            x_axis.append(m)
        print("Yaxis" , y_axis)
        print("X_Axis" , x_axis)
        plt.plot(x_axis , y_axis)


training_inputs = []
training_inputs.append(np.array([1,1])) 
training_inputs.append(np.array([1,0])) 
training_inputs.append(np.array([0,1])) 
training_inputs.append(np.array([0,0]))               
        
    
labels = np.array([1,0,0,0])

        
p = Perceptron(2)
p.train(training_inputs, labels)

inputs = np.array([0.5 , 0.8])
print("Predicted 1",p.predict(inputs))


inputs = np.array([1.5 , 0.5])
print("Predicted 2",p.predict(inputs))

inputs = np.array([1.5 , 1.5])
print("Predicted 3",p.predict(inputs))


inputs = np.array([0.5 , 1.5])
print("Predicted 4",p.predict(inputs))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    