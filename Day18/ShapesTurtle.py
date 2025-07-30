from turtle import Turtle,Screen


tut = Turtle()
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tut.forward(100)
        tut.right(angle)


for i in range(3, 11):
    draw_shape(i)

    




sc = Screen()
sc.exitonclick()