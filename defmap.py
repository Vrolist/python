# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:42:19 2015

@author: hus
"""

#map()函数是内置的高阶函数，接收一个函数f和一个列表list
#并通过把函数f一次作用在list的每个元素上，得到一个新的list并返回

def double(s):
    return s*s

print map(double,[1,2,3,4,5])

#reduce()函数也是内置的高阶函数，接收一个函数f和一个列表list
#函数f必须一次接收两个参数，对list的每个元素进行反复的调用，返回最终结果
#[1,2,3,4,5]
#[3,3,4,5]
#[6,4,5]
#[10,5]
#15

def addsum(x,y):
    return x+y
print reduce(addsum,[1,2,3,4,5,6,7,8,9,10])


#filter()函数同样是python的内置高阶函数，接收一个函数f和一个列表list
#函数f对列表中的每个元素进行判断，返回 True 和 False
#filter()自动过滤掉不符合条件的元素，返回的符合条件的，组成新的list

def is_odd(x):
    return x % 2 == 1
    
print filter(is_odd,[1,2,3,4,5,6,7,8,9])