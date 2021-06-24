import turtle
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle


alex.color("green")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)

alex.color("red")    # alex has a color
alex.left(110)          # alex turns 110 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)

alex.color("blue")    # alex has a color
alex.right(950)         # alex turns 950 degrees right
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)
