from turtle import Screen, Turtle
import time

# --- PADDLE CLASS ---
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("dodgerblue")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        if self.xcor() > -340:
            self.setx(self.xcor() - 40)

    def move_right(self):
        if self.xcor() < 340:
            self.setx(self.xcor() + 40)

# --- BALL CLASS ---
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, -100)
        self.bounce_y()

# --- BRICK CLASS ---
class Brick(Turtle):
    def __init__(self, x_cor, y_cor, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.color(color)
        self.goto(x_cor, y_cor)

# --- MAIN GAME ENGINE ---
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Python Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = []

# Generate Bricks
colors = ["red", "orange", "yellow", "green", "blue"]
for row in range(5):
    for col in range(-7, 8):
        new_brick = Brick(col * 50, 250 - (row * 30), colors[row])
        bricks.append(new_brick)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Wall Collisions
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()

    # Paddle Collision
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Brick Collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            brick.goto(2000, 2000) # Move off-screen
            bricks.remove(brick)
            ball.bounce_y()
            break

    # Missed Paddle
    if ball.ycor() < -290:
        ball.reset_position()

screen.exitonclick()