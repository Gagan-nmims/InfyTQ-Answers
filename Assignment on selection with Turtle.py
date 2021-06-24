import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color('red')           # alex has a color

alex.circle(50)              # draws a circle of radius 50
alex.backward(100)  # alex moves 100 positions backward
alex.left(90)  # alex turns 90 degrees left
alex.forward(100)            # alex moves 100 positions forward
alex.right(90)               # alex turns 90 degrees right
alex.forward(200)
alex.right(90)
alex.forward(100)
alex.right(90)  
alex.forward(90)
alex.backward(90)
alex.left(90)