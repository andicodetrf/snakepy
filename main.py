from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.listen()
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	# detect collision with food
	if snake.head.distance(food) < 15:
		print("nom nom")
		food.refresh()
		# print(new_snake.print_segments())
		snake.extend()
		scoreboard.update_score()

	# detect collision with wall
	head_x = snake.head.xcor()
	head_y = snake.head.ycor()
	if head_x > 290 or head_x < -290 or head_y > 290 or head_y < -290:
		game_is_on = False
		scoreboard.game_over()

	# detect collision with tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			game_is_on = False
			scoreboard.game_over()


screen.exitonclick()
