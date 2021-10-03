# Author: Eitan Vilker

from SearchSolution import SearchSolution
from priority_queue import PriorityQueue
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        return self.transition_cost + self.heuristic

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = PriorityQueue()
    pqueue.push(start_node, priority=start_node.priority())

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0

    # you write the rest:

    actions = search_problem.actions
    while len(pqueue) > 0:

        if len(visited_cost) % 10000 == 0:
            print("Current nodes visited: " + str(len(visited_cost)))

        current_node = pqueue.pop()

        # Base case - Goal reached
        if search_problem.is_goal_reached(current_node):
            solution.nodes_visited = len(visited_cost)
            solution.path = backchain(current_node)
            solution.cost = current_node.transition_cost
            return solution

        successors = search_problem.get_successors(current_node.state)
        next_node_cost = current_node.transition_cost

        # For each possible next state
        for successor in successors:
            # Give cost of 0 if no movement, 1 otherwise
            if successor == current_node.state:
                next_node_cost = current_node.transition_cost
            else:
                next_node_cost = current_node.transition_cost + 1

            move_heuristic = heuristic_fn(successor)
            
            # Check if node has not been looked at or has a better cost
            next_node = AstarNode(successor, move_heuristic, transition_cost=next_node_cost, parent=current_node)
            if successor not in visited_cost or next_node.transition_cost < visited_cost[successor]:
                # Package node and push to priority queue
                next_node.parent = current_node
                visited_cost[successor] = next_node_cost
                pqueue.push(next_node, priority=next_node.priority())