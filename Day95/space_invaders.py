import turtle
import math
import random

# --- SCREEN SETUP ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Space Invaders")
screen.setup(width=800, height=600)
screen.tracer(0)

# --- PLAYER PADDLE ---
player = turtle.Turtle()
player.color("lime")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.goto(0, -250)

playerspeed = 20

# --- BULLET SYSTEM ---
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 3
bulletstate = "ready" # "ready" means ready to fire, "fire" means moving

# --- ALIEN SWARM ---
number_of_aliens = 30
aliens = []

for i in range(number_of_aliens):
    aliens.append(turtle.Turtle())

alien_start_x = -225
alien_start_y = 250
alien_number = 0

for alien in aliens:
    alien.color("red")
    alien.shape("square") # In a real game, you'd use a GIF shape
    alien.penup()
    x = alien_start_x + (50 * (alien_number % 10))
    y = alien_start_y - (40 * (alien_number // 10))
    alien.goto(x, y)
    alien_number += 1

alienspeed = 0.2

# --- FUNCTIONS ---
def move_left():
    x = player.xcor() - playerspeed
    if x < -380: x = -380
    player.setx(x)

def move_right():
    x = player.xcor() + playerspeed
    if x > 380: x = 380
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    return distance < 20

# --- BINDINGS ---
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet, "space")

# --- MAIN GAME LOOP ---
while True:
    screen.update()
    
    # Move the aliens
    for alien in aliens:
        x = alien.xcor()
        x += alienspeed
        alien.setx(x)

        # Move aliens down and change direction
        if alien.xcor() > 380 or alien.xcor() < -380:
            for a in aliens:
                a.sety(a.ycor() - 40)
            alienspeed *= -1

        # Check for collision with bullet
        if is_collision(bullet, alien):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.goto(0, -400)
            alien.goto(0, 1000) # Move dead alien off-screen
            
        # Check for Game Over
        if alien.ycor() < -230:
            print("GAME OVER")
            exit()

    # Bullet Movement
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"