from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('background.png')
        

    def draw(self):
        self.image.draw(800 -self.player.x, 300)
        draw_rectangle(*self.get_bb())

    def update(self):
    	pass
        
    def get_bb(self):
    	return 0, 0, 1600 - 1, 105

    def get_player(self,player):
        self.player = player;


class TWall:
    def __init__(self):
        self.x, self.y = 450, 600

    def draw(self):
        draw_rectangle(*self.get_bb())



    def get_bb(self):
        return 0, 0, self.x, self.y


    def update(self):
        pass
        