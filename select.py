# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:50:10 2015

@author: hus
"""

import time
import random
mp = []
i = 0
while i < 10000:
    mp.append(random.randint(1,100000))
    i+=1
print 'step 1 over'
print len(mp)
x=0
num=0
index=0
change=0
length = len(mp)
t1 = time.time()
while x<length-1:
    num = min(mp[x:length])
    index = mp.index(num)
    mp[x],mp[index] = mp[index],mp[x]
    change+=1
    x+=1
t2 = time.time()
print 'step 2 over'
print change,'次交换'
print t1,t2
print t2-t1,'秒'