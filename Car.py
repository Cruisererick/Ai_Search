import numpy as np

class Car:

    def __init__(self, car_pos, pets = np.zeros(4)):
        self.location = car_pos;
        self.pets = np.zeros(4);
        for x in range (0, 3):
            self.pets[x] = pets[x];

    def take_pet(self, pet):
        for x in range (0, 3):
            if self.pets[x] == 0:
                self.pets[x] = pet
                return True;
        else:
            return False

    def drop_pet(self, house):
        pet_to_drop = house + 32;

        for x in range (0, 3):
             if self.pets[x] == pet_to_drop:
                self.pets[x] = 0;
                return True;
        else:
            return False;
