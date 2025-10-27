from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.goto(0,-280)
        self.setheading(90)

    def SetupControls(self,screen):
        screen.listen()
        screen.onkey(self.MoveUp,'Up')
        screen.onkey(self.MoveDown, 'Down')
        screen.onkey(self.MoveRight, 'Right')
        screen.onkey(self.MoveLeft, 'Left')

    def MoveUp(self):
        self.setheading(90)
        self.forward(10)

    def MoveDown(self):
        self.setheading(270)
        self.forward(10)

    def MoveRight(self):
        self.setheading(0)
        self.forward(10)

    def MoveLeft(self):
        self.setheading(180)
        self.forward(10)