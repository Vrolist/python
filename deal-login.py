#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:38:35 2015

@author: hus
"""


import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

#登陆的主页面
hosturl = 'http://qzone.qq.com/'
#post数据接受和处理的页面（我们要从这个页面发送我们构造的Post数据）
posturl = ''

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

h = urllib2.urlopen(hosturl)

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0)',
           'Referer' : '******'}

postData = {'op':'dmlogin',
            'f':'st',
            'user':'******',
            'pass':'******',
            'rmbr':'true',
            'tmp':'0.73064244544308195'
            }

request = urllib2.Request(posturl, postData, headers)
print request
response = urllib2.urlopen(request)
text = response.read()
print text