from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.speed('fastest')
        self.shape('square')
        self.turtlesize(0.8, 1.5)
        self.color(random.choice(COLORS))









class CarManager:
    def __init__(self):
        self.cars = []
        self.y_position = []


    def CreateCar(self):
        if random.random()<0.3:
            car=Car()
            random_y = random.randrange(-280, 281, 20)

            self.y_position.append(random_y)

            # preventing cars overlapping
            while random_y in self.y_position:
                random_y = random.randrange(-280, 281, 20)

            car.goto(280, random_y)
            self.cars.append(car)

    def MoveCar(self, cars):
        for car in cars[:]:
            random_movement = random.randrange(5, 15, 2)
            car.setheading(180)
            car.forward(random_movement)
            if car.xcor() < -50:
                self.y_position = self.y_position[5:]
                print('reached here removing ypos')
            if car.xcor()<-280:
                cars.remove(car)
                car.hideturtle()
                print(f'removed {car.xcor()}')

