import game_framework
from pico2d import *

import start_state

while True:
	open_canvas()

	game_framework.run(start_state)
	close_canvas()
