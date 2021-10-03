from MazeworldProblem import MazeworldProblem
from Maze import Maze

# from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# test_maze2 = Maze("maze2.maz")
# test_mp = MazeworldProblem(test_maze2, (3, 0))

# print(test_mp.get_successors(test_mp.start_state))


# test_maze4 = Maze("maze4.maz")
# test_mp = MazeworldProblem(test_maze4, (20, 23, 10, 23, 15, 23))
# test_mp = MazeworldProblem(test_maze4, (20, 23))

# test_maze5 = Maze("maze5.maz")
# test_mp = MazeworldProblem(test_maze5, (0, 2, 3, 7, 8, 8))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# # this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# Your additional tests here:
result = astar_search(test_mp, test_mp.euclidean_heuristic)
print(result)