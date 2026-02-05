# Instructor shared code on 2023-10-12
import turtle 
t=turtle.Turtle()
for loop in range(10):
    t.forward(100)
    t.left(72)
import turtle
t=turtle.Turtle()
t.pencolor(input("enter the color"))
t.fillcolor("Darkblue")
ns = int(input("Enter a number for sides"))
for side in range(ns):
    t.forward(100)   # 1
    t.left(50)
t.begin_fill()   # begin filling
t.forward(100)   # 2
t.left(50)
t.forward(100)   # 3 
t.left(50)
t.forward(100)   # 4
t.end_fill()     # end filling
t.left(50)
t.forward(100)   # 5
t.left(50)

