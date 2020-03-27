import turtle

def fib(n,t):
    if n>2:
        if n%2 ==0:
            t.right((n-2)+(n-1))
        else:
            t.left((n-2)+(n-1))
        t.forward((n-2)+(n-1))
        t.penup()
        t.home()
        t.pendown()
        return fib(n-1, t)


t = turtle.Turtle()
t.speed(100)
fib(91, t)
turtle.done()

