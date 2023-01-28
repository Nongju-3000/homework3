import turtle
import random

color = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black"]

def start(length):
    turtle.penup()
    turtle.goto(random.randrange(-200, 200), random.randrange(-200, 200))
    turtle.pendown()
    turtle.color(random.choice(color))
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()


n = int(input("Enter a number: "))
for i in range(n):
    start(random.randrange(50, 200))
turtle.done()
