import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("pink")

# Create turtle
turt = turtle.Turtle()
turt.color("teal")
turt.fillcolor("turquoise")
turt.shape("turtle")
turt.speed(5)

# Function to draw an equilateral triangle
def draw_triangle(size):
    for _ in range(3):
        turt.forward(size)
        turt.left(120)

# Draw first triangle
turt.begin_fill()
draw_triangle(200)
turt.end_fill()

# Move to draw inverted triangle
turt.begin_fill()
turt.right(60)   # rotate to start upside-down triangle
draw_triangle(200)
turt.end_fill()

# Exit when clicked
window.exitonclick()
