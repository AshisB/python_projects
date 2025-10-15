#This is the snake game in python
from turtle import Turtle, Screen
import random


screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('black')
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













screen.exitonclick()

