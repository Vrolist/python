# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:28:26 2015

@author: hus
"""

while True:
    s = raw_input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print 'Input is of sufficient length'
    