#This is the snake game in python
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from score import Score
from wall import Wall,Brick


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
    time.sleep(0.1)
    snake.moveSnake()

    #collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        score.scoreCount()
        snake.addSegment()

    # reappear from another side (left/right)
    if snake.head.xcor()>310 or snake.head.xcor()<-310 :
        snake.reappear()

    #Detect collision with wall
    for unit_brick in wall.bricks:
        if snake.head.distance(unit_brick) <11:
            # score.hitTheWall()
            # is_game_on=False
            score.resetScore()
            snake.resetSnake()


    # Detect collision with tail
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            # score.hitTheWall()
            # is_game_on = False
            score.resetScore()
            snake.resetSnake()







                
        









screen.listen()
screen.exitonclick()

