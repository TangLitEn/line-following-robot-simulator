import numpy as np

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

def directionEncoding(current_direction,turn_direction_array):
	if current_direction == [-1,0]:
		return np.dot(np.array([[0,-1],[1,0]]),turn_direction_array).tolist()
	elif current_direction == [1,0]:
		return np.dot(np.array([[0,1],[-1,0]]),turn_direction_array).tolist()
	elif current_direction == [0,-1]:
		return np.dot(np.array([[-1,0],[0,-1]]),turn_direction_array).tolist()
	elif current_direction == [0,1]:
		return turn_direction_array # no encoding
	
def directionDecoding(current_direction,encoded_direction_array):
	if current_direction == [1,0]:
		return np.dot(np.array([[0,-1],[1,0]]),encoded_direction_array).tolist()
	elif current_direction == [-1,0]:
		return np.dot(np.array([[0,1],[-1,0]]),encoded_direction_array).tolist()
	elif current_direction == [0,-1]:
		return np.dot(np.array([[-1,0],[0,-1]]),encoded_direction_array).tolist()
	elif current_direction == [0,1]:
		return encoded_direction_array # no decoding

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

# print(directionEncoding([1,0],[-1,0]))
# print(directionEncoding([-1,0],[-1,0]))
# print(directionEncoding([0,1],[1,0]))
# print(directionEncoding([0,-1],[1,0]))
# print("=======")
# print(directionDecoding([1,0],[0,1]))
# print(directionDecoding([-1,0],[-1,0]))
# print(directionDecoding([0,1],[1,0]))
# print(directionDecoding([0,-1],[1,0]))