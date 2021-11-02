import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

goomba = None
block = None



class EGoomba:
    def __init__(self):
        self.gx, self.gy = 1700, 525
        self.image = load_image('enemie1.png')


    def draw(self):
        self.image.draw(self.gx, self.gy)


    def update(self):
        self.gx -= 2

class Block():
    def __init__(self):
        self.bx, self.by = 450, 600
        self.image = load_image('block.gif')

    def draw(self):
        self.image.draw(num1, num2)

class Background:
    def __init__(self):
        self.bx, by = 1800, 1024
        self.image = load_image('background.jpg')

    def draw(self):
        self.image.draw(bx,by)




def enter():
    global goomba, block, player, background
    goomba = EGoomba()
    block = Block()
    background = Background()
    palyer  = Player()

def exit():
    global goomba, block, background, player
    del(goomba)
    del(block)
    del(background)
    del(player)


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global dir
    
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1

            elif event.key == SDLK_LEFT:
                dir -= 1

            # 점프 모션 처리
            elif event.key == SDLK_UP:
                player.y += 40

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1

            elif event.key == SDLK_LEFT:
                dir += 1

            elif event.key == SDLK_UP:
                delay(0.05)
                player.y -= 40


def update():
    goomba.update()
    player.update()


def draw():
    clear_canvas()
    goomba.draw()
    block.draw()
    update_canvas()





