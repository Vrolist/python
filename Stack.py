# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:17:05 2015

@author: hus
"""

class Stack:
    def __init__(self, size = 15):
        self.stack = []
        self.size = size
        self.top = -1
    def setSize(self, size):
        self.size = size
    