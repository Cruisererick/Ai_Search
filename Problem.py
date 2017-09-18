from State import State;
from Map import Map;
from Car import Car;

class Problem:

    def __init__(self, map_string):
        self.Create_Initial(map_string);
        self.actions = ["d", "l", "r", "u"];


    def Goal_Test(self, state):
        if 0 == state.map.pets_not_in_house:
            return True;
        else:
            return False;

    def Create_Initial(self, map_string):
        self.map = Map(map_string);
        self.car = Car(self.map.car_location)
        self.initial = State(self.map, self.car, None);

