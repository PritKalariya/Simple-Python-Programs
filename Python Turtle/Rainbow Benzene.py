import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

tom = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    tom.pencolor(colors[x % 6])
    tom.width(x / 100 + 1)
    tom.forward(x)
    tom.left(59)