import turtle

# Set up the window
window = turtle.Screen()
window.bgcolor("lavender")

# Create turtle
turt = turtle.Turtle()
turt.color("blue")
turt.shape("turtle")

# Fill the triangle
turt.begin_fill()

# Draw equilateral triangle
for _ in range(3):
    turt.forward(200)   # move forward 200 units
    turt.left(120)      # turn left 120 degrees

turt.end_fill()

# Exit when clicked
window.exitonclick()
