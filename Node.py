from State import State


class Node:

    def __init__(self, state, action, path_cost, road):
        self.state = State(state.map, state.car, action)
        self.action = action
        self.path_cost = path_cost
        self.path_cost_A = path_cost + (2 * self.state.map.in_street) + len(self.state.car.pets)
        self.road = []
        if action is not None:
            self.road.append(action)
        self.road = road + self.road
        self.hashcode = hash(str(self.state.map.board) + str(self.state.car.location))
