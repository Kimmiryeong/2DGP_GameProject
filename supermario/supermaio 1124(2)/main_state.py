import random
import json
import os

from pico2d import *
import game_world
import game_framework



from character import Mario 
from background import Grass
from background import TWall
from enemie import Goomba
from enemie import Turtle
from block import Block
from block import QBlock
from ball import Ball
from mush import Mushroom

name = "MainState"

player = None

background = None

transwall = None

enemie1 = None
enemie2 = None

Qblock1 = None

block1 = None
block2 = None
block3 = None
block4 = None
block5 = None

fire = None

obj_Mush = None


yForce = 0 

def enter():
    global player
    player = Mario()
    game_world.add_object(player, 1)
    

    global background
    background = Grass()
    game_world.add_object(background,0)
    background.get_player(player)

    global transwall
    transwall = TWall()
    game_world.add_object(transwall,1)


    global enemie1
    enemie1 = Goomba()
    game_world.add_object(enemie1, 1)
    enemie1.get_player(player)

    global enemie2
    enemie2 = Turtle()
    game_world.add_object(enemie2, 1)
    enemie2.get_player(player)

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

    global Qblock1
    Qblock1 = QBlock()


    global obj_Mush
    obj_Mush = Mushroom()
    game_world.add_object(obj_Mush, 1)
    obj_Mush.get_player(player)
    obj_Mush.get_collision(Qblock1)
    player.get_collision(obj_Mush)
    


def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    global yForce
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, background):
            yForce = 2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, Qblock1):
            yForce = 0            
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, block1):
            yForce = 0            
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, block2):
            yForce = 0            
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, block3):
            yForce = 0          
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, block4):
            yForce = 0       
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide(player, block5):
            yForce = 0       
        else:
            player.handle_event(event)

def update():
    global yForce
    for game_object in game_world.all_objects():
        game_object.update()

    # ??? ?????? ??????
    if collide (player, enemie1):
        # enemie1.remove(enemie1)
        game_world.remove_object(enemie1)
        # player.score += 1

    if collide (player, enemie2):
        # enemie1.remove(enemie1)
        game_world.remove_object(enemie2)
        # player.score += 1

    for i in range(0, len(player.ballArr)):
        if enemie1.IsCollision == False:
            if collide (player.ballArr[i], enemie1):
                game_world.remove_object(enemie1)
                game_world.remove_object(player.ballArr[i])
                enemie1.IsCollision = True
        
        if enemie2.IsCollision == False:                
            if collide (player.ballArr[i], enemie2):
                game_world.remove_object(enemie2)
                game_world.remove_object(player.ballArr[i])
                enemie2.IsCollision = True

    if collide (player, block1):
        # ?????? ??????
        if player.y + 25 <= block1.y + 17:
            # game_world.remove_object(player)
            yForce -= 0.03
        # ?????? ???
        else:
            yForce = 0
        
        # ?????? ??? ???
        if player.x + 12 >= block1.x - 20 and player.y >= block1.y - 17 and player.y <= block1.y + 17 :  
            # game_world.remove_object(player)
            player.x -= 3
            if player.y + 25 <= block1.y + 17:
            # game_world.remove_object(player)
                yForce -= 0.03

      
    if collide (player, block2):
        if player.y + 25 <= block2.y + 17:
            # game_world.remove_object(player)
            yForce -= 0.03
        else:
            yForce -= 0.015
        # if (player.x + 12 or player.x - 12) == (block2.x - 17):  
        #     # game_world.remove_object(player)
        #     player.x = block1.x - 16
        #     yForce = 0

        # ?????? ??? ???
        if player.x + 12 >= block2.x - 20 and player.y >= block2.y - 17 and player.y <= block1.y + 17 :  
            # game_world.remove_object(player)
            player.x -= 3
            if player.y + 25 <= block2.y + 17:
            # game_world.remove_object(player)
                yForce -= 0.03



    if collide (player, block3):
        if player.y + 25 <= block3.y + 17:
            # game_world.remove_object(player)
            yForce -= 0.03
        else:
            yForce = 0

        # if (player.x + 12 or player.x - 12) >= (block3.x - 17):  
        #     # game_world.remove_object(player)
        #     player.x = block1.x - 16
        #     yForce = 0

        # ?????? ??? ???
        if player.x + 12 >= block3.x - 20 and player.y >= block3.y - 17 and player.y <= block1.y + 17 :  
            # game_world.remove_object(player)
            player.x -= 3
            if player.y + 25 <= block3.y + 17:
            # game_world.remove_object(player)
                yForce -= 0.03

    if collide (player, block4):
        if player.y + 25 <= block4.y + 17:
            yForce -= 0.03
        else:
            yForce = 0

        # if (player.x + 12 or player.x - 12) >= (block4.x - 17):  
        #     # game_world.remove_object(player)
        #     player.x = block1.x - 16
        #     yForce = 0

        # ?????? ??? ???
        if player.x + 12 >= block4.x - 20 and player.y >= block4.y - 17 and player.y <= block1.y + 17 :  
            # game_world.remove_object(player)
            player.x -= 3
            if player.y + 25 <= block4.y + 17:
            # game_world.remove_object(player)
                yForce -= 0.03

    if collide (player, block5):
        if player.y + 25 <= block5.y + 17:
            # game_world.remove_object(player)
            yForce -= 0.03
        else:
            yForce = 0

        # ?????? ??? ???
        if player.x + 12 >= block5.x - 20 and player.y >= block5.y - 17 and player.y <= block1.y + 17 :  
            # game_world.remove_object(player)
            player.x -= 3
            if player.y + 25 <= block5.y + 17:
            # game_world.remove_object(player)
                yForce -= 0.03
        # ?????? ??? ???_2
        # if (player.x + 12 or player.x - 12) <= block5.x + 17: 
        #     game_world.remove_object(player)
        #     yForce = 0
        #     player.x = block5.x + 17
        # if (player.x + 12 or player.x - 12) >= (block5.x - 17):  
        #     # game_world.remove_object(player)
        #     player.x = block1.x - 16
        #     yForce = 0 

    if collide (player, Qblock1):
        if player.y + 25 <= Qblock1.y + 17:
            # game_world.remove_object(player)
            yForce -= 0.03
            Qblock1.collision = True
        else:
            yForce = 0

        # if (player.x + 12 or player.x - 12) >= (Qblock1.x - 17):  
        #     # game_world.remove_object(player)
        #     player.x = block1.x - 16
        #     yForce = 0

        # ?????? ??? ???
        if player.x + 12 >= Qblock1.x - 20 and player.y >= Qblock1.y - 17 and player.y <= block1.y + 17 :  
            # game_world.remove_object(player)
            player.x -= 3
            if player.y + 25 <= Qblock1.y + 17:
            # game_world.remove_object(player)
                yForce -= 0.03


    player.y += yForce


    if collide(player, background):
        yForce = 0

    elif yForce >= -10:
        yForce -= 0.015



# game object
    if collide (player, obj_Mush):
        game_world.remove_object(obj_Mush)
        obj_Mush.collision = True
    
    if collide (obj_Mush, block1):
        obj_Mush.yForce = 0
    if collide (obj_Mush, block2):
        obj_Mush.yForce = 0
    if collide (obj_Mush, block3):
        obj_Mush.yForce = 0
    if collide (obj_Mush, block4):
        obj_Mush.yForce = 0
    if collide (obj_Mush, block5):
        obj_Mush.yForce = 0
    if collide (obj_Mush, Qblock1):
        obj_Mush.yForce = 0

    if collide (obj_Mush, background):
        obj_Mush.yForce = 0
    elif obj_Mush.yForce >= -10:
        obj_Mush.y += obj_Mush.yForce
        obj_Mush.yForce -= 0.015

  



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()


    block1.draw(400 - player.x, 215)
    block2.draw(435 - player.x, 215)
    block3.draw(470 - player.x, 215)
    Qblock1.draw(505 - player.x, 215)
    block4.draw(540 - player.x, 215)
    block5.draw(575 - player.x, 215)
    transwall.draw()
    if fire == True:
        fire.draw()

    if obj_Mush == False:
        obj_Mush.draw()
    update_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a, = a.get_bb()
    left_b, bottom_b, right_b, top_b, = b.get_bb()


    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True
