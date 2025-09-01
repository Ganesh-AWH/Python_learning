from turtle import Turtle, Screen

tut = Turtle()
screen = Screen()


def move_forwards():
    tut.forward(10)

def move_backwards():
    tut.backward(10)
    
def counter_clock():
    tut.left(10)

def clockwise():
    tut.right(10)

def clear_screen():
    tut.clear()
    tut.penup()
    tut.home()
    tut.pendown()
    
    
screen.listen()
#move forwards
screen.onkey(key="w", fun=move_forwards)
#move backwards
screen.onkey(key="s", fun=move_backwards)

#turnning tut to anti clock wise 
screen.onkey(key="a", fun=counter_clock)

#turnning the tut to clock wise
screen.onkey(key="d", fun=clockwise)

#clearing the screen
screen.onkey(key="c", fun=clear_screen)
#turning tut to anti clock 
screen.exitonclick()