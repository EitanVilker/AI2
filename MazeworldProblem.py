# Author: Eitan Vilker

from Maze import Maze
from time import sleep
from math import sqrt

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal = goal_locations
        self.robot_count = len(goal_locations) // 2
        self.actions = ["Pass", "North", "West", "South", "East"]
        self.start_state = [0]
        for i in range(maze.width):
            for j in range(maze.height):
                if maze.has_robot(i, j):
                    self.start_state.append(i)
                    self.start_state.append(j)
        self.start_state = tuple(self.start_state)


    def __str__(self):
        string =  "Mazeworld problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    # Measures combined Manhattan distance to goal of each robot
    def manhattan_heuristic(self, state):
        total_distance = 0
        for i in range((len(state) - 1) // 2):
            total_distance += abs(state[i * 2 + 1] - self.goal[i * 2])
            total_distance += abs(state[i * 2 + 2] - self.goal[i * 2 + 1])
        return total_distance

    # Measures combined Euclidean distance to goal of each robot
    def euclidean_heuristic(self, state):
        total_distance = 0
        for i in range((len(state) - 1) // 2):
            total_distance += sqrt((state[i * 2 + 1] - self.goal[i * 2])**2 + (state[i * 2 + 2] - self.goal[i * 2 + 1])**2)
        return total_distance



    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))

    # Checks to see if movement is allowed and returns move if legal
    def is_move_legal(self, state, action):
        robot_states = []
        for i in range(self.robot_count):
            robot_states.append([state[1 + 2 * i], state[2 + 2 * i]])
        x = state[state[0] * 2 + 1]
        y = state[state[0] * 2 + 2]
        if action == "North":
            y += 1
        elif action == "South":
            y -= 1
        elif action == "West":
            x -= 1
        elif action == "East":
            x += 1
        if self.maze.is_floor(x, y) and ([x, y] not in robot_states or action == "Pass"):
            new_state = list(state)
            new_state[1 + state[0] * 2] = x
            new_state[2 + state[0] * 2] = y
            new_state[0] = (new_state[0] + 1) % self.robot_count
            return tuple(new_state)
        return None

    def get_successors(self, state):
        # If goal not reached, add legal and optimal next states
        successors = []
        for action in self.actions:
            move = self.is_move_legal(state, action)
            if move is not None:
                successors.append(move)
        return tuple(successors)

    def is_goal_reached(self, current_node):
        if self.goal == current_node.state[1:]:
            return True


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze2 = Maze("maze2.maz")
    test_mp = SensorlessProblem(test_maze2, (3, 0))
    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
