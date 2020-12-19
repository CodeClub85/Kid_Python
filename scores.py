
import pygame

class Score:
	
	def __init__(self, SCREEN):
		
		self.SCREEN = SCREEN
		self.text = 0
		self.color = (255, 255, 255)
		self.pos = (320, 100)
		
		self.font = pygame.font.Font("AllerDisplay.ttf", 120)
		self.surface = self.font.render(str(self.text), True, self.color)
		
	def update(self):
		self.text += 1
		self.surface = self.font.render(str(self.text), True, self.color)
		
	def show(self):
		self.SCREEN.blit(self.surface, self.pos)



