from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
screen.exitonclick()