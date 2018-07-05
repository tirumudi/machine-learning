# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:14:04 2018

@author: 508561
"""

class animal:
    def __init__(self,a):
        self.a=a
        self.name='text'      
    
    def printContext(self):
        print(self.a * self.name)
        
dog = animal(2)
dog.printContext()