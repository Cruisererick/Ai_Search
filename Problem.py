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

    def check_actions(self, state):
        can_do = [];
        for actions in self.actions:
            if actions == "d":
                down_pos = state.map.car_location;
                down_pos = [down_pos[0] + 1, down_pos[1]];
                try:
                    if state.map.board[down_pos[0], down_pos[1]] != 0:
                        can_do.append("d");
                except:
                    pass;
            elif actions == "l":
                down_pos = state.map.car_location;
                down_pos = [down_pos[0], down_pos[1] - 1];
                try:
                    if state.map.board[down_pos[0], down_pos[1]] != 0:
                        can_do.append("l");
                except:
                    pass;
            elif actions == "r":
                down_pos = state.map.car_location;
                down_pos = [down_pos[0], down_pos[1] + 1];
                try:
                    if state.map.board[down_pos[0], down_pos[1]] != 0:
                        can_do.append("r");
                except:
                    pass;
            elif actions == "u":
                down_pos = state.map.car_location;
                down_pos = [down_pos[0] - 1, down_pos[1]];
                try:
                    if state.map.board[down_pos[0], down_pos[1]] != 0:
                        can_do.append("u");
                except:
                    pass;
        return can_do;


