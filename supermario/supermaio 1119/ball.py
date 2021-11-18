# from pico2d import*
# import game_world

# class Ball:
# 	image = None

# 	def __init__(self, x = 80, y = 100, velocity = 1):
# 		if Ball.image == None:
# 			Ball.image == load_image('fire.png')
# 		self.x, self.y, self.velocity = x, y, velocity

# 	def draw(self):
# 		self.image.draw(self.x, self.y)

# 	def update(self):
# 		self.x += self.velocity

# 		if self.x < 25 or self.x > 1600 - 25:
# 			game_world.remove_object(self)



from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('fire.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        if self.x < 30 or self.x > 1600 - 30:
            game_world.remove_object(self)

    def get_bb(self):
    	return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def get_ball(self, ball):
        self.ball = ball;


