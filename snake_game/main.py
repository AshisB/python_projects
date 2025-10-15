#This is the snake game in python
from turtle import Turtle, Screen
import random


screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('black')
# screen.bgpic('download.png')
position=[20,-20,-40]
for i in range(3):
    snake=Turtle()
    snake.shape('square')
    snake.shapesize(stretch_wid=0.2, stretch_len=0.2)
    snake.goto(position[i],0)
    snake.color('white')
    snake.penup()








screen.exitonclick()

