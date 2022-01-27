from turtle import Turtle, Screen

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.ht()
		self.penup()
		self.goto(0, 280)
		self.color("white")
		self.write_score()

	def write_score(self):
		self.write(f"Score : {self.score} ", align="center", font='Arial')

	def update_score(self):
		self.score += 1
		self.clear()
		self.write_score()

	def game_over(self):
		self.goto(0,0)
		self.write(f"GAME OVER", align="center", font='Arial')