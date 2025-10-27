from turtle import Turtle


BALL_COLOR='red'
BALL_DISTANCE=20
BALL_SHAPE='circle'



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.angle=0
        self.movex=10
        self.movey=10
        self.speedball=0.1


    def MoveBall(self):
        xcor=self.xcor()+self.movex
        ycor = self.ycor() + self.movey
        self.goto(xcor,ycor)

    def BounceBall(self):
        self.movex*=-1
        self.speedball*=0.7



    def BounceWall(self):
        self.movey *= -1


    def ResetBall(self):
        self.goto(0,0)
        self.movex*=-1
        self.speedball=0.1

