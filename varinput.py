import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()
l = int(input("enter left angle"))
r = int(input("enter right angle"))
f = int(input("enter forward length"))
penc = input("enter color")
pens = int(input("enter pen size"))
alex.pencolor(penc)
alex.pensize(pens)
alex.forward(f)           # tell alex to move forward by 150 units
alex.left(l)               # turn by 90 degrees
alex.forward(f)
alex.right(r)
alex.forward(f)
