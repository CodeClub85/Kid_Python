
import numpy as np

class Setting:
	
	def __init__(self):
		
		self.white = (255, 255, 255)
		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.dark_green = (0, 180, 0)
		
		self.sn_width = 720
		self.sn_height = 1280
		self.sn_color = (0, 0, 0)
		self.FPS = 6
		self.collision = None
		
		self.snake_sn_width = self.sn_width
		self.snake_sn_height = self.sn_height - 240
		self.snake_speed = 20
		
		self.btn_width = (self.sn_width - 20) / 4
		self.btn_height = self.sn_height - self.snake_sn_height
		
		self.giant_fruit_time = 16
		
		


