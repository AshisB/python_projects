from turtle import Screen,Turtle
from car_manager import CarManager
from player import Player
import time
import random

screen=Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.tracer(0)


player=Player()
car = CarManager()


game_is_on=True
while game_is_on:
    time.sleep(0.6)
    screen.update()
    car.CreateCar()
    car.MoveCar(car.cars)




















screen.exitonclick()