from turtle import Turtle, Screen, register_shape
import random
kurma=Turtle()
screen=Screen()
# screen.setup(width=500, height=200)
# screen.setworldcoordinates(-400, -300, 400, 300)

screen.colormode(255)


def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple


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
            "gray",
            "cyan",
            "magenta",
            "gold",
        ]
kurma.color('aquamarine')
kurma.shape('turtle')
kurma.shapesize(0.5,0.5)
kurma.pensize(1)
kurma.speed(10)

directions=[0,90,180,270]
i=0


#kurma to make a random walk
def draw_circle(gap):
    i=gap
    while True:
        kurma.circle(100)
        kurma.left(gap)
        kurma.pencolor(randomColor())
        if i==360:
            break
        else:
            i= gap + i
#
# def draw_circle(gap):
#     for _ in range(int(360/gap)):
#         kurma.circle(100)
#         kurma.left(gap)
#         kurma.pencolor(randomColor())


draw_circle(10)


# while True:
#     kurma.forward(25)
#     kurma.setheading(random.choice(directions))
#     kurma.pencolor(randomColor())
#      i += 1
#     # Check if back at origin
#     x, y = kurma.position()
#     if abs(x) < 1 and abs(y) < 1:
#         print(f"Returned to origin after {i} steps!")
#         break
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


screen.exitonclick()