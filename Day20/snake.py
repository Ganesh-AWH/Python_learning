from turtle import Turtle
#constant values
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        #head of the snake
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    #constant moving of snake
    def move(self):
        # for seg_num in range(start=1, stop=0, step=-1)
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(DISTANCE)
        

    
    