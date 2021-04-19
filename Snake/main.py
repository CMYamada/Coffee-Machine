from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # collision detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment()

    # collision detection with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        gameOn = False
        scoreboard.game_over()

    # collision detection with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameOn = False
            scoreboard.game_over()





screen.exitonclick()