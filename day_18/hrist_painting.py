#Hrist painting recreating
#imports
import colorgram
from turtle import Turtle,Screen
import random

#initializing objects
kurma=Turtle()
kurma.color('blue')
kurma.speed(5)

screen=Screen()
screen.colormode(255)


#functions
def colorDot():
    hirst_colors=[]
    colors=colorgram.extract('image/hirst_dots.jpg',13)
    for color in colors:
        red=color.rgb.r
        green=color.rgb.g
        blue=color.rgb.b
        if red < 200 or green < 200 or blue < 200:
            color_tuple = (red, green, blue)
            hirst_colors.append(color_tuple)
    return hirst_colors

#
def dotLine(count):
    # dot_colors= colorDot()
    #print(dot_colors)
    dot_colors=[(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17)]
    for _ in range(count):
        kurma.pendown()
        kurma.dot(20,random.choice(dot_colors))
        kurma.penup()
        kurma.forward(50)


def getNewOrigin(angle):
    kurma.penup()
    kurma.setheading(angle)
    kurma.forward(200)
    new_origin=kurma.position()
    kurma.setheading(0)
    return new_origin
    # print(new_origin)


def makeHirst(number,origin):

    for distance in range(1,number+1):
        dotLine(number)
        kurma.setpos(origin[0], origin[1])
        kurma.right(90)
        kurma.forward(40*distance)
        kurma.left(90)

# def makeHirst(number,origin):
#     for distance in range(1,number+1):
#         dotLine(number)
#         kurma.setpos(origin[0],origin[1])
#         kurma.left(90)
#         kurma.forward(40*distance)
#         kurma.right(90)




#our code
kurma.hideturtle()
makeHirst(10,getNewOrigin(145))






















screen.exitonclick()