import random
import json
import os

from pico2d import *
import game_world
import game_framework


from character import Mario 
from background import Grass
from enemie import Goomba
from block import Block

name = "MainState"

player = None
background = None
enemie1 = None
block1 = None
block2 = None


def enter():
    global player
    player = Mario()
    game_world.add_object(player, 1)

    global background
    background = Grass()
    game_world.add_object(background,0)


    global enemie1
    enemie1 = Goomba()
    game_world.add_object(enemie1, 1)

    global block1
    block1 = Block()

    global block2
    block2 = Block()


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
    	game_object.draw()

    block1.draw(400 - player.x, 200)
    block2.draw(425 - player.x, 200)
    update_canvas()
