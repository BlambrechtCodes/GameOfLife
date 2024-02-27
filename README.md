# GameOfLife
An Adaptation of Conway's Game of Life in Python

This Python code implements Conway's Game of Life using the Pygame library for visualization. The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game consists of a grid of cells, each of which can be in one of two states: alive or dead. The cells evolve based on the following rules:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The code initializes a grid of cells, where each cell is represented by a 0 (dead) or 1 (alive). The `update` function calculates the next state of each cell based on the rules and updates the grid accordingly. The main loop of the program handles user input for pausing/resuming the simulation, clearing the grid, toggling cell states with the mouse, and quitting the game. The simulation runs at a fixed time step, updating the display and grid state accordingly.

Overall, the code provides a simple and interactive implementation of Conway's Game of Life using Pygame for visualization.
