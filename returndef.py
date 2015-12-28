# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:04:21 2015

@author: hus
"""
def calc_prod(lst):
    def ride():
        def f(x,y):
            return x * y
        return reduce(f,lst, 1)
    return ride
'''
f = calc_prod([1,2,3,4])
print f()
'''
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
'''    
f = count()
print type(f)
print len(f)
for i in f:
    print i()
'''

def newcount():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = newcount()
print f1(), f2(), f3()