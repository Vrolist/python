# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:12:21 2015

@author: hus
"""

import re

secret_code = 'sdhfujxxixxjdifje234uhfdsxxlovexx874u23hfihxxyouxxhufe'

#a = 'xz123'
#b = re.findall('x.',a)
#print b

#a = 'xyxy123'
#b = re.findall('x*',a)
#print b

#a = 'xy123'
#b = re.findall('x?',a)
#print b


###重点学习下面两种

#贪心算法
#b = re.findall('xx.*xx', secret_code)
#print b

#非贪心算法
#c = re.findall('xx.*?xx', secret_code)
#print c

d = re.findall('xx(.*?)xx', secret_code)
print d

#for each in d:
#    print each

#hello后面有一个换行符
#s = '''sdfxxhello
#xxsdfsfxxworldxxdfji213'''

#error = re.findall('xx(.*?)xx', s)
#over = re.findall('xx(.*?)xx', s, re.S)

#print error
#print over

#s2 = 'adhuxxIxx123xxlovexxjdfisdf'
#f = re.search('xx(.*?)xx123xx(.*?)xx', s2)
#f1 = f.group(1)
#f2 = f.group(2)
#print f1
#print f2
#print f
#p = re.findall('xx(.*?)xx123xx(.*?)xx', s2)
#print p
#print p[0][1]


#s = '123rrrrrr123'
#output = re.sub('123(.*?)123', '123%d123'%789, s)
#print output
#print s

#不要使用compile
#pattern = 'xx(.*?)xx'
#new_pattern = re.compile(pattern,re.S)
#output = re.findall(new_pattern, secret_code)
#print output

#匹配纯数字
#a = 'adsf213456789sdfe4234sdf'
#b = re.findall('(\d+)',a)
#print b