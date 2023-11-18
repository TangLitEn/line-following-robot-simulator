def initMaze(route,maze_size_square):
	Maze = []
	for row in range(maze_size_square):
		hold = []
		for column in range(maze_size_square):
			hold.append(" ")
		Maze.append(hold)

	for wall_index in route:
		Maze[wall_index[0]][wall_index[1]] = "X"

	return Maze

def printMaze(maze_array,maze_size_square):
	for row in range(0,maze_size_square):
		for column in range(0,maze_size_square):
			print(maze_array[row][column],end="")
		print("\n")