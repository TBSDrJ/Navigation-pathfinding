# imports pathfinding 1.0.1
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# Read in the maze
filename = 'maze.txt'
fin = open(filename, 'r')
maze = []
for line in fin:
  maze.append([int(c) for c in line.strip()])

# Convert into Grid object, specify start/end
grid = Grid(matrix = maze)
start = grid.node(32, 4)
end = grid.node(3, 1)

finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

print(grid.grid_str(path=path, start=start, end = end))
