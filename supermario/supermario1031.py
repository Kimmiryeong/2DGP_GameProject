from pico2d import *	
import random


class EGoomba:
	def __init__(self):
		self.gx, self.gy = 1700, 525
		self.image = load_image('enemie1.png')


	def draw(self):
		self.image.draw(self.gx, self.gy)


	def update(self):
		self.gx -= 2

class Block():
	def __init__(self):
		self.bx, self.by = 450, 600
		self.image = load_image('block.gif')

	def draw(self):
		self.image.draw(num1, num2)

	# def update(self):
	# 	events = get_events()
	# 	for event in events:
	# 		if event.type == SDL_KEYDOWN:
	# 			if event.key == SDLK_RIGHT:
	# 				self.bx -= 1

	# 			elif event.key == SDLK_LEFT:
	# 				self.by += 1
	



def handel_events():
	global running
	global dir
	global x 
	global y 
	events = get_events()

	for event in events:
		if event.type == SDL_QUIT:
			running = False

		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_RIGHT:
				dir += 1

			elif event.key == SDLK_LEFT:
				dir -= 1

			# 점프 모션 처리
			elif event.key == SDLK_UP:
				y += 40

			elif event.key == SDLK_ESCAPE:
				running = False

		elif event.type == SDL_KEYUP:
			if event.key == SDLK_RIGHT:
				dir -= 1

			elif event.key == SDLK_LEFT:
				dir += 1

			elif event.key == SDLK_UP:
				delay(0.05)
				y -= 40



open_canvas(1800, 1024)
background = load_image('background.png')
character = load_image('mario_standing.gif')
run_character = load_image('run1.gif')


runnig = True

x = 300
y = 530
dir = 0

goomba = EGoomba()
block = Block()

while runnig:
	clear_canvas()
	background.draw(100, 700)

	# Animation

	# Front
	if (x % 2 == 0):
		character.draw(x,y)

	else:
		run_character.draw(x,y)


	handel_events()
	x += dir * 5
	delay(0.01)

	goomba.update()
	# block.update()

	goomba.draw()
	block.draw(450,600)

	update_canvas()


close_canvas()

