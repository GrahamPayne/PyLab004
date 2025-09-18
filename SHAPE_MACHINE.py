

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

                             #---------#SETUP#----------#

import turtle
import random


# creates turtle object
t = turtle.Turtle()
t.speed(10)
t.hideturtle()   #this hides the pointer

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("grey")
screen .setup(width=600, height=600)

t.clear()   #clears screen

#draws square
def draw_square(t, length):
    """This will draw the square with given side length"""
    for _ in range(4):
        t.forward(length)
        t.left(90)

draw_square(t, 100)


#Draws Circle
def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

# Example usage
draw_circle(t, 50)

#Draws Polygon
def draw_polygont(t, sides, length):
    """Draws a polygon with the given length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
draw_polygont(t, 6, 100)




turtle.exitonclick() #closes when clicked