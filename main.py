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
border_caneta.color("red")
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
jogador = turtle.Turtle()
jogador.color("yellow")
jogador.shape("triangle")
jogador.penup()
jogador.speed(0)
jogador.setposition(0,-250)
    

delay = input("Pressione enter para sair")

