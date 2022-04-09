# NQueenProblem

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. 
For example, following is a solution for N Queen problem.
where type(N) = int

# I make a solution with 3 different AI algorithms

## Hill-climbing
Hill -climbing is a general method that takes three objects as input: a configuration, a function which for each configuration gives a set of 
neighboring configurations, and an objective function which makes it possible to evaluate each configuration. The method simply consists of 
starting from the initial configuration, evaluating the neighboring solutions, and choosing the best of these, and repeating the operation 
until arriving at a position better than the neighboring positions. It is then a local optimum.

## Local beam search
Beam search uses breadth-first search to build its search tree. At each level of the tree, it generates all successors of the states at the 
current level, sorting them in increasing order of heuristic cost. 
However, it only stores a predetermined number,  of best states at each level (called the beam width). 
Only those states are expanded next. The greater the beam width, the fewer states are pruned. 
With an infinite beam width, no states are pruned and beam search is identical to breadth-first search. 
The beam width bounds the memory required to perform the search. 
Since a goal state could potentially be pruned, beam search sacrifices completeness (the guarantee that an algorithm will terminate with a solution, if one exists). 
Beam search is not optimal (that is, there is no guarantee that it will find the best solution).

## Genetic algorithm
In computer science and operations research, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the 
larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems 
by relying on biologically inspired operators such as mutation, crossover and selection. 
Some examples of GA applications include optimizing decision trees for better performance, solving sudoku puzzles, hyperparameter optimization, etc.

### ENJOY!
