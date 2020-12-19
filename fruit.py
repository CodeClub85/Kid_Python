
import random
import pygame
import game_functions as gf

class Fruit:
	
	def __init__(self, SCREEN, S, snake, tails):
		
		self.SCREEN = SCREEN
		self.S = S
		self.GRID_POINTS = gf.create_grid_points(self.S, snake)
		
		self.width = self.height = 10
		self.color = S.red
		
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.set(snake, tails)
		
	def set(self, snake, tails):
		while True:
			point = random.choice(self.GRID_POINTS)
			if point == snake.rect.topleft:
				continue
			for tail in tails:
				if point == tail.rect.topleft:
					continue
			self.rect.center = point[0] + 10, point[1] + 10
			break
		
	def draw(self):
		pygame.draw.circle(self.SCREEN, self.color, self.rect.center, 7)
		
		