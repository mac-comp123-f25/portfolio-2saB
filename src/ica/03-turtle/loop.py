import turtle
wind = turtle.Screen()
turt = turtle.Turtle()

wind.bgcolor("pink")
turt.forward(200)
turt.right(180)

wind.bgcolor("light green")
turt.forward(200)
turt.right(180)

wind.bgcolor("yellow")
turt.forward(200)
turt.right(180)

wind.bgcolor("blue")
wind.exitonclick()


# We can simplify this by doing the following (try this):
wind = turtle.Screen()
turt = turtle.Turtle()

for back_color in ['pink', 'light green', 'yellow', 'blue']:
   wind.bgcolor(back_color)
   turt.forward(200)
   turt.right(180)
wind.exitonclick()


# Often we simply want to repeat some action a fixed number of times. Using the range function will help us with that:
wind = turtle.Screen()
turt = turtle.Turtle()
wind.bgcolor("light green")
for reps in range(20):
   turt.forward(200)
   turt.right(180)
wind.exitonclick()

