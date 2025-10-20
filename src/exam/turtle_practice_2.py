"""
@author : Providence Thusabantu

This will draw a 36 pointed stars as I desire at any point that I click on the screen. Goal is to make an interactive turtle.
"""

# importing the module I need for this exercise. Turtle to draw my stars.
import turtle


# Defines our turtle program to determine the shape we're drawing
def draw_star(x, y):
    turtle.speed(200)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.color('red', 'yellow')      # color and fill of the star

    turtle.begin_fill()

    for i in range(36):
        turtle.forward(150)
        turtle.left(170)

    turtle.end_fill()

# This sends the turtle to draw the star at the point at which there is a click
turtle.getscreen().onclick(draw_star)

draw_star(0, 0)

turtle.done()
