from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed('fastest')
        x_cor=random.randint(-280,280)
        y_cor=random.randint(-280,280)
        self.goto(x_cor,y_cor)