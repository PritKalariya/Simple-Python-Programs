from turtle import *

color('green')
bgcolor('black')
speed(10)
hideturtle()

c = 0
while c < 200:
    right(c)
    forward(c * 3)
    c += 1