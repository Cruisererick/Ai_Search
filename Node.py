from State import State;

class Node:

    def __init__(self, problem, state, action, path_cost, road):
        self.problem = problem;
        self.state = State(state.map, state.car, None);
        self.action = action;
        self.path_cost = path_cost;
        self.road = [];
        if action != None:
            self.road.append(action);
        self.road = road + self.road;

        self.execute_action();
        self.hashcode = hash(str(self.state.map.board) + str(self.state.car.location));





    def execute_action(self):
        if self.action != None:
            self.state = State(self.state.map, self.state.car, self.action);
        else:
            pass;
