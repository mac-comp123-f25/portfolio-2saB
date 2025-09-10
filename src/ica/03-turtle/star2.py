import turtle

# Set up the window
window = turtle.Screen()
window.bgcolor("lavender")

# First turtle
star1 = turtle.Turtle()
star1.color("blue")
star1.shape("turtle")

# Draw a five-pointed star
for i in range(5):
    star1.forward(100)
    star1.right(144)  # key angle for a star

# Second turtle
star2 = turtle.Turtle()
star2.color("red")
star2.shape("turtle")

# Move second turtle to a new location
star2.penup()
star2.goto(200, 0)  # move right of the first star
star2.pendown()

# Draw another five-pointed star
for i in range(5):
    star2.forward(100)
    star2.right(144)

# Exit on click
window.exitonclick()
