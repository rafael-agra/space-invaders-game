#Import list
import turtle
import os

#Setting up the screen 
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Border drawing
border_caneta = turtle.Turtle()
border_caneta.speed(0)
border_caneta.color("white")
border_caneta.penup()
border_caneta.setposition(-300,-300)
border_caneta.pendown()
border_caneta.pensize(4)

#Drawing square 
for side in range(4):
    border_caneta.fd(600)
    border_caneta.lt(90)
border_caneta.hideturtle()

#Create the player
player = turtle.Turtle()
player.color("yellow")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#Moving player in X and Y axis
playerspeed = 15

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def move_top():
    y = player.ycor()
    y += playerspeed
    player.sety(y)


def move_down():
    y = player.ycor()
    y -= playerspeed
    player.sety(y)

#Create Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_top, "Up")
turtle.onkey(move_down, "Down")

#Create enemy 
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)
enemyspeed = 3

#-----------------------
#      Main game 
#-----------------------
while True:

    #move enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280 or  enemy.xcor() < -280 :
        y = enemy.ycor()
        y -=40
        enemyspeed *= -1
        enemy.sety(y)

    


delay = input("Pressione enter para sair")

