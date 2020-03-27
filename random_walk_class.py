"""
Class to create a randomwalk object
"""

class RandomWalk:
    """
    A 2D randomwalk object. Variables included in the random
    walk are in the __init__ function.
    """
    def __init__(self, for_len_r, back_len_r, penup_prob, steps):

        """
        Parameters 
        ----------
        for_len_r: int
            integer lower limit on forward movement

        for_len_r2: int
            integer upper limit on forward movementf

        the turtle will randomly choose an integer
        between for_len_r1 and for_len_r2 and move
        forward that amount

        back_len_r1: int
            integer lower limit on backward movement

        back_len_r2: int
            integer upper limit on forward movement

        the turtle will randomly choose an integer
        between back_len_r1 and back_len_r2 and move
        backward that amount

        penup_prob: int
            number between 0-1 which represents the percentage of 
            time that the turtle lifts the pen up as it performs
            the 2d random walk. set this to 0 if you want no 
            gaps in the movement
        """

        self.for_len_r1, self.for_len_r2 = for_len_r
        self.back_len_r1, self.back_len_r2 = back_len_r
        self.penup_prob = penup_prob
        self.steps = steps

    def draw(self):
        """
        This function takes the variables from 
        __init__ and uses them to generate a
        2D random walk
        """
        import turtle
        import random
        t = turtle.Turtle()
        for x in range(self.steps):
            switch = random.randint(0,1) 
            penup_switch = (random.randrange(0,10))/10
            if switch:
                if penup_switch < self.penup_prob:
                    t.penup()
                t.forward(random.randrange(self.for_len_r1, self.for_len_r2))
            else:
                if penup_switch < self.penup_prob:
                    t.penup()
                t.backward(random.randrange(self.back_len_r1, self.back_len_r2))
            t.pendown()
            switch = random.randint(0,1)
            if switch:
                t.right(90)
            else:
                t.left(90)
