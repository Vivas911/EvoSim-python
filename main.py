from random import *
import pygame
from time import time
from classdata import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60

DIS_PARAM = (800, 600)

dis = pygame.display.set_mode(DIS_PARAM)
pygame.display.set_caption("ЯнеЗнаюЧтоЯтакое")

creatures = []

timer = time()

our_time = 0
graph = []

run = True
while run:
	if time() - timer > 0.2:
		creatures.append(Creature( [ randint(0,DIS_PARAM[0]) , randint(0,DIS_PARAM[1]) ], "blue"))
		timer = time()

		for creature in creatures:
			creature.update_life(creatures, DIS_PARAM)

		our_time += 1 

	for creature in creatures:
		creature.update_pos(dis, DIS_PARAM)

	graph_update(our_time, dis, creatures, graph)

	if len(creatures) > 350:
		creatures = []
		our_time = 0
		graph = []

	events = pygame.event.get()

	for event in events:
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
	dis.fill("gray23")

	clock.tick(FPS)

pygame.quit()