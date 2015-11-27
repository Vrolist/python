# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:37:31 2015

@author: hus
"""
import urllib2
import re
def htmlsource(url):
    html = urllib2.urlopen(url)