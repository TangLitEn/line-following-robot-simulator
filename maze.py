def printCurrentMaze(route,maze_size_square):
	for row in range(1,maze_size_square+1):
		for column in range(1,maze_size_square+1):
			maze_index = column + (maze_size_square * (row - 1))
			#print(maze_index)
			if maze_index in route:
				print(" # ",end="")
			else:
				print("   ",end="")
		print("\n")