from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
DOWN = 270
UP = 90


class Snake:
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def print_segments(self):
		temp = []
		for seg in self.segments:
			temp.append(seg.position())
		return temp

	def create_segment(self, segment_pos):
		new_segment = Turtle("square")
		new_segment.color('white')
		new_segment.penup()

		new_segment.goto(segment_pos)
		self.segments.append(new_segment)

	def create_snake(self):
		for pos in STARTING_POS:
			self.create_segment(pos)

	def move(self):
		for seg_num in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[seg_num - 1].xcor()
			new_y = self.segments[seg_num - 1].ycor()
			# print(f"{seg_num}: x - {new_x}, y - {new_y}")
			self.segments[seg_num].goto(new_x, new_y)

		self.head.forward(MOVE_DISTANCE)

	def extend(self):
		self.create_segment(self.segments[-1].position())

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)








# class Snake:
# 	def __init__(self):
# 		start_pos = [(0, 0), (-20, 0), (-40, 0)]
# 		self.segments = []
#
# 		for pos in start_pos:
# 			segment = Turtle("square")
# 			segment.color('white')
# 			segment.penup()
# 			segment.goto(pos)
# 			self.segments.append(segment)
#
# 	def update_pos(self):
# 		for seg_num in range(len(self.segments) - 1, 0, -1):
# 			new_x = self.segments[seg_num - 1].xcor()
# 			new_y = self.segments[seg_num - 1].ycor()
# 			self.segments[seg_num].goto(new_x, new_y)
#
# 	def move(self):
# 		self.segments[0].forward(20)
#
# game_is_on = True
# new_snake = Snake()
#
# while game_is_on:
# 	screen.update()
# 	time.sleep(0.1)
# 	new_snake.update_pos()
# 	new_snake.move()