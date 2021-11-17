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
block3 = None

block4 = None
block5 = None
yForce = 0 

def enter():
    global player
    player = Mario()
    game_world.add_object(player, 1)

    global background
    background = Grass()
    game_world.add_object(background,0)
    background.get_player(player)


    global enemie1
    enemie1 = Goomba()
    game_world.add_object(enemie1, 1)
    enemie1.get_player(player)

    global block1
    block1 = Block()

    global block2
    block2 = Block()

    global block3
    block3 = Block()

    global block4
    block4 = Block()

    global block5
    block5 = Block()


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
        
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
        #     global yForce
        #     yForce = 100
        #     for i in range (1,100):
        #         yForce -= 4
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, background):
            global yForce
            yForce = 2            


        else:
            player.handle_event(event)




def update():
    global yForce
    for game_object in game_world.all_objects():
        game_object.update()

    if collide (player, enemie1):
        # enemie1.remove(enemie1)
        game_world.remove_object(enemie1)

    
            
    
    player.y += yForce


    if collide(player, background):
        yForce = 0

    elif yForce>=-10:
        yForce -= 0.01




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
    	game_object.draw()

    block1.draw(400 - player.x, 200)
    block2.draw(425 - player.x, 200)
    block3.draw(450 - player.x, 200)
    block4.draw(500 - player.x, 200)
    block5.draw(525 - player.x, 200)
    update_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a, = a.get_bb()
    left_b, bottom_b, right_b, top_b, = b.get_bb()


    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True