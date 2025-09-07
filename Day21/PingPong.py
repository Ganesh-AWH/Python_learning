from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time

#screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping pong")
screen.tracer(0)


l_paddle = Paddle((-375, 0))
r_paddle = Paddle((375, 0))
ball = Ball()
scoreboard = ScoreBoard()


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

    #Detecting collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        #call bounce logic
        ball.bounce_y()    
    
    #Detect collison with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
    
    #Detecting ball goes out of the bound
    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()

