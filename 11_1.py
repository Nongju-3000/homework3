import turtle

def tree(length):
    if length > 5:
        turtle.forward(length)
        turtle.right(20)
        tree(length - 15)
        turtle.left(40)
        tree(length - 15)
        turtle.right(20)
        turtle.backward(length)

t = turtle.Turtle()
t.left(90)

t.color("green")
t.speed(1)
tree(90)