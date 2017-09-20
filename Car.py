class Car:

    def __init__(self, car_pos, pets=[]):
        self.location = car_pos
        self.pets = pets.copy()

    def take_pet(self, pet):
        self.pets.append(pet)
        return True

    def drop_pet(self, house):
        pet_to_drop = house + 32

        for x in range(0, len(self.pets)):
            if self.pets[x] == pet_to_drop:
                del self.pets[x]
                return True
        else:
            return False
