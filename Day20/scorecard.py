from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Score_card(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #using file to track high score
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.update_score()
        self.hideturtle()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    
    def increase_score(self):
        self.score += 1
        self.update_score()   
        
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()
        
