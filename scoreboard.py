from turtle import Turtle, Screen


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = self.get_high_score()
		self.ht()
		self.penup()
		self.goto(0, 280)
		self.color("white")
		self.write_score()

	def get_high_score(self):
		with open("hs.txt") as file:
			retrieved_score = file.read()
			return int(retrieved_score)

	def write_high_score(self, hs):
		with open("hs.txt", mode="w") as file:
			file.write(str(hs))

	def write_score(self):
		self.clear()
		self.write(f"Score : {self.score} | High Score: {self.high_score}", align="center", font='Arial')

	def update_score(self):
		self.score += 1
		self.write_score()

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			self.write_high_score(self.high_score)

		self.score = 0
		self.write_score()


	# def game_over(self):
	# 	self.goto(0,0)
	# 	self.write(f"GAME OVER", align="center", font='Arial')