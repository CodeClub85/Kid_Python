
import pygame
from button import Button
from snake import SnakeTail

def check_events(S, snake, buttons):
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if buttons["left"].rect.collidepoint(event.pos):
				if not snake.moving_x:
					snake.set_move(True, False, -S.snake_speed)
				
			elif buttons["right"].rect.collidepoint(event.pos):
				if not snake.moving_x:
					snake.set_move(True, False, S.snake_speed)
				
			elif buttons["up"].rect.collidepoint(event.pos):
				if not snake.moving_y:
					snake.set_move(False, True,-S.snake_speed)
				
			elif buttons["down"].rect.collidepoint(event.pos):
				if not snake.moving_y:
					snake.set_move(False, True, S.snake_speed)
				

def create_grid_points(S, snake):
	points = []
	xs = [i for i in range(0, S.snake_sn_width, snake.width)]
	ys =  [i for i in range(0, S.snake_sn_height-20, snake.width)]
	for y in ys:
		for x in xs:
			points.append((x, y))
	return points


def create_control_buttons(SCREEN, S, buttons):
	space = 10
	height = S.snake_sn_height
	left  = Button(SCREEN, S, (0, height), (S.btn_width, S.btn_height))
	up  = Button(SCREEN, S, (left.rect.right + space, height), (S.btn_width*2, S.btn_width-60))
	right = Button(SCREEN, S, (up.rect.right + space, height), (S.btn_width, S.btn_height))
	down = Button(SCREEN, S, (left.rect.right + space, up.rect.bottom + space), (S.btn_width*2, S.btn_width))
	
	buttons["left"] = left
	buttons["up"] = up 
	buttons["right"] = right
	buttons["down"] = down


def update_fps(tails, S):
	if len(tails) % 10 == 0:
		S.FPS += 1
	
		
def make_new_tail(SCREEN, S, tails, positions):
	if len(tails) % 2 == 0:
		tails.append(SnakeTail(SCREEN, positions[-1], S.dark_green))
	else:
		tails.append(SnakeTail(SCREEN, positions[-1], S.green))

	
def check_snake_fruit_collision(SCREEN, S, snake, fruit, tails, positions, score):
	if snake.rect.colliderect(fruit.rect):
		pygame.mixer.music.load("eat.ogg")
		pygame.mixer.music.play()
		fruit.set(snake, tails)
		update_fps(tails, S)
		score.update()
		make_new_tail(SCREEN, S, tails, positions)
		
			
def game_over(SCREEN, S, score):
	font = pygame.font.Font("AllerDisplay.ttf", 100)
	game_over = font.render("Game Over", True, S.red)
	score.pos = (320, 550)
	SCREEN.fill((0, 0, 0))
	SCREEN.blit(game_over, (100, 400))
	score.show()
		
		
def check_snake_wall_collision(SCREEN, S, snake):
	if snake.rect.top < 0 or snake.rect.left < 0 or snake.rect.right > S.snake_sn_width or snake.rect.bottom > S.snake_sn_height-20:
		pygame.quit()
		
		
def check_snake_body_collision(SCREEN, S, snake, tails, score):
	for tail in tails:
		if snake.rect.colliderect(tail.rect):
			S.collision = True
			game_over(SCREEN, S, score)
		
		
def store_positions(snake, tails):
	positions = []
	positions.append((snake.cenx, snake.ceny))
	for tail in tails:
		positions.append((tail.center))
	return positions
	

def updates(SCREEN, S, snake, fruit, buttons, tails, score):
	positions = store_positions(snake, tails)
	
	pygame.draw.line(SCREEN, S.white, (0, S.snake_sn_height-15), (S.snake_sn_width, S.snake_sn_height-15), 10)
	score.show()
	for button in buttons.values():
		button.draw()
	fruit.draw()
	snake.update()
	snake.draw()
	for tail, pos in zip(tails, positions):
		tail.center = pos
		tail.draw()
	
	check_snake_fruit_collision(SCREEN, S, snake, fruit, tails, positions, score)
	check_snake_body_collision(SCREEN, S, snake, tails, score)
		
		
def update_screen(SCREEN, S, snake, fruit, buttons, tails, score):
	if not S.collision:
		SCREEN.fill(S.sn_color)
		updates(SCREEN, S, snake, fruit, buttons, tails, score)
	else:
		game_over(SCREEN, S, score)
	
	pygame.display.update()




