import game_framework
from pico2d import *
import main_state

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

            else:
                if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                    game_framework.change_state(main_state)



def draw():
    clear_canvas()
    image.draw(1800, 1024)
    update_canvas()                



def draw():
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






