import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=player.move)

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()    
    car_manager.run()
    
    #detecting collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    
screen.exitonclick()