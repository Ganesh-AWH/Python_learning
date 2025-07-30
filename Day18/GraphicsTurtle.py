from turtle import Turtle, Screen

turtle_obj = Turtle()
turtle_obj.shape("turtle")

for _ in range(10):
    turtle_obj.forward(10)
    turtle_obj.penup()
    turtle_obj.forward(10)
    turtle_obj.pendown()








screen_obj = Screen()
screen_obj.exitonclick()
