

'''
                             ░██
 ░███████   ░███████   ░████████  ░███████
░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██
░██        ░██    ░██ ░██    ░██ ░█████████
░██    ░██ ░██    ░██ ░██   ░███ ░██
 ░███████   ░███████   ░█████░██  ░███████

           ░██
           ░██
 ░███████  ░██ ░██    ░██  ░████████
░██        ░██ ░██    ░██ ░██    ░██
 ░███████  ░██ ░██    ░██ ░██    ░██
       ░██ ░██ ░██   ░███ ░██   ░███
 ░███████  ░██  ░█████░██  ░█████░██
                                 ░██
                           ░███████
'''

# ---------- SETUP ----------
import turtle
import random

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)

# Create turtle
t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.pencolor("darkorange")
t.penup()
t.clear()


# ---------- BASIC SHAPES ----------
def draw_square(t, length):
    """Draw a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)


def draw_circle(t, radius):
    """Draw a circle with the given radius."""
    t.circle(radius)


def draw_polygon(t, sides, length):
    """Draw a regular polygon """
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


# ---------- COMPOSITES ----------
def draw_pumpkin(t, x, y, radius):
    """Draw a pumpkin centered at (x, y) with a stem on top."""
    # body
    t.penup()
    t.goto(x, y - radius)  # move to bottom so circle centers at (x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # stem (keeps your left-turn sequence; just positions it)
    t.fillcolor("green")
    t.begin_fill()
    t.penup()
    t.goto(x + radius // 10, y + radius)  # start so rectangle centers over top
    t.setheading(0)
    t.pendown()
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.end_fill()


def draw_eye(t, x, y, size):
    """Draw a triangular eye at (x, y)."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()


def draw_mouth(t, x, y, width, height=22, teeth=6):
    """
    Draw a jack-o-lantern mouth with SHARP triangular teeth.
    """
    seg = width / teeth

    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()

    cx = x
    for _ in range(teeth):
        t.goto(cx + seg / 2, y - height)  # tip of tooth
        t.goto(cx + seg, y)  # back to baseline
        cx += seg

    # close the shape along the top back to start
    t.goto(x, y)
    t.end_fill()


def draw_star(t, x, y, size):
    """Draw a filled 5-point star."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def draw_sky(t, num_stars, pumpkins=None, margin=25):
    """
    Draw stars; if pumpkins provided as list of (x, y, r),
    place stars above the tallest stem (plus margin).
    """
    min_x, max_x = -300, 300
    max_y = 300

    if pumpkins:
        safe_min_y = max((y + r + (r // 2)) for (_, y, r) in pumpkins) + margin
    else:
        safe_min_y = 0

    safe_min_y = min(max_y - 10, max(safe_min_y, -250))

    for _ in range(num_stars):
        x = random.randint(min_x, max_x)
        y = random.randint(int(safe_min_y), max_y - 10)
        size = random.randint(10, 24)
        draw_star(t, x, y, size)


# ---------- Lovely SCENE ----------
t.clear()

# centers and sizes (x, y_center, radius)
pumpkins = [
    (-150, -200, 100),  # left
    (0, -205, 90),  # middle
    (150, -200, 120),  # right
]

# LEFT
draw_pumpkin(t, *pumpkins[0])
draw_eye(t, -190, -140, 30)
draw_eye(t, -110, -135, 30)
draw_mouth(t, -190, -170, 80)

# MIDDLE
draw_pumpkin(t, *pumpkins[1])
draw_eye(t, -20, -155, 25)
draw_eye(t, 20, -155, 25)
draw_mouth(t, -35, -182, 70)

# RIGHT
draw_pumpkin(t, *pumpkins[2])
draw_eye(t, 110, -130, 30)
draw_eye(t, 190, -130, 30)
draw_mouth(t, 110, -170, 80)

# Stars (kept clear of stems)
draw_sky(t, 15, pumpkins=pumpkins, margin=25)

# keep window open until click (must be last)
turtle.exitonclick()
