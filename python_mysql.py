# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:17:15 2015

@author: hus
"""

import MySQLdb

try:
    conn = MySQLdb.connect("localhost","root","husxx",port=3306)
    cur = conn.cursor()
    
    cur.execute('create database if not exists python')
    conn.select_db('python')
    
    #cur.execute('create table test(id int, info varchar(20))')
    
    values=[]
    for i in range(20):
        values.append((i,'hi rollen'+str(i)))
        
    cur.executemany('insert into test values(%s, %s)',values)
    
    cur.execute('update test set info="I am rollen" where id=3')
    
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "MySQL Error %d: %s" %(e.args[0], e.args[1])
