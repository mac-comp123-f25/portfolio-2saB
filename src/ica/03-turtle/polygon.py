import turtle

# Number of sides in the polygon
n = 6   # change this to 3 for a triangle, 4 for a square, 5 for pentagon, etc.

# Set up the window
window = turtle.Screen()
window.bgcolor("lavender")

# Create turtle
turt = turtle.Turtle()
turt.color("blue")
turt.shape("turtle")

# Fill the polygon
turt.begin_fill()

# Draw regular polygon with n sides
for _ in range(n):
    turt.forward(100)         # side length
    turt.left(360 / n)        # turn based on polygon angle

turt.end_fill()

# Exit when clicked
window.exitonclick()
