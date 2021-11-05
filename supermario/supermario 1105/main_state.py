import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

goomba = None
character = None
block = None
background = None


class EGoomba:
    def __init__(self):
        self.gx, self.gy = 100, 145
        self.image = load_image('enemie1.png')


    def draw(self):
        self.image.draw(self.gx, self.gy)


    def update(self):
        self.gx -= 3



class Block:
    def __init__(self):
        self.image = load_image('block_0000.gif')

    def draw(self, num1, num2):
        self.image.draw(num1, num2)


class Player:
    def __init__(self):
        self.x, self.y = 100, 230
        self.dir = 0
        self.image = load_image('mario_standing.gif')

    def draw(self):
        self.image.draw(self.x, self.y)

        if self.x % 2 == 0 : 
            self.image.draw(self.x,self.y)

        else:
            self.runImage = load_image('run1.gif')
            self.runImage.draw(self.x, self.y)

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.x, self.y = 400,300

    def draw(self):
        self.image.draw(self.x, self.y)




###############################################################################################################################################################

# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')

#     def draw(self):
#         self.image.draw(400, 30)



# class Boy:
#     def __init__(self):
#         self.x, self.y = 0, 90
#         self.frame = 0
#         self.image = load_image('run_animation.png')
#         self.dir = 1

#     def update(self):
#         self.frame = (self.frame + 1) % 8
#         self.x += self.dir
#         if self.x >= 800:
#             self.dir = -1
#         elif self.x <= 0:
#             self.dir = 1

#     def draw(self):
#         self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global goomba, block, character,background
    goomba = EGoomba()
    block = Block()
    character = Player()
    background = Background()


def exit():
    global goomba, block, character, background
    del(block)
    del(goomba)
    del(character)
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                character.dir += 1

            elif event.key == SDLK_LEFT:
                character.dir -= 1

            # 점프모션 처리
            elif event.key == SDLK_UP:
                character.y += 43

            elif event.key == SDLK_ESCAPE:
                running = False


        elif event.type == SDL_KEYUP:
            
            if event.key == SDLK_RIGHT:
                character.dir -= 1

            elif event.key == SDLK_LEFT:
                character.dir += 1

            elif event.key == SDLK_UP:
                delay(0.05)
                character.y -= 40


   

def update():
    pass


def draw():
    clear_canvas()
    background.draw()
    character.draw()
    goomba.draw()
    block.draw(100, 200)
    
    update_canvas()





