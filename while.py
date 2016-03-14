# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:18:39 2015

@author: hus
"""

import random
number = random.randint(0, 100)
running = True
while running:
    guess = int(raw_input('Enter an integer:'))
    if guess == number:
        print 'Congratulations, you guessed it.'
        running = False
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that'
else:
    print 'The while loop is over.'
print 'Done'
