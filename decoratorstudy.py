# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:50:26 2015

@author: hus
"""

def log(f):
    def fn(x):
        print  'call ' + f.__name__ + '()...'
        return f(x)
    return fn

@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

#print factorial(10)

def adap(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
@adap
def add(x,y):
    return x+y

#print add(2,3)

import time

def performance(f):
    def currenttime(*x,**y):
        print time.ctime()
        return f(*x,**y)
    return currenttime

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)
print range(1,11)