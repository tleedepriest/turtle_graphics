"""
Class to create a randomwalk object
"""
import random

class RandomWalk(object):
    """
    A 2D randomwalk object. Variables included in the random
    walk are in the __init__ function.
    """
    def __init__(self, turtle, steps):

        """
        Parameters 
        ----------

        
        Returns
        ----------
        None
        """
        self.turtle = turtle
        self.steps = steps
    
    def draw_random_walk(self):
        """
        Parameters
        -------------
        self

        Returns
        -------------
        None 

        This is the main function which executes the two
        functions below
        """
        for _ in range(self.steps):
            self.move()
            self.turn()

    def move(self, for_len=(25, 50), back_len=(25, 50), penup_prob=0):
        """
        Parameters
        ------------
        for_len_r: tuple containing ints --> (25, 50)
            the turtle will randomly choose a value
            between 25 and 50 and move forward that amount

        OR

        for_len_r: int
            turtle always moves forward this length

        ####################################################

        back_len_r: tuple containing ints --> (25, 50)
            the turtle will randomly choose an integer
            between 25 and 50 and move backward that amount

        OR

        back_len_r: int
            the turtle will always move backward this amount

        ####################################################

        penup_prob: int
            an number between 0 and 1 (0 inclusive 1 exclusive)
            0 means the turtle will never be lifted while the turtle
            draws .99 means the turtle will be lifted 99% of the time
            while the turtle draws. Higher number, less visible lines.

            no more than digits after decimal
        
        Returns
        --------------
        None
        
        this function moves the turtle forward half of the time and
        backward half of the time while drawing at least
        """
        def check_type(tuple_or_int):
            """
            Parameters
            -----------
            tuple_or_int: tuple or int
                if tuple generate random number in tuple range
                if int do nothin
            
            Returns
            ----------
            length: int
                the lenth the turtle will move
            """

            if isinstance(tuple_or_int, tuple):
                length = random.randrange(*tuple_or_int)
            elif isinstance(tuple_or_int, int):
                length = tuple_or_int
            else:
                raise ValueError("for_len must be of type tuple or int")

            return length

        switch = random.randint(0, 1)
        penup_switch = random.uniform(0, 1)

        if switch:
            if penup_switch < penup_prob:
                self.turtle.penup()
            self.turtle.forward(check_type(for_len))
            
        else:
            if penup_switch < penup_prob:
                self.turtle.penup()
            self.turtle.backward(check_type(back_len))

        self.turtle.pendown()

    def turn(self, right_angle=90, left_angle=90):
        """
        please the pylint gods
        """
        switch = random.randint(0, 1)

        if switch:
            self.turtle.right(right_angle)
        else:
            self.turtle.left(left_angle)

