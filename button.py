
import pygame

class Button:
	
	def __init__(self, SCREEN, S, pos, dim):
		
		self.SCREEN = SCREEN
		self.pos = pos
		self.dim = dim
		self.color = S.white
		
		self.rect = pygame.Rect(self.pos, self.dim)
		
	def draw(self):
		pygame.draw.rect(self.SCREEN, self.color, self.rect)




