from pico2d import *

class Block:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('block.gif')

    def draw(self, num1, num2):
        self.image.draw(num1 , num2)
        self.x = num1
        self.y = num2
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 17, self.y - 17, self.x + 17, self.y + 17

class QBlock:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('question.gif')

    def draw(self, num1, num2):
        self.image.draw(num1 , num2)
        self.x = num1
        self.y = num2
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 17, self.y - 17, self.x + 17, self.y + 17


   