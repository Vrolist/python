#!/usr/bin/python
#Filename:line.py

import pygame, sys, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")
color = 255,255,255
i = 1
while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()

	screen.fill((255,255,255))
	width = 2
	while i <= 100:
		color1 = random.randint(0,255)
		color2 = random.randint(0,255)
		color3 = random.randint(0,255)
		color = color1,color2,color3
		print i
		start = (random.randint(0,600), random.randint(0,500))
		end = (random.randint(0,600), random.randint(0,500))
		print color, start, end
		pygame.draw.line(screen, color, start, end, width)
		i += 1
		pygame.display.update()
		pygame.time.Clock().tick(1)
