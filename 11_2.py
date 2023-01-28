import turtle

def drawBar(height):
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(height)
    turtle.write(str(height), font = ('Times New Roman', 16, 'bold'))
    turtle.right(90)

    turtle.forward(40)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

data = [120, 56, 309, 220, 156, 23, 98]

t=turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)

for i in data:
    drawBar(i)