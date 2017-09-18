import numpy as np;



class Map:


    def __init__ (self, board, car_pos = 0, pets = -1):
        self.pets_not_in_house = 0;
        if type(board) == str:
            self.board = self.boardToMap(board);
        else:
            self.board = np.copy(board);

        if car_pos == 0:
            self.car_location = self.car_initial();
        else:
            self.car_location = car_pos
        if pets == -1:
            self.pets_not_in_house = self.pets_not_in_house / 2;
        else:
            self.pets_not_in_house = pets;



    def boardToMap(self, board):
        lines = [];
        line = []
        for x in range(0, len(board)):

            if board[x] == ".":
                line.extend([0])
            elif board[x] == "|":
                line.extend([1])
            elif board[x] == "-":
                line.extend([-1])
            elif board[x] == "+":
                line.extend([-5]);
            elif board[x] == "^":
                line.extend([-10]);
            elif board[x] == ";":
                lines.append(line);
                line = [];
            else:
                tohex = ord(board[x]);
                line.extend([tohex]);
                self.pets_not_in_house = self.pets_not_in_house + 1;

        for line in lines:
            if 'map' in locals():
                aux_array = np.array(line);
                map = np.vstack([map,aux_array]);
            else:
                map = np.array(line)
        return map


    def car_initial(self):
        [x,y] = np.where(self.board == -10)
        return [x[0],y[0]];

    def move_car(self, car_pos, car):

        if 96 < self.board[car_pos[0], car_pos[1]] < 123:
            if car.take_pet(self.board[car_pos[0], car_pos[1]]):
                self.pet_taken(car_pos);
                self.car_location = car_pos;
                car.location = car_pos;
            else:
                self.car_location = car_pos;
                car.location = car_pos;
        elif 64 < self.board[car_pos[0], car_pos[1]] < 91:
            for pet in car.pets:
                if pet - 32 == self.board[car_pos[0], car_pos[1]]:
                    car.drop_pet(self.board[car_pos[0], car_pos[1]])
                    self.pet_in_house(car_pos);
            self.car_location = car_pos;
            car.location = car_pos;

        else:
            self.car_location = car_pos;
            car.location = car_pos;

    def pet_taken(self, taken_pos):
        self.board[taken_pos[0], taken_pos[1]] = -1;

    def pet_in_house(self, house_pos):
        self.board[house_pos[0], house_pos[1]] = -1;
        self.pets_not_in_house = self.pets_not_in_house - 1;
