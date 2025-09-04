from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Score_card(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.display_score()
        self.hideturtle()
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()
    
    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
        