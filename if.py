# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:38:53 2015

@author: hus
"""
import random

number = random.randint(0,10)
print number
guess = int(raw_input('Enter an ingeger:'))

if guess == number:
    print 'Congratulations, you guess it'
elif guess < number:
    print 'No ,it is a little higher than that'
else:
    print 'No it is a little lower than that'

print 'Done'

