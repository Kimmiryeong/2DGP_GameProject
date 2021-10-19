from pico2d import *



# def Goomba_motion():
# 	global gx
# 	global gy
# 	gx = 1800
# 	gy = 525
# 	while running:
# 		gx -= dir * 5




def handle_events():
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
				y += 20

			elif event.key == SDLK_ESCAPE:
				running = False
			


		elif event.type == SDL_KEYUP:
				if event.key == SDLK_RIGHT:
					dir -= 1
				elif event.key == SDLK_LEFT:
					dir += 1

				elif event.key == SDLK_UP:
					delay(0.05)
					y -= 20




open_canvas(1800, 1024)
background = load_image('background.png')
character = load_image('mario_standing.gif')
enemy1 = load_image('enemie1.png')
run_character = load_image('run1.gif')


running = True
x = 300
y = 530
# frame = 0
# 방향 left: -1, right: 1
dir = 0

while running:
	clear_canvas()
	background.draw(100,700)
	# character.clip_draw(frame * 100, 1 * 100, 100, 100, x, 530)
	# character.draw(300,530)


	# Animation


	# Goomba
	# Goomba_motion()
	gx = 1200
	enemy1.draw(gx, y)
	gx -= 5

	# Front
	if(x % 2 == 0):
		character.draw(x,y)	

	else:
		run_character.draw(x,y)	
	
	
	update_canvas()

	handle_events()
	x += dir * 5
	delay(0.01)

close_canvas()

# clip_draw(left, bottom, width, height, x, y)