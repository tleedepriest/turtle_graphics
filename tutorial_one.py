#Python Turtle Graphics Tutorial #1 - Introduction 


import turtle 

travis = turtle.Turtle() #give your turtle a name 
travis.color("Purple") #give the turtle a color
travis.pensize(8) #give the line the turtle draws a thickness
#travis.shape('turtle') #arrow, circle, ....


travis.forward(100) #move the turtle forward 100 pixels
travis.left(90) #turn the turtle left 90 degress 
travis.penup() #lift the turtle off the page so it so not draw

travis.forward(100) #move the turtle forward 100 pixels...but don't draw
travis.right(90) #turn the turtle 90 degrees
travis.pendown() #put the turtle back down on the page so we can draw again
travis.color("green") #change the color of the pen
travis.forward(100) #move forward 100 pixels while drawing a green line 



nadine = turtle.Turtle()
nadine.color("black")
nadine.pensize(20)
nadine.backward(100)

turtle.done()
