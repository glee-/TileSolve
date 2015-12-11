# TileSolve
Solves path based tile puzzles using brute force methods.
The goal of the puzzle is to cross over each tile once without backtracking.
An example of the puzzle is included, as bt1.png. This puzzle is defined in the program as the variable 'a'.

#How I made it
I first added functions to determine the possible moves from each location on the board. From there, I created functions that would create a path around the board. Once a path had no more possible moves, I took the path out of the iterative function and stored it within a variable named 'solutions'. The solver continues to work until all paths have been fully completed.

#Useful functions in the program
1. solve: solves the puzzle
2. cleanup: stores finished paths into a global variable
3. printPaths: prints all of the paths
4. selectivePrint: prints paths that are at least a certain length
5. createPath: creates paths based on the possible moves

#Setup
To use the program, clone the project onto your computer. Open a terminal window, and run the program using <code>python solver.py</code>.
