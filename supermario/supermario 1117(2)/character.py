import game_framework
from pico2d import *


import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 100.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# 


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    # (SDL_KEYDOWN, SDLK_UP): JUMP_DOWN,
    # (SDL_KEYUP, SDLK_UP): JUMP_UP
}


class IdleState:

    def enter(Mario, event):
        if event == RIGHT_DOWN:
            Mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Mario.velocity += RUN_SPEED_PPS
        Mario.timer = 500

    def exit(Mario, event):
        if event == SPACE:
            Mario.fire_ball()
        pass

    def do(Mario):
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        Mario.timer -= 1
        if Mario.timer == 0:
            Mario.add_event(SLEEP_TIMER)

    def draw(Mario):
        # if Mario.dir == 1:
        #     Mario.image.clip_draw(int(Mario.frame) * 100, 300, 100, 100, Mario.x, Mario.y)
        # else:
        #     Mario.image.clip_draw(int(Mario.frame) * 100, 200, 100, 100, Mario.x, Mario.y)
        # Mario.x += Mario.dir * 0.4
        Mario.image.draw(Mario.x, Mario.y)


class RunState:

    def enter(Mario, event):
        if event == RIGHT_DOWN:
            Mario.velocity += RUN_SPEED_PPS
            Mario.left = 0
            Mario.go = 1
        elif event == LEFT_DOWN:
            Mario.velocity -= RUN_SPEED_PPS
            Mario.left = 1
            Mario.go = 1
        elif event == RIGHT_UP:
            if Mario.velocity == 0 :
                Mario.left = 1
            Mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Mario.left = 0
            Mario.velocity += RUN_SPEED_PPS
        Mario.dir = clamp(-1, Mario.velocity, 1)

    def exit(Mario, event):
        # if event == SPACE:
        #     Mario.fire_ball()
        pass

    def do(Mario):
        #Mario.frame = (Mario.frame + 1) % 8
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        Mario.x += Mario.velocity * game_framework.frame_time
        Mario.x = clamp(25, Mario.x, 1600 - 25)

    def draw(Mario):
        # if Mario.dir == 1:
        #     Mario.image.clip_draw(int(Mario.frame) * 100, 100, 100, 100, Mario.x, Mario.y)
        # else:
        #     Mario.image.clip_draw(int(Mario.frame) * 100, 0, 100, 100, Mario.x, Mario.y)
        Mario.x += Mario.dir * 0.4
        if Mario.left == 1:
            Mario.image_leftrun.draw(Mario.x, Mario.y)
        else:
            Mario.image_run.draw(Mario.x, Mario.y)


class SleepState:

    def enter(Mario, event):
        Mario.frame = 0

    def exit(Mario, event):
        pass

    def do(Mario):
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(Mario):
        # if Mario.dir == 1:
        #     Mario.image.clip_composite_draw(int(Mario.frame) * 100, 300, 100, 100, 3.141592 / 2, '', Mario.x - 25, Mario.y - 25, 100, 100)
        # else:
        #     Mario.image.clip_composite_draw(int(Mario.frame) * 100, 200, 100, 100, -3.141592 / 2, '', Mario.x + 25, Mario.y - 25, 100, 100)
        # Mario.x += Mario.dir * 0.4
        Mario.image.draw(Mario.x, Mario.y)






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
    # JumpState: {JUMP_UP : RunState, JUMP_DOWN : RunState}
}

class Mario:

    def __init__(self):
        self.x, self.y = 100, 129
        self.image = load_image('mario_standing.gif')
        self.image_run = load_image('run1.gif')
        self.image_left = load_image('left.jpg')
        self.image_leftrun = load_image('left_run.jpg')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.left = 0
        self.go = 0


    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self,event)


    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

