# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 23:04:55 2021
@author: tyler
"""


#Can possibly add more


class Error_Measures:

    #Error Rate
    def Missclasification(self, y_pred, y):
            missclassified = []
            for i in range(0,len(y)):
                
                if y[i] != y_pred[i]:
                    count = 1
                else:
                    count = 0
                missclassified.append(count)
            error_rate = missclassified.count(1)/len(y)
            
            return error_rate
                
    #Mean-Squared Error
    def MSE_Pred(self, y_pred, y):
            mse = (sum((y-y_pred)**2))**0.5
        
            return mse
