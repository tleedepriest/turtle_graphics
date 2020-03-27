import turtle
import random

travis = turtle.Turtle()

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

#travis.color('yellow', 'purple') #outline, fill

#travis.width(5)
#travis.begin_fill()
#travis.circle(100)
#travis.end_fill()

#travis.penup()
#travis.forward(150)
#travis.penup()
#travis.forward(200)
#travis.left(90)
#travis.forward(100)
#travis.pendown()
#travis.color('yellow', 'black')

#travis.begin_fill()

#for x in range(4):
#    travis.forward(100)
#    travis.right(90)

#travis.end_fill()

for x in range(100):
    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)
    r = random.randrange(0,75)
    color_index = random.randrange(0, len(colors))
    travis.color(colors[color_index], colors[color_index])
    travis.setpos(x, y)
    travis.pendown()
    travis.begin_fill()
    travis.circle(r)
    travis.end_fill()
    travis.penup()


turtle.done()
