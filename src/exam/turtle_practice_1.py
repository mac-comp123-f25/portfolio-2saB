"""
@author : Providence Thusabantu

This will draw as many number of 5 pointed stars as I desire of different sizes at random places.
"""

# importing the 2 modules I need for this exercise. Turtle to draw my stars. Random to randomize where the stars are drawn
import turtle
import random

# Defines our turtle program to determine the shape we're drawing
def draw_stars(turt, size):
    turt.begin_fill()
    for i in range(5):
        turt.forward(size)
        turt.left(216)
    turt.end_fill()


# defines the colors to be used to draw our stars, bcolor for background, and other for line and fill of stars
turtle.bgcolor("black")
turt = turtle.Turtle()
turt.color("red", "blue")
turt.speed(0)


# Defines our turtle program and loop function to draw our stars repeatedly till it has reached whatever number of stars we require
for i in range(200):
    turt.penup()
    x, y = random.randint(-300, 300), random.randint(-300, 300)
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    draw_stars(turt, random.randint(20, 35))
    turt.penup()
    turt.end_fill()


turtle.speed(0)


turtle.done()       # so that our screen does not disappear after its done carrying out our function