from random import *
import pygame

class Creature():
	def __init__(self, pos, data_pos):
		self.pos = pos
		self.data_pos = data_pos

		self.vec = [0, 0]

		self.radius = 30

		self.all_data = {
			"blue": ((0,0,255), 5, 10, [["red", 10], ["green", 10]]),
			"green": ((0,255,0), 5, 10, 0),
			"red": ((255,0,0), 5, 5, [["orange", 5]]),
			"orange": ((255,127,0), 10, 5, 0)
		}

		self.info = self.all_data[self.data_pos] #color, ParentChance, DeathChance, MutateChance

	def update_pos(self, dis, dis_info):
		for i in range(2):
			if self.vec[i] in range(-10, 10):
				self.vec[i] += choice((-1,1))
			else:
				if self.vec[i] < 0:
					self.vec[i] += 1
				else:
					self.vec[i] -= 1

		self.pos = list(self.pos[i]+self.vec[i] for i in range(2))

		for i in range(2):
			if self.pos[i] > dis_info[i]:
				self.pos[i] -= self.radius
				self.vec[i] = 0
			elif self.pos[i] < 0:
				self.pos[i] += self.radius
				self.vec[i] = 0

		pygame.draw.circle(dis, self.info[0], self.pos, self.radius)

	def update_life(self, creatures, dis_info):


		if (randint(0, 100) < self.info[1]):
			if not self.info[3]:
				creatures.append(Creature(self.pos, self.data_pos))
			else:
				for chance in self.info[3]:
					if randint(0,100) < chance[1]:
						creatures.append(Creature(self.pos, chance[0]))
						break
				else:
					creatures.append(Creature(self.pos, self.data_pos))					

		if (randint(0, 100) < self.info[2]):	
			creatures.remove(self)

def graph_update(our_time, dis, creatures, graph):
	rect = pygame.Rect(our_time, 600-len(creatures), 1, len(creatures))
	
	graph.append(rect)

	for r in graph:
		pygame.draw.rect(dis, (0,0,0), r)