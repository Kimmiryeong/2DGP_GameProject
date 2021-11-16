from pico2d import *

class Block:
    def __init__(self):
        self.image = load_image('block.gif')

    def draw(self, num1, num2):
        self.image.draw(num1 , num2)