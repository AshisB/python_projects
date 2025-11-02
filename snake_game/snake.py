#snake class file
from turtle import Turtle,Screen

STARTING_POS=[(0,0),(-10,0),(-20,0)]
MOVE_DISTANCE=10
SNAKE_SIZE=0.5
SNAKE_HEAD_COLOR='red'
SNAKE_HEAD_SHAPE='square'
SNAKE_BODY_COLOR='white'
SNAKE_BODY_SHAPE='circle'
UP,DOWN,RIGHT,LEFT=90,270,0,180

class Snake:
    def __init__(self):
        self.segments = []
        self.speed=10
        self.createSnake()
        self.segment=None
        self.head=self.segments[0]
        self.head.shape(SNAKE_HEAD_SHAPE)
        self.head.color(SNAKE_HEAD_COLOR)
        self.setupControl()

    def snakeSegment(self):
        snake_segment = Turtle()
        snake_segment.shapesize(SNAKE_SIZE, SNAKE_SIZE)
        snake_segment.speed(self.speed)
        snake_segment.penup()
        snake_segment.color(SNAKE_BODY_COLOR)
        snake_segment.shape(SNAKE_BODY_SHAPE)
        self.segment = snake_segment


    def createSnake(self):
        # snake body
        for position in STARTING_POS:
            self.snakeSegment()
            self.segment.goto(position)
            self.segments.append(self.segment)




    def moveSnake(self):
        count_seg = len(self.segments)

        # for count in range(count_seg):
        #     if segments[count]==segments[0]:
        #         store=segments[count].pos()
        #         # segments[count].left(90)
        #         segments[count].forward(20)
        #     else:
        #         swap=store
        #         store=segments[count].pos()
        #         segments[count].goto(swap)

        for i in range(count_seg - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)



        self.head.forward(MOVE_DISTANCE)


    def setupControl(self):
        screen = Screen()
        screen.listen()
        screen.onkey(self.moveUp, 'w')
        screen.onkey(self.moveRight, 'd')
        screen.onkey(self.moveLeft, 'a')
        screen.onkey(self.moveDown, 's')
        #alternatives
        screen.onkey(self.moveUp, 'Up')
        screen.onkey(self.moveRight, 'Right')
        screen.onkey(self.moveLeft, 'Left')
        screen.onkey(self.moveDown, 'Down')




    def moveUp(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def reappear(self):
        sym=-1
        new_ycor=self.head.ycor()
        new_xcor = (sym*self.head.xcor())-(sym*MOVE_DISTANCE+10)
        self.head.goto(new_xcor,new_ycor)


    def addSegment(self):
        self.snakeSegment()
        self.segments.append(self.segment)


    def resetSnake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.__init__()
        # self.moveSnake()




