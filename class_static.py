# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:15:25 2015

@author: hus
"""

class stat():
    def __new__(self):
        print 'new'
        
    def sayhello(self):
        print 'hello'
        




class Person(object):
    """Silly Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)
        
    def show(self):
        print self.name, self.age
        
if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print type(piglei)
    print __name__
else:
    print __name__