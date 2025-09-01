from turtle import Turtle, Screen
import random

screen = Screen()
is_game_on = False

#width-xaxis and height-yaxis
screen.setup(height=500, width=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
tut_positions = [-60, -30, 0, 30, 60, 90]
all_turtles = []


for tut_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tut_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=tut_positions[tut_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_game_on = True

while is_game_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost, The {winning_color} turtle is the winner!")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()