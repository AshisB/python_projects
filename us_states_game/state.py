from turtle import Turtle,Screen

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
       

    def LocateState(self,xcor,ycor,state):
        self.goto(xcor, ycor)
        self.write(state, align='center', font=('Arial', 8, 'normal'))
