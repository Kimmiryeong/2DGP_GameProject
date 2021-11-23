from pico2d import *
class Mushroom:
	def __init__(self):
		self.x, self.y = 505 , 247
		self.yForce  = 0
		self.collision = False
		self.image = load_image('Mushroom.png')

	def draw(self):
		if self.Qblock1.collision == True:
			self.image.draw(self.x - self.player.x, self.y)
			draw_rectangle(*self.get_bb())

	def update(self):
		
		if self.Qblock1.collision == True:
			self.x -= 0.3
		# pass
		

	def get_bb(self):
		x = self.x -self.player.x;
		return x - 15, self.y - 15, x + 15, self.y + 15

	def get_player(self, player):
		self.player = player

	def get_collision(self, Qblock1):
		self.Qblock1  = Qblock1