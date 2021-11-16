from pico2d import *

class Goomba:
    def __init__(self):
        self.x, self.y = 1000, 123
        self.image = load_image('enemie1.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= 0.4

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


