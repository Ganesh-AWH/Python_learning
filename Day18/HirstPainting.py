import colorgram
import turtle
from turtle import Turtle, Screen
import random

tut = Turtle()
turtle.colormode(255)
tut.speed("fastest")
tut.penup()

colors = colorgram.extract('e:/Programming/Python/Udemy Course/Day18/image.jpg', 30)

rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color.append((r, g, b))

tut.setheading(225)
tut.forward(300)
tut.setheading(0)
no_of_dots = 100    

for dot_count in range(1, no_of_dots+1):
    tut.dot(20, random.choice(rgb_color))
    tut.forward(50)
    
    if dot_count % 10 == 0:
        tut.setheading(90)
        tut.forward(50)
        tut.setheading(180)
        tut.forward(500)
        tut.setheading(0)


sc = Screen()
sc.exitonclick()