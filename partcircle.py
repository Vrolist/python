# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:10:59 2015

@author: hus
"""

import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('partcircle')
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,200,0))
    color = 100,230,12
    position = 300,250
    radius = 100
    width = 20
    pygame.draw.circle(screen, color, position, radius, width)
    
    pygame.display.update()
