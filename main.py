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
    xcor = player.xcor()
    xcor -= playerspeed
    if xcor < -280:
        xcor = -280
    player.setx(xcor)

def move_right():
    xcor = player.xcor()
    xcor += playerspeed
    if xcor > 280:
        xcor = 280
    player.setx(xcor)

def move_top():
    ycor = player.ycor()
    ycor += playerspeed
    player.sety(ycor)


def move_down():
    ycor = player.ycor()
    ycor -= playerspeed
    player.sety(ycor)

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



delay = input("Pressione enter para sair")

