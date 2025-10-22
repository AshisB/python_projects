from turtle import Turtle
HALF_WIDTH=300
TOTAL_WIDTH=HALF_WIDTH*2
BRICK_SIZE=5
NUMBER_OF_BRICKS=round(TOTAL_WIDTH/BRICK_SIZE)

class Brick(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('brown')
        self.goto(x,y)


        # self.shapesize(0.2,0.2)

class Wall():
    def __init__(self):
        self.bricks=[]
        self.createWalls()

    def createWalls(self):
            for i in range(NUMBER_OF_BRICKS):
                brick1=Brick(-(HALF_WIDTH)+(BRICK_SIZE*i),HALF_WIDTH)
                brick2 = Brick(-(HALF_WIDTH) + (BRICK_SIZE * i), -HALF_WIDTH+10)
                self.bricks.append(brick1)
                self.bricks.append(brick2)