from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Score_card
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()
food = Food()
score = Score_card()

screen.listen()
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
        score.update_score()
    
    #detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.game_over()
        is_game_on = False
    
screen.exitonclick()