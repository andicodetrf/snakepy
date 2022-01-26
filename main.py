from turtle import Screen, Turtle
import time
from snake import Snake

# my_range = list(range(9, -1, -1))
# somelist = [1,2,3,4,5]
# print(my_range)
# print(somelist[::-1])

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.listen()
screen.tracer(0)

# tim = Turtle("turtle")
# tim.color("white")
# tim.goto(-50, -50)
#
# def moveup():
# 	tim.setheading(90)
#
# screen.onkey(moveup, "Up")

game_is_on = True
new_snake = Snake()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

while game_is_on:
	screen.update()
	time.sleep(0.1)
	new_snake.move()




screen.exitonclick()
