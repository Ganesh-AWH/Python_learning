import random
import turtle
from turtle import Turtle, Screen


def generate_random_rgb_color():
    """Generates a single random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tut = Turtle()
turtle.colormode(255)

directions = [0, 90, 180, 270]
tut.pensize(10)
tut.speed("fastest")
for _ in range(200):
    tut.color(generate_random_rgb_color())
    tut.forward(30)
    tut.setheading(random.choice(directions))

sc = Screen()
sc.exitonclick()