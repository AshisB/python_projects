from turtle import Turtle,Screen


PADDLE_SHAPE='square'
PADDLE_WIDTH=5
PADDLE_LENGTH=1
PADDLE_COLOR='white'
PADDLE_SPACE=30
PADDLE_SPEED='fastest'
PADDLE_DRAG_LENGTH=250

class PongPaddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.position=(x,y)
        self.CreatePaddle()


    def CreatePaddle(self):
        self.penup()
        self.speed(PADDLE_SPEED)
        self.shape(PADDLE_SHAPE)
        self.shapesize(PADDLE_WIDTH,PADDLE_LENGTH)
        self.color(PADDLE_COLOR)
        self.goto(self.position)


    def MoveUp(self):

        if self.y<PADDLE_DRAG_LENGTH:
            self.y=self.y+PADDLE_SPACE
        self.goto(self.x, self.y)

    def MoveDown(self):
        if self.y>-PADDLE_DRAG_LENGTH:
            self.y=self.y-PADDLE_SPACE
        self.goto(self.x,self.y)





    #
    # def DragMove(self,x,y):
    #     self.ondrag(None)
    #     x = self.x
    #     if y < PADDLE_DRAG_LENGTH:
    #         y = y
    #     else:
    #         y = PADDLE_DRAG_LENGTH
    #
    #     if y > -PADDLE_DRAG_LENGTH:
    #         y = y
    #     else:
    #         y = -PADDLE_DRAG_LENGTH
    #
    #     self.goto(x, y)
    #     self.ondrag(self.DragMove)
