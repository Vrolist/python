# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:25:13 2015

@author: hus
"""
import random

one = random.randint(1,11)
two = random.randint(11,21)
print one, two
for i in range(one, two):
    print i
else:
    print 'The for loop is over'
