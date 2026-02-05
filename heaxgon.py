import turtle
t = turtle.Turtle()
wn = turtle.Screen()
ns = 6
s = 50
a = 360/ns
for size in range(ns):
    t.forward(s)
    t.left(a)

t.pensize(1)
t.pencolor("black")

t.fillcolor("purple")

t.begin_fill()
t.left(60)
t.forward(50)

t.right(120)
t.forward(50)
t.end_fill()

t.fillcolor("blue")

t.begin_fill()
t.left(120)
t.forward(50)

t.left(120)
t.forward(50)
t.end_fill()

t.fillcolor("green")

t.begin_fill()
t.right(120)
t.forward(50)

t.right(120)
t.forward(50)
t.end_fill()

t.right(120)
t.forward(50)
t.end_fill()

t.fillcolor("beige")

t.begin_fill()
t.right(120)
t.forward(50)

t.left(120)
t.forward(50)
t.end_fill()

t.left(120)
t.forward(50)

t.fillcolor("orange")

t.begin_fill()
t.right(120)
t.forward(50)

t.right(120)
t.forward(50)
t.end_fill()

t.right(120)
t.forward(50)

t.fillcolor("green")

t.right(120)
t.forward(50)

t.begin_fill()
t.left(119)
t.forward(50)

t.left(119)
t.forward(50)
t.end_fill()

wn.exitonclick()
