from turtle import Turtle,Screen




kurma=Turtle()
screen=Screen()
screen.listen()

# functions

def forward():
    kurma.forward(10)

def backward():
    kurma.backward(10)

def counterClockWise():
    kurma.left(10)


def clockWise():
    kurma.right(10)


def clear():
    kurma.clear()

def reset():
    kurma.home()
    clear()

def button(k,func):
    screen.onkey(key=k,fun=func)


button('w',forward)
button('s',backward)
button('a',counterClockWise)
button('d',clockWise)
button('C',clear)
button('R',reset)


screen.exitonclick()