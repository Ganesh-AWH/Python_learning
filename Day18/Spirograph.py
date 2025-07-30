import random
import turtle
from turtle import Turtle, Screen

def generate_random_rgb_color():
    """Generates a single random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

turtle.colormode(255)
tut = Turtle()
tut.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tut.color(generate_random_rgb_color())
        tut.circle(100)
        tut.setheading(tut.heading() + size_of_gap)

draw_spirograph(2)

sc = Screen()
sc.exitonclick()