from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

#screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping pong")
screen.tracer(0)


l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()


screen.listen()
screen.onkey(key="Up", fun=l_paddle.go_up)
screen.onkey(key="Down", fun=l_paddle.go_down)

screen.onkey(key="w", fun=r_paddle.go_up)
screen.onkey(key="s", fun=r_paddle.go_down)


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()

