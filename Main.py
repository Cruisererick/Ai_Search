from Loader import Loader
from Map import Map
from Problem import Problem
from Node import Node
import queue
import itertools




def breadth_first (problem):
    tie_breaker = itertools.count()
    road = [];
    node = Node(problem, problem.initial, None, 0, road);
    frontier = queue.PriorityQueue();
    touple = (node.path_cost, next(tie_breaker), node)
    frontier._put(touple);
    explored = set();


    while True:
        if frontier.empty():
            return False;
        touple = frontier.get();
        node = touple[2];

        if problem.Goal_Test(node.state) == True:
            return node;

        explored.add(node.state)

        for actions in problem.actions:
            child = Node(problem, node.state, actions, node.path_cost + 1, node.road);

            in_frontier = False;
            in_explored = False;
            auxfrontier = queue.PriorityQueue();
            for x in range (0, frontier.qsize()):
                touple = frontier.get();
                auxnode = touple[2];
                if auxnode.state.equals(child.state):
                    in_frontier = True;
                auxfrontier.put(touple);
            frontier = auxfrontier;

            for states in explored:
                if (states.equals(child.state) == True):
                    in_explored = True;

            if in_frontier == False and in_explored == False:
                touple = (child.path_cost, next(tie_breaker), child)
                frontier._put(touple);
            elif  in_frontier == True:
                auxfrontier = queue.PriorityQueue();
                for x in range (0, frontier.qsize()):
                    touple = frontier.get();
                    auxnode = touple[2];
                    if auxnode.state.equals(child.state):
                        if child.path_cost < auxnode.path_cost:
                            frontier.get()
                            touple = [child.path_cost, child]
                            auxfrontier.put(touple);
                    else:
                        auxfrontier.put(touple);
                frontier = auxfrontier;


def main():
    file = "C:/Users/Juan/Desktop/AI_Search/lumosity_breadth_first_search_train.csv"
    csv = Loader(file);
    map_list = csv.data_frame['board'].values.tolist();
    problem = Problem(".......;.a-c-C.;...|.|.;.+-^-B.;.|.|.|.;.b.A-+.;.......;")
    problem = Problem(map_list[0]);
    node = breadth_first(problem);

    road = [];
    node1 = Node(problem, problem.initial, None, 0, road);

    node2 = Node(problem, node1.state, "u", node1.path_cost + 1, node1.road)

    node3 = Node(problem, node2.state, "r", node2.path_cost + 1, node2.road)

    print(node3.road);

if __name__ == '__main__':
    main()






