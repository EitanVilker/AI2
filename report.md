<h1>

    CS76
    21F
    PA2
    Eitan Vilker

</h1>

## Description
For my A* search algorithm, I was able to keep it completely agnostic of the problems it was intended to solve. 
I did so through use of a priority queue drawing from the official design in the Python documentation. 
It only has five functions: an init function, a length function, a push function, a pop function, and a remove item function.
The priority queue is sorted by the cost of each state, as determined by the total of the current shortest path cost and the heuristic of the state. "Marking" the states by cost allows states to be replaced in the queue when a better cost is reached.
The actual A* algorithm begins by checking for the base case, terminating the problem and returning the solution if the goal condition specified in the problem is met. Next, I collect the successors of the current node, based on the legal actions as written in the problem script. Finally, I add the successor to the priority queue if it's new or has a better cost.

For the Mazeworld problem, I set it up such that individual states are represented by the robot whose turn it is to move and the location of the robot. The goal state does not contain any robot turn, however, as it doesn't matter which robot reaches its final position first. I implemented a simple Manhattan heuristic here, summing of the minimum number of possible moves to get to the goal, ignoring any obstacles or other robots in the way. I also implemented a Euclidean heuristic, simply taking the absolute distance from each robot to the goal.

For the Sensorless problem, I represented states as sets of tuples, where each tuple contains a possible location of the robot. These sets are sorted before they are put into visited_cost dictionary, as otherwise identical sets might have different dictionary entries. The goal state location is arbitrary, and only included for use with the Manhattan heuristic; mostly the goal state just checks to see if a single space for the robot has been isolated. The Manhattan heuristic here is set up to take the average of all possible locations to the arbitrary goal point. I also implemented a simple length checking state, which returns the number of current possible robot locations.

## Evaluation

#### Mazeworld Problem
My program finished almost instantaneously with all heuristics up to a 9x9 maze for three robots. It also went up to 40x40 with one robot, and did complete after 15 seconds or so with 2 robots. With 3 robots on that maze, the algorithm looked at over 16 million different states until I gave up and terminated the program.

I tested eauch heuristic on maze 3, which was 6x5. The null heuristic performed the worst, as expected, visiting 3,230 nodes before finding the best path. Next was Euclidean distance, with 574 nodes visited, and finally Manhattan distance performed the best by a narrow margin with exactly 500 nodes visited. This makes a lot of sense, since robots can't move in Euclidean distance using only the compass directions, but Manhattan distance is pretty much designed for compass directions.

Overall, I believe I can conclude that my algorithm was able to find the most optimal path each time, since I got consistently the same cost path with every heuristic, including the null one.

#### Sensorless Problem
My program finished quickly with all heuristics up to a 7x7 maze. The null heuristic again performed the worst, visiting 956 nodes. This time, however, Manhattan was only second best, though a substantial improvement, looking at 652 nodes. This increase paled in comparison to the length heuristic, which looked at just over 11% of the nodes of the null heuristic at 107. This is logical, as the primary goal of this problem is to get down to one state so that the robot's location can be identified, so proximity to the goal can be almost perfectly encapsulated by how many states the robot could still be in.

My algorithm seems to work excellently for this problem for the maze sizes we were instructed to use, but it rapidly becomes too inefficient once you go even a few dimensions larger. I believe that this is because the problem essentially starts out with the maximum k, a robot for every floor space. This number goes down, but by the time it converges with the number of robots in the Mazeworld problem, the solution will have almost been reached. Therefore, it should perform substantially worse on same size mazes, but it does work well given these limitations.


## Responses

a) The starting state variable for a maze with k robots would look like this: (0, k0x, k0y, k1x, k1y, ..., (k - 2)x, (k - 2)y, (k - 1)x, (k - 1)y).
There would be a single integer at the start of each state, denoting which robot is slated to move. After that, there would be 2k integers, alternating x and y coordinates for each robot.

b) If n is the height and the width of the maze, and k is the number of robots, we would expect to see n<sup>2</sup> possible states for a single robot. For more than one rbot, the number of states would look like (n<sup>2</sup>)(n<sup>2</sup> - 1)...(2<sup>2</sup>)(1<sup>2</sup>), with terms equal to k, since for every robot added, it cannot go to the same place another robot has been inserted. Looking at the upper bound, however, we can simplify this to O(n<sup>2k</sup>).

c) Walls can be collided with in 0-4 directions, 0 if it is in a corner, 1 if it is along the edge, and 2-4 everywhere else. I'll simplify this to 2 on average in order to get a very rough approximation. This is assuming that a wall square can be anywhere, rather than just on the edge, in which case there would be just k(w - 4) collisions possible. With w different walls, and n much greater than k, there would be a different state for every robot crashing into each wall. For each of these collision states, there are about n<sup>2k</sup> states when considering the rest of the robots, as shown above. Thus, we get a total of 2wn<sup>2k</sup> collision states.

d) A straightforward breadth-first search would likely not be computationally feasible in a maze with large n and a muber of robots.Breadth-first search would be essentially exploring just about every node for not just one robot but for each. Experimentally, we can see this in effect when running a much more efficient A* search on a 40x40 maze with only 3 robots; the number of states just grows exponentially, with 16 million not even being enough to reach a solution. BFS will probably look at most, if not all, of these nodes when searching for a solution, so long as the path isn't very specifically easy, and n<sup>2k</sup> is not a number of states that can be explored in reasonable time.

e) Manhattan distance is a useful, monotonic heuristic for this maze space. This is because in a space without any movement besides the compass directions, Manhattan distance is always the shortest distance to a goal. Thus, the Manhattan distance from a state can never be greater than the Manhattan distance from a neighbor state plus the distance to that state. It costs only 1 unit of fuel to move to a neighbor state, but if that state is closer to the goal, its heuristic is necessarily also exactly 1 closer to the goal, so both sides of the monotonicity equation are equal. If the neighboring state is not closer to the goal, than its heuristic will be larger or equal to the heuristic of the current state, so the heuristic of the current state will be less than or equal to the sum of the heuristic of the neighbor state and the cost to get there.

f) An 8-puzzle is a case of a Mazeworld problem because each of the number tiles can be thought of as a robot, the tiles cannot occupy the same space, the tiles move only in compass directions, and there are distinct borders that are impassable. It is a special case, however, because there is only one empty space, so only a few tiles will be able to move each time, with the rest passing. The maximum number of branches for any move is 3, as discounting the node used to move into the current space, there are at most 3 tiles that can come into it.

g) In order to break the problem into 2 disjoint sets, I would set two goal states, one for each half of the tiles. Then I would carry out an A* search to reach the first goal state, then another to reach the second, and finally a third that combines everything into one state.

h) I used three heuristics in testing the Sensorless robot problem. First, the null heuristic, which was technically optimistic, since it never found a worse path than from a neighbor, but it also never found a better one. Next, I implemented Manhattan distance again, although this time with the tweak that I took the average of all the possible robot locations' Manhattan distances from the arbitrary goal point. This is a bit more difficult to show that it is optimistic, but ultimately it is the same concept as for the Mazeworld problem. The average Manhattan distance to get to a single point is always going to be substantially less than the cost to reach that point, since it assumes only one robot needs to be moved but the robot needs to be localized before it can reach the destination, barring rare cases in which it's exactly equal. Finally, I used a simple length heuristic, which just calculated the total number of positions a robot could be in the given state. This heuristic probably dominates the other two, because it should be very close to the number of moves needed to get to the goal, being exactly equal except when a move doesn't reduce the number of states. Thus, it is also optimistic, being equal to the actual cost or a little bit less. The heuristic will also always be consistent, because it will always output the smallest number of moves to the goal state.

### Screenshots

<img width="960" alt="2021-10-02 (1)" src="https://user-images.githubusercontent.com/38114628/135738801-399d3dae-fcad-458c-9db0-83a1a362e9f6.png">
<img width="960" alt="2021-10-02 (2)" src="https://user-images.githubusercontent.com/38114628/135738810-154cf177-286f-4bab-99d5-51d25cade165.png">
