from turtle import Turtle
DIVIDER_SHAPE='square'
DIVIDER_WIDTH=1
DIVIDER_LENGTH=0.5
DIVIDER_COLOR='white'

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.CreateDivider()


    def CreateDivider(self):
        self.penup()
        self.speed('fastest')
        self.shape(DIVIDER_SHAPE)
        self.shapesize(DIVIDER_WIDTH,DIVIDER_LENGTH)
        self.color(DIVIDER_COLOR)

        for number in range(-300, 301, 40):
            self.goto(0, number)
            self.stamp()


