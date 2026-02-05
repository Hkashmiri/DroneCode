from turtle import Screen, Turtle

screen = Screen()

a = Turtle()
b = Turtle()

for _ in range(4):
    a.forward(100)
    a.left(90)

for _ in range(4):
    b.backward(100)
    b.right(90)

a.clear()

screen.exitonclick()
