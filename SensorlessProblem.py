# Author: Eitan Vilker

from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:

    def __init__(self, maze, goal_location):
        self.maze = maze
        self.goal = goal_location
        self.actions = ["North", "West", "South", "East"]
        self.start_state = []
        for i in range(maze.width):
            for j in range(maze.height):
                if maze.is_floor(i, j):
                    self.start_state.append((i, j))
        self.start_state = tuple(self.start_state)

    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def is_move_legal(self, mini_state, action):
        x = mini_state[0]
        y = mini_state[1]
        if action == "South":
            if self.maze.is_floor(x, y - 1):
                return (x, y - 1)
            else:
                return (x, y)
        elif action == "North":
            if self.maze.is_floor(x, y + 1):
                return (x, y + 1)
            else:
                return (x, y)        
        elif action == "West":
            if self.maze.is_floor(x - 1, y):
                return (x - 1, y)
            else:
                return (x, y)
        elif action == "East":
            if self.maze.is_floor(x + 1, y):
                return (x + 1, y)
            else:
                return (x, y)        
        
        # print("Eliminated move- x: " + str(x) + ", y: " + str(y) + ", action: " + action)
        # return None

    def get_successors(self, state):
        successors = []
        for action in self.actions:
            small_successor = set()
            for mini_state in state:
                potential_move = self.is_move_legal(mini_state, action)
                small_successor.add(potential_move)
            small_successor = tuple(sorted(small_successor))
            successors.append(small_successor)
        return successors

    def manhattan_heuristic(self, state):

        total_distance = 0
        for mini_state in state:
            total_distance += abs(mini_state[0] - self.goal[0])
            total_distance += abs(mini_state[1] - self.goal[1])

        if len(state) == 0:
            return 0

        return total_distance / len(state)

    def length_heuristic(self, state):
            return len(state)

    def is_goal_reached(self, current_node):
        if len(current_node.state) == 1:
            return True

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = []
            for mini_state in state:
                self.maze.robotloc.append(mini_state[0])
                self.maze.robotloc.append(mini_state[1])
            sleep(1)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze2 = Maze("maze2.maz")
    test_mp = SensorlessProblem(test_maze2, (3, 0))
    print(test_mp.get_successors(((1, 0), (1, 1), (2, 1), (3, 1), (3, 0), (2, 2))))
