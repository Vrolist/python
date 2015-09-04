#!/usr/bin/python
#Filename: war.py
"""
Create on Sat Aug 29 2015

@author : hus
"""
class base:
	def __init__(self, blood, attack, defense, gold, experience):
		self.blood = blood
		self.attack = attack
		self.defense = defense
		self.gold = gold
		self.experience = experience
	'''
	def __del__(self):
		print "Base Delete"
	'''
class Hero(base):
	def __init__(self, name):
		base.__init__(self, 30, 4, 3, 50, 1)
		self.name = name
		self.grade = 1
		#self.current_blood = 30
		self.current_blood = self.blood
		#self.blood = 30
		#self.attack = 4
		#self.defense = 3
		#self.gold = 50
		self.current_experience = 0
		#self.experience = 1

	#def __del__(self):
		#print "Game Over, Thank You!!!!!"

	def current(self):
		print 'name:', self.name
		print 'grade:', self.grade
		#print 'current_blood:', self.current_blood
		print 'blood:', self.current_blood, '/', self.blood
		print 'attack:', self.attack
		print 'defense:', self.defense
		print 'gold:', self.gold
		#print 'current_experience:', self.current_experience
		print 'experience:', self.current_experience, '/' , self.experience
	def win(self,number,gold):
		self.current_experience += number
		self.gold += gold
		while self.current_experience >= self.experience:
			if self.grade < 18:
				self.current_experience -=  self.experience
				self.update()
	def injured(self,beattack):
		if beattack-self.defense > 0:
			self.current_blood -= beattack-self.defense
		if self.current_blood > self.blood:
			self.current_blood = self.blood
		elif self.current_blood < 0:
			self.current_blood = 0
			#break
			#Hero.__del__(self)
			#base.__del__(self)
	def update(self):
		self.grade += 1
		self.blood += 10
		self.current_blood = self.blood
		self.attack += 4
		self.defense += 2
		self.experience += 2
	
	#def attack(self):

class MosterOne(base):
	def __init__(self):
		base.__init__(self, 12, 3, 2, 5, 2)
		self.name = 'yama'
		self.grade = 1
		self.current_blood = self.blood
		#self.blood = 12
		#self.attack = 2
		#self.defense = 2
		#self.gold = 5
		#self.experience = 2
	def current(self):
		print 'name:', self.name
		print 'blood:', self.current_blood, '/', self.blood
		print 'attack:', self.attack
		print 'defense:', self.defense
		print 'gold:', self.gold
		#print 'current_experience:', self.current_experience
		print 'experience:', self.experience
	def injured(self, beattack):
		if beattack-self.defense > 0:
			self.current_blood -= beattack-self.defense
		if self.current_blood > self.blood:
			self.current_blood = self.blood
		elif self.current_blood < 0:
			self.current_blood = 0
			#death
	def __del__(self):
		print "%s death" % self.name
class main():
	def __init__(self):
		print 'Welcome to play Easy Game (by Carrot Group)'
		self.name = raw_input('Enter Your Hero Name:')
		h = Hero(self.name)
		password = raw_input('Enter Your Hero Password:')
		
	def main(self):
		while True:
			pass
			
	def __del__(self):
		print
'''
***   *********   ***
***   Game Over   ***
***   Hero Exit   ***
***   Good Bye    ***
***   *********   ***
'''


#main()


'''
h = Hero('Carrot')
h.current()
while True:
	m = MosterOne()
	m.current()
	while True:
		s = raw_input('Continue(Y/N):')
		if s == 'N' or s == 'n':
			break
		h.injured(m.attack)
		m.injured(h.attack)
		h.current()
		m.current()
		if m.current_blood == 0 :
			print 'You Win'
			h.win(m.experience, m.gold)
			break
		if h.current_blood == 0 :
			print 'You Lost'
			break
	h.current()
	co = raw_input('Enter Any Key To Continue:') 
'''
