import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(200)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    #Turtle Tom
    tom = turtle.Turtle()
    tom.shape("turtle")
    tom.color("white")
    tom.speed(10)
    tom.pensize(3)

    for i in range(1, 40):
        draw_square(tom)
        tom.right(10)

    #Turtle Jerry
    jerry = turtle.Turtle()
    jerry.shape("turtle")
    jerry.color("blue")
    jerry.speed(5)
    jerry.pensize(2)

    size = 1

    while True:
        jerry.forward(size)
        jerry.right(91)
        size += 1

    window.exitonclick()

draw_art()