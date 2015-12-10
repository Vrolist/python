# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:53:33 2015

@author: hus
"""
#definition class
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print '%s: %s' %(self.name, self.score)

class Demo():
    pass
hus = Demo
hus.na = 'hus'
print hus.na