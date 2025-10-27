from turtle import Screen,Turtle
from car_manager import CarManager
import time
import random

screen=Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.tracer(0)


car_list=[]

game_is_on=True
while game_is_on:
    time.sleep(0.8)
    screen.update()
    car = CarManager()
    car_list.append(car)
    car.MoveCar(car_list)




















screen.exitonclick()