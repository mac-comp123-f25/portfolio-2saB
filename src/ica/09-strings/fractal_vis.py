import turtle
from fractal.l_system import apply_l_system
from fractal.fractal_engine import draw_fractal

def draw_koch_antisnowflake(tur, n, angle, step_size):
    axiom = 'F'
    rules = {'F': 'F+F--F+F'}
    l_system = apply_l_system(axiom, rules, n)

    draw_fractal(tur, l_system, angle, step_size)

if __name__ == '__main__':
    scr = turtle.Screen()
    tur = turtle.Turtle()
    tur.hideturtle()
    tur.speed(0)
    tur.up()
    tur.down()

    draw_koch_antisnowflake(tur, 4, 60, 5)

    tur.up()
    tur.forward(50)
    tur.color('red')
    tur.write('done')
    scr.mainloop()

# tur.clickonexit()

# n = 4
# axiom = F++F++F
# rule = F → F+F--F+F
# δ = 60°
# s = 1 / 3
