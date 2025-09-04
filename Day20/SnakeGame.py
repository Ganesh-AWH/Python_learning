from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()

screen.listen()
food = Food()


screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
    
screen.exitonclick()