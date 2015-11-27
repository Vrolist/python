# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:54:31 2015

@author: hus
"""

import urllib2
import urllib
import cookielib

hurl = 'http://localhost:8080/supermanager/'
purl = 'http://localhost:8080/supermanager/select.jsp'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
data = urllib.urlencode({"select":"cashier","name":'hus',"pwd":'hus'})
if opener.open(hurl,data):
    print 'open Success'
op = opener.open(purl)

data = op.read()

print data#获取页面html代码