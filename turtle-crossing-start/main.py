from turtle import Screen,Turtle
from car_manager import CarManager
from player import Player
from score import Score
import time


screen=Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.tracer(0)


player=Player()
player.SetupControls(screen)

score=Score()

car = CarManager()

game_is_on=True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car.CreateCar()
    car.MoveCar(car.cars,player)
    if player.ycor() > 280:
        score.LevelUpdate()
        is_next_level=player.NextLevel()
        if is_next_level:
            car.IncreaseSpeed()

    #detect collision with cars and calculate score
    for unit_car in car.cars:

        # Detect Collision
        head_x = player.xcor()
        head_y = player.ycor() + 10
        if unit_car.distance(player) < 15 or unit_car.distance(head_x,head_y)<15:
            score.GameOver()
            game_is_on=False
        else:
            # Calculate Score

            if player.ycor() > unit_car.ycor() and unit_car.distance(player) < 25 and unit_car.scored==0:
                score.ScoreUpdate()
                unit_car.scored=1






















screen.exitonclick()