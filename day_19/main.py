from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=500,height=400)

colors=["red","green","blue","yellow","purple","orange"]
screen.textinput(title="Make a bet",prompt="Please choose turtle color: red, green, blue, yellow, purple, orange=>")

ypos=-150
for color in colors:
    kurma=Turtle(shape="turtle")
    kurma.color(color)
    kurma.penup()
    kurma.goto(x=-230,y=ypos)
    ypos+=50

screen.exitonclick()
