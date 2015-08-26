# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:52:29 2015

@author: hus
"""
import re
import urllib
a = raw_input('input url:')

s = urllib.urlopen(a)
s1 = s.read()

def getimg(aaa):
    reg = re.compile(r'src="(.*?)" pic_ext=')
    l = re.findall(reg, aaa)
    tem = 0
    for x in l:
        tem += 1
        urllib.urlretrieve(x,'%s.jpg' % tem)
getimg(s1)
