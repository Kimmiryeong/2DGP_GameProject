import game_framework
from pico2d import*
import title_state

name = "Start state"
image = None
logo_time = 0.0

def enter():
	global image
	image = load_image('kpu_credit.png')


def exit():
	global image
	del(image)

def update():
	global logo_time 

	if (logo_time > 1.0):
		logo_time = 0
		game_framework.quit()

	delay(0.01)
	logo_time += 0.01

def draw():
	global load_image
	clear_canvas()
	image.draw(1800, 1024)
	update_canvas()

def handle_events():
	events = get_events()
	pass


def pause():
	pass

def resume():
	pass



# start_state의 구현과 활동
# 1. start_state.py를 만든다
# 2. start_state.py의 내부 함수들을 작성한다
# 3. 다른 소스에서 import start_state를 해서 활용한다.

# enter() -> handle_events(), update(), draw() -> pause() -> resum() -> handle_events(), update(), draw() -> exit()

