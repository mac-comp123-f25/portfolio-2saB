import turtle

def draw_nested_squares(tt):
    """
    Draws nested squares using turtle graphics.
    The outer loop determines the side length (10 → 80, step 10).
    The inner loop draws the four sides of each square.
    """
    for side_length in range(10, 81, 10):   # 10, 20, ..., 80
        for _ in range(4):                  # draw 4 sides
            tt.forward(side_length)
            tt.left(90)  # turn to make square


# --- main script ---
win = turtle.Screen()
tt = turtle.Turtle()

draw_nested_squares(tt)

win.exitonclick()
