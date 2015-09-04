#!/usr/bin/python
#Filename:arc.py
import pygame, sys, math
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")
while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	screen.fill((0,0,200))

	color1 = 255, 0, 255
	color2 = 255, 255, 255
	position1 = 200,150,200,200
	position2 = 150,200,150,200
	start_angle = math.radians(0)
	end_angle = math.radians(360)
	width = 8
	pygame.draw.arc(screen, color1, position1, start_angle, end_angle, width)
	pygame.draw.arc(screen, color2, position2, start_angle, end_angle, width)
	pygame.display.update()
