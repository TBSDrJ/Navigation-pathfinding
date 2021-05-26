
filename = 'maze.txt'
fin = open(filename, 'r')
maze = []
for line in fin:
  maze.append([int(c) for c in line.strip()])
