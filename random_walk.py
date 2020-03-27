"""
This program generates a turtle which undergoes a 2d randomwalk
if the turtle is still in the screen/window
"""
from tkinter import *
import turtle 
import random


colors = ['red', 'green', 'purple']
travis = turtle.Turtle()
travis.speed(10)
wn = turtle.Screen()

def is_in_screen(w, t):
    left_bound = -(w.window_width()/2)
    right_bound = (w.window_width()/2)
    top_bound = (w.window_height()/2)
    bottom_bound = -(w.window_height()/2)

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    if turtle_x >= left_bound and turtle_x <= right_bound:
        in_screen = True
    else:
        in_screen = False
    if turtle_y >= bottom_bound and turtle_y <= top_bound:
        in_screen = True
    else:
        in_screen = False
    return in_screen

for x in range(4):
    while is_in_screen(wn,travis):
        switch = random.randint(0,1)
        penup_switch = random.randrange(0,10)
        if switch:
            if penup_switch < 3:
                travis.penup()
            travis.forward(25)
        else:
            if penup_switch < 3:
                travis.penup()
            travis.backward(random.randrange(25,50))
        travis.pendown()
        switch = random.randint(0,1)
        if switch:
            travis.right(90)
        else:
            travis.left(90)
    travis.penup()
    travis.home() #move the turtle back into the center of the screen
    if colors:
        travis.color(colors.pop())
    travis.pendown()

turtle.getscreen().getcanvas().postscript(file="random_walk.eps")
turtle.done()



