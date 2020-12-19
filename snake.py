

import pygame
from pygame.sprite import Sprite

class Snake:
	
	def __init__(self, SCREEN, S):
		
		self.SCREEN = SCREEN
		self.snake_sn = S.snake_sn_width, S.snake_sn_height
		
		self.width = 20
		self.color = S.green
		
		self.center()
		self.rect = pygame.Rect(0, 0, self.width, self.width)
		
		self.moving_x = True
		self.moving_y = False
		self.speed = 20
		
	def set_move(self, x, y, s):
		self.moving_x = x
		self.moving_y = y
		self.speed = s
	
	def center(self):
		self.cenx = self.snake_sn[0]/2 + 10
		self.ceny = self.snake_sn[1]/2 + 10
		
	def check_boundary(self):
		if self.cenx > self.snake_sn[0]:
			self.cenx = 10
		elif self.cenx < 0:
			self.cenx = self.snake_sn[0] - 10
		elif self.ceny < 0:
			self.ceny = self.snake_sn[1] - 30
		elif self.ceny > self.snake_sn[1]-20:
			self.ceny = 10
			
	def update(self):
		if self.moving_x:
			self.cenx += self.speed
		elif self.moving_y:
			self.ceny += self.speed
		self.check_boundary()
		
		self.rect.center = (self.cenx, self.ceny)
			
	def draw(self):
		pygame.draw.rect(self.SCREEN, self.color, self.rect)
	

class SnakeTail:
	
	def __init__(self, screen, center, color):
		
		self.screen = screen
		
		self.width = 20
		self.color = color
		self.center = center
		self.rect = pygame.Rect(0, 0, self.width, self.width)
	
	def draw(self):
		self.rect.center = self.center
		pygame.draw.rect(self.screen, self.color, self.rect)
		
		