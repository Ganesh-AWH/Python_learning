from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def goto_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finishingPoint(self):
        y_cor = self.ycor()
        if y_cor > FINISH_LINE_Y:
            return True
        else:
            return False