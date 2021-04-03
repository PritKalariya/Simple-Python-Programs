from turtle import *


setup(500, 500)


# Brush
speed(10)
bgcolor("black")
shape("turtle")
colormode(255)


def drawRound(size, filled):
    pendown()
    if filled == True:
        begin_fill()
    setheading(180)
    circle(size, 360)
    if filled == True:
        end_fill()


def drawRect(length, width, filled):
    setheading(0)
    pendown()
    if filled == True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled == True:
        end_fill()


def head():
    #
    color("blue", "blue")
    penup()
    goto(0, 100)
    drawRound(75, True)

    #
    color("white", "white")
    penup()
    goto(0, 72)
    drawRound(60, True)


def eyes():
    # Left eye socket
    color("black", "white")
    penup()
    goto(-15, 80)
    drawRound(17, True)

    # Right eye socket
    color("black", "white")
    penup()
    goto(19, 80)
    drawRound(17, True)

    #
    color("black", "black")
    penup()
    goto(-8, 70)
    drawRound(6, True)
    color("white", "white")
    penup()
    goto(-8, 66)
    drawRound(2, True)

    # Right eyeball
    color("black", "black")
    penup()
    goto(12, 70)
    drawRound(6, True)
    color("white", "white")
    penup()
    goto(12, 66)
    drawRound(2, True)


def nose():
    color("red", "red")
    penup()
    goto(0, 40)
    drawRound(7, True)


def mouth():
    # Mouth
    color("black", "black")
    penup()
    goto(-30, -20)
    pendown()
    setheading(-27)
    circle(70, 55)

    #
    penup()
    goto(0, 26)
    pendown()
    goto(0, -25)


def whiskers():
    color("black", "black")

    # Middle left
    penup()
    goto(10, 5)
    pendown()
    goto(-40, 5)

    # Middle right
    penup()
    goto(-10, 5)
    pendown()
    goto(40, 5)

    # Upper right
    penup()
    goto(10, 5)
    pendown()
    goto(40, 20)

    # Upper left
    penup()
    goto(10, 15)
    pendown()
    goto(-40, 20)

    # lower left
    penup()
    goto(-10, -5)
    pendown()
    goto(-40, -10)

    # Lower right
    penup()
    goto(10, -5)
    pendown()
    goto(40, -10)


def body():
    # Blue body
    color("blue", "blue")
    penup()
    goto(-50, -40)
    drawRect(100, 80, True)

    # White belly
    color("white", "white")
    penup()
    goto(0, -30)
    drawRound(40, True)

    # Red ribbon
    color("red", "red")
    penup()
    goto(-60, -35)
    drawRect(120, 10, True)

    # White legs
    color("white", "white")
    penup()
    goto(15, -127)
    pendown()
    setheading(90)
    begin_fill()
    circle(14, 180)
    end_fill()


def feet():
    # Left foot
    color("black", "white")
    penup()
    goto(-30, -110)
    drawRound(20, True)

    # Right foot
    color("black", "white")
    penup()
    goto(30, -110)
    drawRound(20, True)


def arms():
    # Left arm
    color("blue", "blue")
    penup()
    begin_fill()
    goto(-51, -50)
    pendown()
    goto(-51, -57)
    left(70)
    goto(-76, -85)
    left(70)
    goto(-86, -70)
    left(70)
    goto(-51, -50)
    end_fill()

    # Right arm
    color("blue", "blue")
    penup()
    begin_fill()
    goto(49, -50)
    pendown()
    goto(49, -75)
    left(70)
    goto(74, -85)
    left(70)
    goto(84, -70)
    left(70)
    goto(49, -50)
    end_fill()


def hands():
    # Left hand
    color("black", "white")
    penup()
    goto(-90, -71)
    drawRound(15, True)

    # Right hand
    color("black", "white")
    penup()
    goto(90, -71)
    drawRound(15, True)



head()
eyes()
nose()
mouth()
whiskers()
body()
feet()
arms()
hands()