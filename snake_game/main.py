#This is the snake game in python
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from score import Score
from wall import Wall


screen = Screen()
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('green')
screen.tracer(0)
screen.bgpic('background.gif')


snake=Snake()
food=Food()
score=Score()
wall=Wall()



is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.moveSnake()
    if snake.head.distance(food)<15:
        food.refresh()
        score.scoreCount()


                
        









screen.listen()
screen.exitonclick()

