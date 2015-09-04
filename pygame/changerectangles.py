#!/usr/bin/python
#Filename:hello.py

import pygame, sys, random
from sys import exit
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Rectangles")
pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1
color = 200,200,0
screencolor = 255,255,255
while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			exit()
	screen.fill(screencolor)
	#move the ractangle
	pos_x += vel_x
	pos_y += vel_y




	#keep rectangle on the screen
	if pos_x > 500 or pos_x < 0:
		vel_x = -vel_x
		c1 = random.randint(0,255)
		c2 = random.randint(0,255)
		c3 = random.randint(0,255)
		color = c1, c2, c3
		screencolor = 255-c1, 255-c2, 255-c3
		print color
	if pos_y > 400 or pos_y < 0 :
		vel_y = -vel_y
                c1 = random.randint(0,255)
                c2 = random.randint(0,255)
                c3 = random.randint(0,255)
                color = c1, c2, c3
                screencolor = 255-c1, 255-c2, 255-c3
		print color


	#draw the ractangle
	width = 0
	pos = pos_x, pos_y, 100, 100
	pygame.draw.rect(screen, color, pos, width)

	pygame.display.update()
	#pygame.time.wait(10)
	pygame.time.Clock().tick(180)
