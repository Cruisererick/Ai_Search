from Map import Map
from Car import Car


class State:

    def __init__(self, map_passes, car, action):
        self.map = Map(map_passes.board, map_passes.car_location, map_passes.pets_not_in_house, map_passes.in_street)
        self.car = Car(car.location, car.pets)
        self.action = action
        self.execute()

    def execute(self):

        if self.action == "d":
            self.move_car_down()
        elif self.action == "l":
            self.move_car_left()
        elif self.action == "r":
            self.move_car_right()
        elif self.action == "u":
            self.move_car_up()

    def move_car_down(self):
        down_pos = self.map.car_location
        down_pos[0] += 2
        self.map.move_car(down_pos, self.car)

    def move_car_left(self):
        down_pos = self.map.car_location
        down_pos[1] -=  2
        self.map.move_car(down_pos, self.car)

    def move_car_right(self):
        down_pos = self.map.car_location
        down_pos[1] += 2
        self.map.move_car(down_pos, self.car)

    def move_car_up(self):
        down_pos = self.map.car_location
        down_pos[0] -= 2
        self.map.move_car(down_pos, self.car)
