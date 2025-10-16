#This is the snake game in python
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food


screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('green')
screen.tracer(0)
screen.bgpic('background.gif')


snake=Snake()
food=Food()




is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.moveSnake()

                
        









screen.listen()
screen.exitonclick()

