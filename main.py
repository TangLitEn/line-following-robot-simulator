from maze import printMaze
from maze import initMaze
from robot import routeDetection 
from robot import carDetection
from robot import carMove
from robot import carTurn
import maze_list
import time as t

maze_size_square = 22
starting_square = [19,2]
starting_direction = [0,1]
maze_list_array = maze_list.route_line_following_2

maze_array = initMaze(maze_list_array,maze_size_square)
step = 0 # terminating step, in case it goes wild
termination_step = 999
current_car_square = starting_square
current_direction = starting_direction

while step<=termination_step: 
	# do the route following first
	maze_array = initMaze(maze_list_array,maze_size_square)	
	available_route = routeDetection(current_car_square,current_direction,maze_array)
	print("==========================================================")
	print("                     STEP: ",step,"                  ")
	printMaze(maze_array,maze_size_square,current_car_square,current_direction)
	print("==========================================================")
	print("SENSOR DETECTION: ", carDetection(current_car_square,current_direction,maze_array))
	print("CURRENT AVAILABLE ROUTE: ",available_route)
	print("CURRENT CAR: ",current_car_square," | CURRENT DIRECTION: ",current_direction)
	print("==========================================================")
	if len(available_route) == 1:
		if available_route[0] == [0,1]:
			current_car_square = carMove(current_car_square,current_direction)[0]
		else:
			# after turning, immediately move forward
			current_direction = carTurn(current_car_square,current_direction,available_route[0])[1]
			current_car_square = carMove(current_car_square,current_direction)[0]
		###
	else:
		step = 1000
	t.sleep(0.2)
	maze_array = initMaze(maze_list_array,maze_size_square)	
	step+=1