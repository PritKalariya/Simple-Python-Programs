from turtle import *

screen = Screen()

pen = Turtle()
pen.speed(5)


pen.penup()
pen.goto(-400, 250)
pen.pendown()


# Orange Rectangle
# White Rectangle
pen.color("Orange")
pen.begin_fill()
pen.forward(800)
pen.right(90)
pen.forward(167)
pen.right(90)
pen.forward(800)
pen.end_fill()
pen.left(90)
pen.forward(167)

# Green Reactangle
pen.color("green")
pen.begin_fill()
pen.forward(167)
pen.left(90)
pen.forward(800)
pen.left(90)
pen.forward(167)
pen.end_fill()

# Blue circle
pen.penup()
pen.goto(70, 0)
pen.pendown()
pen.color("navy")
pen.begin_fill()
pen.circle(70)
pen.end_fill()

# White circle
pen.penup()
pen.goto(60, 0)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(60)
pen.end_fill()

# Mini blue circle
pen.penup()
pen.goto(-57, -8)
pen.pendown()
pen.color("navy")
for i in range(24):
    pen.begin_fill()
    pen.speed(20)
    pen.circle(3)
    pen.end_fill()
    pen.penup()
    pen.forward(15)
    pen.right(15)
    pen.pendown()

# Small blue circles
pen.penup()
pen.goto(20, 2)
pen.pendown()
pen.begin_fill()
pen.circle(20)
pen.end_fill()
# spokes
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.pensize(2)
for i in range(24):
    pen.forward(60)
    pen.backward(60)
    pen.left(15)

done()