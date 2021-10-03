<h1>

    CS76
    21F
    PA2
    Eitan Vilker

</h1>

## Description
For my A* search algorithm, I was able to keep it completely agnostic of the problems it was intended to solve. I did so through use of a priority queue drawing from the official design in the Python documentation. It only has five functions: an init function, a length function, a push function, a pop function, and a remove item function.
The actual A* algorithm begins by checking for the base case, terminating the problem and returning the solution if the goal condition specified in the problem is met. Next, I collect the successors of the current node, based on the legal actions as written in the problem script. Finally, I add the successor to the priority queue if it's new or has a better cost.
For the Mazeworld problem, I set it up such that individual states 

## Evaluation


## Responses
