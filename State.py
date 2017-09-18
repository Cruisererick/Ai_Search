from Map import Map
from Car import Car

class State:

    def __init__(self, map, car, action):
        self.map = Map(map.board, map.car_location, map.pets_not_in_house);
        self.car = Car(car.location, car.pets);
        self.action = action;
        self.execute()

    def execute(self):

        if self.action == "d":
            self.move_car_down();
        elif self.action == "l":
            self.move_car_left();
        elif self.action == "r":
            self.move_car_right();
        elif self.action == "u":
            self.move_car_up();



    def move_car_down(self):
        down_pos = self.map.car_location;
        down_pos = [down_pos[0] + 2, down_pos[1]];
        try:
            if self.map.board[down_pos[0] - 1, down_pos[1]] != 0:
                    self.map.move_car(down_pos,self.car);
            else:
                    pass;
        except:
            pass;

    def move_car_left(self):
        down_pos = self.map.car_location;
        down_pos = [down_pos[0], down_pos[1] - 2];
        try:
            if self.map.board[down_pos[0], down_pos[1] + 1] != 0:
                    self.map.move_car(down_pos,self.car);
            else:
                    pass;
        except:
            pass;

    def move_car_right(self):
        down_pos = self.map.car_location;
        down_pos = [down_pos[0], down_pos[1] + 2];
        try:
            if self.map.board[down_pos[0], down_pos[1] - 1] != 0:
                    self.map.move_car(down_pos,self.car);
            else:
                    pass;
        except:
            pass;

    def move_car_up(self):
        down_pos = self.map.car_location;
        down_pos = [down_pos[0] - 2, down_pos[1]];
        try:
            if self.map.board[down_pos[0] + 1, down_pos[1]] != 0:
                    self.map.move_car(down_pos,self.car);
            else:
                    pass;
        except:
            pass;

    def equals(self, state):
        map_equals = True;
        car_equals = True;
        X,Y = self.map.board.shape;

        if self.car.location != state.car.location:
            car_equals = False;

        for x in range(0, X):
            for y in range(0, Y):
                if self.map.board[x,y] != state.map.board[x,y]:
                    map_equals = False;

        if car_equals == True and map_equals == True:
            return True
        else:
            return False;

