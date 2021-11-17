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

