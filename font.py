# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:43:07 2015

@author: hus
"""

import pygame, random
import threading

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('font demo')
font1 = pygame.font.Font(None, 20)
font2 = pygame.font.Font(None, 40)

white = 255,255,255
screencolor = 255,255,0
speed = 0
time = 0
textImage = 0

def speedclock():
    global speed 
    while True:
        speed = random.randint(0,200)
        pygame.time.Clock().tick(1)
def main():
    while True:
        time = random.randint(0,200)
        text1 = font1.render('speed:'+str(speed), True, white)
        text2 = font2.render('number:'+str(time), True, white)
        screen.fill(screencolor)
        screen.blit(text1, (100,100))
        screen.blit(text2, (100,160))
        pygame.display.update()
        pygame.time.Clock().tick(60)
t = threading.Thread(target=speedclock)
t.start()
main()