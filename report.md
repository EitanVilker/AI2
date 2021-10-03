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
The actual A* algorithm begins by checking for the base case, terminating the problem and returning the solution if the goal condition specified in the problem is met. Next, I collect the successors of the current node, based on the legal actions as written in the problem script. Finally, I add the successor to the priority queue if it's new or has a better cost.

For the Mazeworld problem, I set it up such that individual states are represented by the robot whose turn it is to move and the location of the robot. The goal state does not contain any robot turn, however, as it doesn't matter which robot reaches its final position first. I implemented a simple Manhattan heuristic here, summing of the minimum number of possible moves to get to the goal, ignoring any obstacles or other robots in the way. I also implemented a Euclidean heuristic, simply taking the absolute distance from each robot to the goal.

For the Sensorless problem, I represented states as sets of tuples, where each tuple contains a possible location of the robot. These sets are sorted before they are put into visited_cost dictionary, as otherwise identical sets might have different dictionary entries. The goal state location is arbitrary, and only included for use with the Manhattan heuristic; mostly the goal state just checks to see if a single space for the robot has been isolated. The Manhattan heuristic here is set up to take the average of all possible locations to the arbitrary goal point. I also implemented a simple length checking state, which returns the number of current possible robot locations.

## Evaluation

#### Mazeworld Problem
My program finished almost instantaneously with all heuristics up to a 9x9 maze for three robots. It also went up to 40x40 with one robot, and did complete after 15 seconds or so with 2 robots. With 3 robots on that maze, the algorithm looked at over 16 million different states until I gave up and terminated the program.
 I tested eauch heuristic on maze 3, which was 6x5. The null heuristic performed the worst, as expected, visiting 3,230 nodes before finding the best path. Next was Euclidean distance, with 574 nodes visited, and finally Manhattan distance performed the best by a narrow margin with exactly 500 nodes visited. This makes a lot of sense, since robots can't move in Euclidean distance using only the compass directions, but Manhattan distance is pretty much designed for compass directions.

#### Sensorless Problem
My program finished quickly with all heuristics up to a 7x7 maze. The null heuristic again performed the worst, visiting 956 nodes. This time, however, Manhattan was only second best, though a substantial improvement, looking at 652 nodes. This increase paled in comparison to the length heuristic, which looked at just over 11% of the nodes of the null heuristic at 107. This is logical, as the primary goal of this problem is to get down to one state so that the robot's location can be identified, so proximity to the goal can be almost perfectly encapsulated by how many states the robot could still be in.



## Responses
