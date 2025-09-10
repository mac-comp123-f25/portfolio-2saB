#Make a turtle and set its color using the color method. Use the shape method to change it to the 'turtle' shape or one of the alternatives: ("arrow", "circle", "square", "triangle", "classic"). Then write statements to have the turtle trace a five-pointed star. This will require 5 copies of a move forward followed by a turn. Note that the angle of each point in a five-pointed star is 36 degrees.
import turtle

# Set up the window
window = turtle.Screen()
window.bgcolor("lavender")

# First turtle
star1 = turtle.Turtle()
star1.color("blue")
star1.shape("turtle")

# Draw a five-pointed star (no loop)
star1.forward(100)
star1.right(144)

star1.forward(100)
star1.right(144)

star1.forward(100)
star1.right(144)

star1.forward(100)
star1.right(144)

star1.forward(100)
star1.right(144)

# Second turtle
star2 = turtle.Turtle()
star2.color("red")
star2.shape("turtle")

# Move second turtle to a new location
star2.penup()
star2.goto(200, 0)  # move right of the first star
star2.pendown()

# Draw another five-pointed star (no loop)
