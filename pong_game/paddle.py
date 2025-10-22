from turtle import Turtle

PADDLE_SHAPE='square'
PADDLE_WIDTH=5
PADDLE_LENGTH=1
PADDLE_COLOR='white'
PADDLE_POSITION=(350,0)
PADDLE_SPEED='fastest'

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.CreatePaddle()

    def CreatePaddle(self):
        self.penup()
        self.speed(PADDLE_SPEED)
        self.shape(PADDLE_SHAPE)
        self.shapesize(PADDLE_WIDTH,PADDLE_LENGTH)
        self.color(PADDLE_COLOR)
        self.goto(PADDLE_POSITION)

    def MovePaddle(self):
        pass