import turtle as t
import random

"""
This solo project will draw Peppa pig. Started out wanting to draw the whole family but quickly 
realised how hard it is to draw just 1 character. I decided to draw Peppa with the clear sky, 
the sun, some flowers perhaps and just maybe a puddle of mud.
"""


def nose(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-30)
    t.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            t.left(3)
            t.forward(a)
        else:
            a = a - 0.08
            t.left(3)
            t.forward(a)
    t.end_fill()

    t.penup()
    t.setheading(90)
    t.forward(25)
    t.setheading(0)
    t.forward(10)
    t.pendown()
    t.pencolor(255, 155, 192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160, 82, 45)
    t.end_fill()

    t.penup()
    t.setheading(0)
    t.forward(20)
    t.pendown()
    t.pencolor(255, 155, 192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160, 82, 45)
    t.end_fill()

def head(x, y):
    t.color((255, 155, 192), "pink")
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.setheading(180)
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -95)
    t.setheading(161)
    t.circle(-300, 15)
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            t.left(3)
            t.forward(a)
        else:
            a = a - 0.08
            t.left(3)
            t.forward(a)
    t.end_fill()

def ears(x, y):
    t.color((255, 155, 192), "pink")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 54)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.forward(-12)
    t.setheading(0)
    t.forward(30)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 56)
    t.end_fill()

def eyes():
    t.color((255, 155, 192), "white")
    t.penup()
    t.setheading(90)
    t.forward(-20)
    t.setheading(0)
    t.forward(-95)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.penup()
    t.setheading(90)
    t.forward(12)
    t.setheading(0)
    t.forward(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.color((255, 155, 192), "white")
    t.penup()
    t.seth(90)
    t.forward(-25)
    t.seth(0)
    t.forward(40)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.penup()
    t.setheading(90)
    t.forward(12)
    t.setheading(0)
    t.forward(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

def cheek(x, y):
    t.color((255, 155, 192))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def mouth(x, y):
    t.color(239, 69, 19)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-80)
    t.circle(30, 40)
    t.circle(40, 80)

def body(x, y):
    t.color("red", (255, 99, 71))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(-130)
    t.circle(100, 10)
    t.circle(300, 30)
    t.setheading(0)
    t.forward(230)
    t.setheading(90)
    t.circle(300, 30)
    t.circle(100, 3)
    t.color((255, 155, 192), (255, 100, 100))
    t.setheading(-135)
    t.circle(-80, 63)
    t.circle(-150, 24)
    t.end_fill()

def hands(x, y):
    t.color((255, 155, 192))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-160)
    t.circle(300, 15)
    t.penup()
    t.setheading(90)
    t.forward(15)
    t.setheading(0)
    t.forward(0)
    t.pendown()
    t.setheading(-10)
    t.circle(-20, 90)
    t.penup()
    t.setheading(90)
    t.forward(30)
    t.setheading(0)
    t.forward(237)
    t.pendown()
    t.setheading(-20)
    t.circle(-300, 15)
    t.penup()
    t.setheading(90)
    t.forward(20)
    t.setheading(0)
    t.forward(0)
    t.pendown()
    t.setheading(-170)
    t.circle(20, 90)

def foot(x, y):
    t.pensize(10)
    t.color((240, 128, 128))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-90)
    t.forward(40)
    t.setheading(-180)
    t.color("black")
    t.pensize(15)
    t.forward(20)
    t.pensize(10)
    t.color((240, 128, 128))
    t.penup()
    t.setheading(90)
    t.forward(40)
    t.setheading(0)
    t.forward(90)
    t.pendown()
    t.setheading(-90)
    t.forward(40)
    t.setheading(-180)
    t.color("black")
    t.pensize(15)
    t.forward(20)

def tail(x, y):
    t.pensize(4)
    t.color((255, 155, 192))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(0)
    t.circle(70, 20)
    t.circle(10, 330)
    t.circle(70, 30)

def sun():
    t.penup()
    t.goto(310, 170)              # sun circle
    t.pendown()
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    for i in range(12):                  # sun rays
        t.penup()
        t.goto(300, 210)
        t.setheading(i * 30)
        t.forward(60)
        t.pendown()
        t.forward(20)


def flower(x, y, petal_color):
    t.penup()                   # stem
    t.pensize(4)
    t.goto(x, y)
    t.setheading(90)
    t.color("green")
    t.pendown()
    t.forward(70)

    t.setheading(0)                       # petals
    t.color(petal_color)
    for _ in range(5):
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.right(72)

    t.color("yellow")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.speed(0)

flower_colors = ["red", "pink", "blue", "orange", "purple", "white"]

for i in range(26):
    x = random.randint(-380, 380)
    y = random.randint(-230, -150)
    color = flower_colors[i % len(flower_colors)]
    flower(x, y, color)


def setting():
    t.pensize(4)
    t.hideturtle()
    t.colormode(255)
    t.color((255, 155, 192), "pink")
    t.setup(840, 500)
    t.bgcolor("skyblue")
    t.speed(0)

def main():
    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes()
    cheek(80, 10)
    mouth(-20, 30)
    body(-32, -8)
    hands(-56, -45)
    foot(2, -177)
    tail(148, -155)
    sun()
    flower(x, y, color)

    t.done()

if __name__ == '__main__':
    main()
