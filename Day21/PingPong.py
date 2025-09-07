from turtle import Screen, Turtle
from paddle import Paddle

#screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping pong")
screen.tracer(0)


l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))



screen.listen()
screen.onkey(key="Up", fun=l_paddle.go_up)
screen.onkey(key="Down", fun=l_paddle.go_down)

screen.onkey(key="w", fun=r_paddle.go_up)
screen.onkey(key="s", fun=r_paddle.go_down)


is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()

