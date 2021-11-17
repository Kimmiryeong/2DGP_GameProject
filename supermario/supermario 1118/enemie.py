from pico2d import *

class Goomba:
    def __init__(self):
        self.x, self.y = 1000, 123
        self.image = load_image('enemie1.png')

    def draw(self):
        self.image.draw(self.x-self.player.x , self.y)
        # if self.player.go == 1:
        #     self.image.draw(self.x , self.y)
        # else:
        #     self.image.draw(self.x, self.y)

        draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= 0.4

    def get_bb(self):
        x = self.x -self.player.x;
        return x - 20, self.y - 20, x + 20, self.y + 20

    def get_player(self, player):
        self.player = player;


class Turtle:
    def __init__(self):
        self.x, self.y = 1020, 123
        self.image = load_image('turtle.png')
        self.frame = 0

    def draw(self):
        
        self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x - self.player.x, self.y)
        # if self.player.go == 1:
        #     self.image.draw(self.x , self.y)
        # else:
        #     self.image.draw(self.x, self.y)

        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x -= 0.2


    def get_bb(self):
        x = self.x -self.player.x;
        return x - 20, self.y - 20, x + 20, self.y + 20

    def get_player(self, player):
        self.player = player;

