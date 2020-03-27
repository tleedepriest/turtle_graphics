import turtle
import random

t = turtle.Turtle()
t.color('black', 'black')
t.begin_fill()

for i in range(2):
    t.circle(25, 180)
    t.right(-45)
    t.circle(-20,-180)

t.circle(25,180)
t.right(-20)
t.circle(-20,-180)

for i in range(2):
    t.circle(25, 180)
    t.right(-45)
    t.circle(-20,-180)

t.home()
t.end_fill()
turtle.done()
