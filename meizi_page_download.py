# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:39:01 2015

@author: hus
"""
#妹子图网站，爬取单一系列图片并保存在同一个文件夹下

import urllib
import urllib2
import os
import re


#def picCheck(path):
def loadurl(url):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=5)
        html = conn.read()
        return html
    except Exception:
        return ''
def download(url,filename):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=3)
        f = open(filename,'wb')
        f.write(conn.read())
        f.close()
        return True
    except Exception:
        print 'load',url,'error'
        return False
def save_pic(url,path):
    searchname = '.*/(.*?.jpg)'
    name = re.findall(searchname,url)
    filename = path +'/'+ name[0]
    
    #print filename + ':start'
    
    while True:
        if os.path.exists(filename):
            os.remove(filename)
        if not os.path.exists(filename):
            os.mknod(filename)
        if download(url,filename):
            break
    
    print filename + ':over'
    
def pic_list(picList,path):
    picurl = ''
    for picurl in picList:
        save_pic(picurl,path)

def picurl(url,path):
    if not os.path.exists(path):
        os.makedirs(path)
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break
    #conn = urllib2.urlopen(url,data=None,timeout=2)
    #html = conn.read()
    rePicContent1 = '<div.*?id="picture.*?>.*?<p>(.*?)</p>'
    rePicContent2 = '<div.*?class="postContent.*?>.*?<p>(.*?)</p>'
    rePicList = '<img.*?src="(.*?)".*?>'
    picContent = re.findall(rePicContent1, html,re.S)
    if len(picContent) <=0:
        picContent = re.findall(rePicContent2, html,re.S)
    if len(picContent) <=0:
        print 'load false, over download this page and return'
        return False
    else:
        picList = re.findall(rePicList,picContent[0],re.S)
        pic_list(picList,path)
#url = 'http://www.meizitu.com/a/454.html'
#picurl(url,'/home/hus/Desktop/shiyanlou/')

str1 = 're123re0re456re'
r1 = '(re.*re)'
r2 = '(re.*?re)'
print 'r1'
for i in re.findall(r1,str1):
    print i
print 'r2'
for i in re.findall(r2,str1):
    print i