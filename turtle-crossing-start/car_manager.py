from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.speed('slowest')
        self.shape('square')
        self.turtlesize(1, 2)
        self.color(random.choice(COLORS))
        self.CreateCar()




    def CreateCar(self):
        random_y = random.randrange(-280, 281, 40)
        self.goto(280, random_y)


    def MoveCar(self, cars):
        for car in cars[:]:
            random_movement = random.randrange(10, 25, 10)
            car.setheading(180)
            car.forward(random_movement)
            if car.xcor()<-280:
                cars.remove(car)
                car.hideturtle()
                print(f'removed {car.xcor()}')

