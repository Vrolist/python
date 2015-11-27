# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:02:15 2015

@author: hus
"""
import MySQLdb
import re
import urllib2
mainurl = "http://www.qiushibaike.com"

otherurl = '/textnew'
url = mainurl + otherurl
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0)'
headers = { 'User-Agent' : user_agent }
i = 1
opse = 0
sumcontent = 0
allcontent = []
while url != "":
    
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content_left = response.read().decode('utf-8')
    
    rg_content='<div class="content">(.*?)</div>'
    rg_unit = '<div.*?id="qiushi_tag.*?>.*?<div.*?class="author.*?>.*?<a.*?rel="nofollow.*?>.*?</a>.*?<a.*?title=".*?>.*?</a>.*?<h2>(.*?)</h2>.*?<div.*?class="content">(.*?)</div>.*?<div.*?class="stats">.*?<span.*?class="stats-vote.*?>.*?<i.*?class="number.*?>(.*?)</i>'
    regular = '<div.*?id="content-left" class="col1">(.*?)<div class="pagebar clearfix">.*?</div>.*?</div>'
    rg_nexturl = '<a.*?class="next".*?href="(.*?)".*?>.*?</a>'
    content = re.findall(regular, content_left, re.S)
    content = content[0]
    #print content_left
    #print len(content)
    #print type(content)
    ct_unit = re.findall(rg_content, content, re.S)
    ct_next = re.findall(rg_nexturl, content_left, re.S)
    if len(ct_next) != 0:
        url = mainurl + ct_next[0]
        i += 1
        print url
    else:
        url = ''
    #print ct_next[0]
    for si in ct_unit:
        opse += 1
        allcontent.append((opse,si))
    print len(ct_unit)
    sumcontent += len(ct_unit)

print i
print sumcontent

try:
    conn = MySQLdb.connect("localhost","root","husxx",port=3306,charset='utf8')
    cur = conn.cursor()
    
    cur.execute('create database if not exists qiubai')
    conn.select_db('qiubai')
    
    #cur.execute('create table test(id int, info varchar(20))')
    
    #values=[]
    #for i in range(20):
    #    values.append((i,'hi rollen'+str(i)))
    
    cur.executemany('insert into joke values(%s, %s)',allcontent)
    #cur.execute('update test set info="I am rollen" where id=3')
    
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "MySQL Error %d: %s" %(e.args[0], e.args[1])
print 'Over'