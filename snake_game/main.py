#This is the snake game in python
from turtle import Turtle, Screen
import random
import time


screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
# screen.bgpic('download.png')



#snake body
segments=[]
positions=[0,-20,-40]
for position in positions:
    snake_segment=Turtle()
    snake_segment.penup()
    snake_segment.color('white')
    if position==0:
        snake_segment.shape('triangle')
    else:
        snake_segment.shape('square')
    snake_segment.goto(position,0)

    segments.append(snake_segment)

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.6) 
    count_seg=len(segments)
   
    # for count in range(count_seg):
    #     if segments[count]==segments[0]:
    #         store=segments[count].pos()
    #         # segments[count].left(90)
    #         segments[count].forward(20)
    #     else:
    #         swap=store
    #         store=segments[count].pos()
    #         segments[count].goto(swap)


    for i in range(count_seg-1,0,-1):
        x_cor=segments[i-1].xcor()
        y_cor=segments[i-1].ycor()
        segments[i].goto(x_cor,y_cor)

    segments[0].left(90)
    segments[0].forward(20)

           
                
        










screen.exitonclick()

