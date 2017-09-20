from Loader import Loader
import pandas as pd
from Problem import Problem
from Node import Node
import queue
import itertools
import copy
import datetime


def breadth_first(problem):
    tie_breaker = itertools.count()
    road = []
    node = Node(problem.initial, None, 0, road)
    frontier = queue.PriorityQueue()
    frontier_hash_map = {}
    touple = (node.path_cost, node.road, next(tie_breaker), node)
    frontier.put(touple)
    frontier_hash_map[node.hashcode] = node

    explored_hash_map = {}

    while True:

        if frontier.empty():
            return False
        touple = frontier.get()
        node = touple[3]
        frontier_hash_map.pop(node.hashcode)

        if Problem.goal_test(node.state):
            print(datetime.datetime.now())
            return node.road

        if node.hashcode in explored_hash_map:
            pass
        else:
            explored_hash_map[node.hashcode] = node

        can_do = problem.check_actions(node.state)
        for action in can_do:
            child = Node(node.state, action, node.path_cost + 1, node.road)
            in_frontier = False
            in_explored = False
            if child.hashcode in explored_hash_map:
                in_explored = True

            if child.hashcode in frontier_hash_map:
                in_frontier = True

            if (in_frontier is False) and (in_explored is False):
                    touple = (child.path_cost, child.road, next(tie_breaker), child)
                    frontier.put(touple)
                    frontier_hash_map[child.hashcode] = child


def a_star(problem):
    tie_breaker = itertools.count()
    road = []
    node = Node(problem.initial, None, 0, road)
    frontier = queue.PriorityQueue()
    frontier_hash_map = {}
    touple = (node.path_cost_A, node.action, node.road, next(tie_breaker), node)
    frontier.put(touple)
    frontier_hash_map[node.hashcode] = node

    explored_hash_map = {}

    while True:

        if frontier.empty():
            return False
        touple = frontier.get()
        node = Node(touple[4].state, None, touple[4].path_cost, touple[4].road)
        frontier_hash_map.pop(node.hashcode)

        if Problem.goal_test(node.state):
            print(datetime.datetime.now())
            return node.road

        if node.hashcode not in explored_hash_map:
            explored_hash_map[node.hashcode] = node

        can_do = problem.check_actions(node.state)
        for action in can_do:
            child = Node(node.state, action, node.path_cost + 1, node.road)

            if (child.hashcode not in explored_hash_map) and (child.hashcode not in frontier_hash_map):
                    touple = (child.path_cost_A, child.action, child.road, next(tie_breaker), child)
                    frontier.put(touple)
                    frontier_hash_map[child.hashcode] = child

            elif child.hashcode in frontier_hash_map:
                auxnode = frontier_hash_map[child.hashcode]
                if auxnode.path_cost_A > child.path_cost_A:
                    auxfrontier = queue.PriorityQueue()
                    for x in range(0, frontier.qsize()):
                        touple = frontier.get()
                        auxnode = touple[4]
                        if child.hashcode == auxnode.hashcode:
                            frontier_hash_map.pop(auxnode.hashcode)
                            frontier_hash_map[child.hashcode] = child
                            touple = (child.path_cost_A, child.action, child.road, next(tie_breaker), child)
                            auxfrontier.put(touple)
                        else:
                            auxfrontier.put(touple)
                    frontier.queue = copy.deepcopy(auxfrontier.queue)
                    auxfrontier.empty()


def main():
    print(datetime.datetime.now())
    file = "C:/Users/Juan/Desktop/AI_Search/lumosity_a_star_search_train.csv"
    csv_read = Loader(file)
    map_list = csv_read.data_frame['board'].values.tolist()
    problem = Problem(".......;.a-c-C.;...|.|.;.+-^-B.;.|.|.|.;.b.A-+.;.......;")
    problem_real = Problem(map_list[12])
    road = a_star(problem_real)
    print(datetime.datetime.now())
    data = []
    id_data = 0;
    for problem in map_list:
        problem_real = Problem(problem)
        road = breadth_first(problem_real)
        road = ''.join(road[1:len(road)])
        tople = [id_data + 1, road]
        data.append(tople)
        break

    df = pd.DataFrame(data, columns=['id', 'breadth_first_search'])
    df.to_csv('C:/Users/eric/Desktop/AI_search stuff/lumosity_breadth_first_search_train_MINE.csv', index=False)
    print(datetime.datetime.now())


if __name__ == '__main__':
    main()
