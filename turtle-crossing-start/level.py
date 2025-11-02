from car_manager import Car,CarManager
from player import Player


class Level:
    def __init__(self,car,level):
        self.level=level
        self.car=car

    def ManageLevel(self):
        if self.level==2:
            print('reached here')
            self.car.IncreaseSpeed()

