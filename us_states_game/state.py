from turtle import Turtle,Screen

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
       

    def LocateState(self,xcor,ycor,state):
        # Move to the coordinates first, then write the state name there.
        # Writing before moving prints at the turtle's current position (usually 0,0).
        print(f'here x cor is {xcor} and y cor is {ycor}')
        self.goto(xcor, ycor)
        self.write(state, align='center', font=('Arial', 8, 'normal'))
