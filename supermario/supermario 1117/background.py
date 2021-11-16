from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 300)
        draw_rectangle(*self.get_bb())

    def update(self):
    	pass
        
    def get_bb(self):
    	return 0, 0, 1600- 1, 105