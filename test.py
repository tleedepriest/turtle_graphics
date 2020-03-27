from random_walk_class import RandomWalk
from polygon_class import Polygon
import turtle 


random_walk = RandomWalk((25,50),(25,50), 0, 100)
random_walk.draw()

for x in range(3, 100):
    turtle.speed(100)
    if x%2 == 0:
        shape = Polygon(10,x)
        shape.draw()
    else:
        shape = Polygon(10,x, 'left')
        shape.draw()


turtle.done()
