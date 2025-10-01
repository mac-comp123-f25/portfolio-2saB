"""The code draws circles that are layered to form a shape
that resembles a flower. The circles are drawn one after
the other layering 5 circles on top of each other before
it moves on to the next. There are 4 turtles that are
performing this function."""

import turtle
import math

def drawFiveCircles(turt, radius, centreX, centreY):
    turt.up()
    turt.goto(centreX, centreY)
    turt.down()

# repeats 5 times
    for i in [0, 1, 2, 3, 4, 5]:
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawFiveCircles(sepalTurtle, 50, 0, 0)

drawFiveCircles(petalTurtle, 25, 0, 0)

sepalTurtle.up()                    # TODO: Step 2: start here
sepalTurtle.goto(0, 0)
sepalTurtle.down()
"""Begin fill, till left is repeated 5 times"""

# for i in [0, 1, 2, 3,4, 5]:      # repeat four times
#     sepalTurtle.begin_fill()
#     sepalTurtle.circle(50)
#     sepalTurtle.end_fill()
#     sepalTurtle.left(72)



petalTurtle.up()
petalTurtle.goto(0, 0)
petalTurtle.down()

# for i in [0,1,2,3,4,5]:
#     petalTurtle.begin_fill()
#     petalTurtle.circle(25)
#     petalTurtle.end_fill()
#     petalTurtle.left(72)


centerTurtle.up()
centerTurtle.goto(0, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(0, 220)
sepalTurtle.down()

for i in [0,1,2,3,4,5]:
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)



petalTurtle.up()
petalTurtle.goto(0, 220)
petalTurtle.down()

for i in range (5):
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()
    petalTurtle.left(72)

centerTurtle.up()
centerTurtle.goto(0, 205)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(220, 0)
sepalTurtle.down()
for i in range(5):
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)

petalTurtle.up()
petalTurtle.goto(220, 0)
petalTurtle.down()

for i in range (5):
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()
    petalTurtle.left(72)


centerTurtle.up()
centerTurtle.goto(220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(0, -220)
sepalTurtle.down()

for i in range(5):
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)



petalTurtle.up()
petalTurtle.goto(0, -220)
petalTurtle.down()

for i in range(5):
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()
    petalTurtle.left(72)


centerTurtle.up()
centerTurtle.goto(0, -235)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(-220, 0)
sepalTurtle.down()

for i in range (5):
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)

petalTurtle.up()
petalTurtle.goto(-220, 0)
petalTurtle.down()

for i in range(5):
    petalTurtle.begin_fill()
    petalTurtle.circle(25)
    petalTurtle.end_fill()
    petalTurtle.left(72)

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()