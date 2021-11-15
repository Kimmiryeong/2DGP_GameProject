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
        self.x, self.y = 1000, 123
        self.image = load_image('enemie1.png')


    def draw(self):
        self.image.draw(self.x, self.y)


    def update(self):
        self.x -= 0.3



class Block:
    def __init__(self):
        self.image = load_image('block.gif')

    def draw(self, num1, num2):
        self.image.draw(num1 - character.x , num2)



class Player:
    def __init__(self):
        self.x, self.y = 100, 129
        self.dir = 0
        self.standing = load_image('mario_standing.gif')
        self.running = load_image('run1.gif')
    def draw(self):
        self.x += self.dir * 0.4
        self.standing.draw(self.x,self.y)





       



class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.x, self.y = 400,300

    def draw(self):
        self.image.draw(self.x - character.x, self.y)



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

            elif event.key == SDLK_ESCAPE:
                game_framework.quit()


            # 점프모션 처리
            elif event.key == SDLK_UP:
                # character.y += 43
                p1 = (character.x, character.y)
                p2 = (0, character.y + 40)
                p3 = (character.x * 2, 0)
                draw_curve_3_points(p1, p2, p3)



            elif event.key == SDLK_ESCAPE:
                running = False


        elif event.type == SDL_KEYUP:
            
            if event.key == SDLK_RIGHT:
                character.dir -= 1

            elif event.key == SDLK_LEFT:
                character.dir += 1

            elif event.key == SDLK_UP:
                delay(0.05)
                character.y -= 43


   

def draw_curve_3_points(p1, p2, p3):

    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3

    for i in range(0, 1000, 2):
        t = i / 100
        x  = (2 * t ** 2 - 3 * t + 1) * x1 + (-4 * t ** 2 + 4 * t) * x2 + (2 * t ** 2 - t) * x3
        y = (2 * t ** 2 - 3 * t + 1) * y1 + (-4 * t ** 2 + 4 * t) * y2 + (2 * t ** 2 - t) * y3
        character.running.draw(character.x,character.y)
    

def update():
    pass




def draw():  
    clear_canvas()
    background.draw()
    character.draw()
    goomba.update()
    goomba.draw()
    block.draw(400, 200)
    
    update_canvas()
