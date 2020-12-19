
import pygame
from pygame.time import Clock
from snake import Snake, SnakeTail
from fruit import Fruit
from button import Button
from settings import Setting
from scores import Score
import game_functions as gf

def set_flag(SCREEN, S):
	font = pygame.font.Font("AllerDisplay.ttf", 80)
	play = font.render("play", True, S.white)
	exit = font.render("exit", True, S.white)
	play_surface = pygame.Rect((210, 550), (300, 100))
	exit_surface = pygame.Rect((210, 700), (300, 100))
	image = pygame.image.load("snake.png")
	image_rect = image.get_rect()
	font = pygame.font.Font("Chrusty.ttf", 100)
	text = font.render("Kid Python", True, (0, 200, 0))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if play_surface.collidepoint(event.pos):
					pygame.time.delay(500)
					return True
				if exit_surface.collidepoint(event.pos):
					return False
					
		SCREEN.fill((0, 0, 0))
		SCREEN.blit(image, (S.sn_width/2 - image_rect.centerx, image_rect.bottom))
		SCREEN.blit(text, (100, image_rect.bottom+180))
		SCREEN.blit(play, (280, 550))
		SCREEN.blit(exit, (280, 700))
		pygame.display.update()


def run_game():
	
	pygame.init()
	S = Setting()
	clock = Clock()
	SCREEN = pygame.display.set_mode((S.sn_width, S.sn_height))
	
	snake = Snake(SCREEN, S)
	tails = [SnakeTail(SCREEN, (snake.cenx - snake.width, snake.ceny), S.dark_green)]
	fruit = Fruit(SCREEN, S, snake, tails)
	buttons = dict()
	gf.create_control_buttons(SCREEN, S, buttons)
	score = Score(SCREEN)
	
	flag = set_flag(SCREEN, S)
	while flag:
		gf.check_events(S, snake, buttons)
		gf.update_screen(SCREEN, S, snake, fruit, buttons, tails, score)
		clock.tick(S.FPS)


if __name__ == "__main__":
	run_game()




