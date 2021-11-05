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

	def draw(self, num1, num2):
		self.image.draw(num1, num2)


class Player:
	def __init__(self):
		self.x, self.y = 300, 530
		self.image = load_image('mario_standing.gif')

	def draw(self):
		if (self.x % 2 == 0):
			character.draw(self.x, self.y)

		else:
			run_character = load_image('run1.gif')
			run_character.draw(self.x, self.y)


def handel_events():
	global running
	global dir

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
				player.y += 40

			elif event.key == SDLK_ESCAPE:
				running = False

		elif event.type == SDL_KEYUP:
			if event.key == SDLK_RIGHT:
				dir -= 1

			elif event.key == SDLK_LEFT:
				dir += 1

			elif event.key == SDLK_UP:
				delay(0.05)
				player.y -= 40



open_canvas(1800, 1024)
background = load_image('background.png')

player = Player()
goomba = EGoomba()
block = Block()


runnig = True

dir = 0




while runnig:
	clear_canvas()
	background.draw(100, 700)

	# Animation

	# Front
	

	handel_events()
	player.x += dir * 5
	delay(0.01)

	goomba.update()
	# block.update()

	goomba.draw()
	block.draw(450,600)

	update_canvas()


close_canvas()

