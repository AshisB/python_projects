#This is the snake game in python
from turtle import Turtle, Screen
import random
import time
from snake import Snake


screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
# screen.bgpic('download.png')  need to use gif


snake=Snake()




is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.moveSnake()

                
        









screen.listen()
screen.exitonclick()

