#!/usr/bin/python
#Filename:math.py
p = 250
h = 0.1
while True:
	
	h += 0.1
	p += h
	if p+h >= 400:
		h = -h
	print p, h
	s = raw_input()
