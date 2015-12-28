#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:44:39 2015

@author: hus
"""

import urllib
import urllib2
import httplib
import requests
import json

httpClient = None

#有道词典查询单词的连接
QUERY_URL = 'http://fanyi.youdao.com/openapi.do?keyfrom=tinxing&key=1312427901&type=data&doctype=json&version=1.1&q='

url_query = 'https://api.shanbay.com/bdc/search/?word={name}'

url_account = 'https://api.shanbay.com/account/'

#req = urllib2.Request(url)
#res = urllib2.urlopen(url).read()
#print res

query_url = QUERY_URL + 'name'
#js= json.loads(requests.get(url_query).text)
js = json.loads(requests.get(url_query).text)

print type(js)
#print js['query']
#print js['errorCode']
#for i in js['translation']:
#    print i
