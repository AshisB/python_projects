from turtle import Turtle,Screen
import random
import colo
kurma=Turtle()
screen=Screen()

screen.colormode(255)
shellcolors=[
            "red",
            "green",
            "blue",
            "yellow",
            "orange",
            "purple",
            "pink",
            "brown",
            "black",
            "white",
            "gray",
            "cyan",
            "magenta",
            "gold",
            "silver",
        ]
kurma.color('aquamarine')
kurma.shape('turtle')
kurma.shapesize(1,1)
# kurma.resizemode('user')
#
# for i in range(4):
#     kurma.forward(100)
#     kurma.right(90)


#
kurma.pensize(3)
#
# for _ in range(10):
#     kurma.pendown()
#     kurma.forward(10)
#     kurma.penup()
#     kurma.forward(10)
#

# draw shapes
for i in range(3,11):
    for _ in range(i):
        kurma.forward(100)
        kurma.right(360/i)
    kurma.color(random.choice(shellcolors))
    kurma.pencolor(random.choice(shellcolors))


















screen.exitonclick()