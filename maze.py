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

def printMaze(Maze_Array,maze_size_square,car_location_array,car_direction_array):
	car_location = car_location_array

	#layering maze array
	X = car_direction_array[0]
	Y = car_direction_array[1]

	layered_maze_array = Maze_Array

	layered_maze_array[car_location[0]-Y-X][car_location[1]-Y+X] = "A"
	layered_maze_array[car_location[0]-Y][car_location[1]+X] = "B"
	layered_maze_array[car_location[0]-Y+X][car_location[1]+Y+X] = "C"
	layered_maze_array[car_location[0]-X][car_location[1]-Y] = "L"
	layered_maze_array[car_location[0]][car_location[1]] = "O"
	layered_maze_array[car_location[0]+X][car_location[1]+Y] = "R"

	for row in range(0,maze_size_square):
		for column in range(0,maze_size_square):
			print(layered_maze_array[row][column],end="")
		print("\n")