from maze import printMaze
from maze import initMaze
from maze import directionEncoding
from maze import directionDecoding
from robot import routeDetection 
from robot import carDetection
from robot import carMove
from robot import carTurn
import maze_list
import time as t

maze_size_square = 22
starting_square = [19,2]
starting_direction = [0,1]
maze_list_array = maze_list.route_maze_2

maze_array = initMaze(maze_list_array,maze_size_square)
current_car_square = starting_square
current_direction = starting_direction

choices = [1,2]
choice = 999

print("==========================================================")
print("=		  INTIALIZING MAP			=")
printMaze(maze_array,maze_size_square,current_car_square,current_direction)
print("==========================================================")

while choice == 999:
	print("AVAILABLE METHOD:")
	print("1. Manual Method")
	print("2. Depth-First Search")
	choice = int(input("Please choose your method of solving"))
	print("")
	if choice not in choices:
		print("INVALID OPTION")
		choice = 999
	print("==========================================================")

# Manual solving
if choice == 1:
	step = 0
	termination_step = 999
	while step<=termination_step: 
		# do the route following first
		maze_array = initMaze(maze_list_array,maze_size_square)	
		available_route = routeDetection(current_car_square,current_direction,maze_array)
		print("==========================================================")
		print("                     STEP: ",step,"                  ")
		printMaze(maze_array,maze_size_square,current_car_square,current_direction)
		print("==========================================================")
		maze_array = initMaze(maze_list_array,maze_size_square)	
		print("SENSOR DETECTION: ", carDetection(current_car_square,current_direction,maze_array))
		print("CURRENT AVAILABLE ROUTE: ",available_route)
		print("CURRENT CAR: ",current_car_square," | CURRENT DIRECTION: ",current_direction)
		print("==========================================================")
		if len(available_route) == 0:
			print("...........⊂(◉‿◉)つ...............")
			print(".................................")
			print(".....NO MORE AVAILABLE ROUTE.....")
			print(".......YOU MIGHT HAVE WIN........")
			print("..............OR.................")
			print(".......THE SYSTEM CRASHED .......")
			print(".......ʕノ•ᴥ•ʔノ ︵ ┻━┻...........")
			print(".................................")
			print("............☜(⌒▽⌒)☞..............")
			step = 999
		elif len(available_route) == 1:
			if available_route[0] == [0,1]:
				current_car_square = carMove(current_car_square,current_direction)[0]
			else:
				# after turning, immediately move forward
				current_direction = carTurn(current_car_square,current_direction,available_route[0])[1]
				current_car_square = carMove(current_car_square,current_direction)[0]
			###
		else:
			option = 999
			while option == 999:
				print("*******************************************************")
				print("AVAILABLE DIRECTION ARE: ",available_route)
				print("")
				option = int(input("Please select the direction that you wanna head to (0 for the first option, 1 for the second option and so forth)"))
				print("")
				if option >= len(available_route):
					print("INVALID OPTION")
					option = 999
				print("*******************************************************")
			
	# after turning, immediately move forward
			current_direction = carTurn(current_car_square,current_direction,available_route[option])[1]
			current_car_square = carMove(current_car_square,current_direction)[0]	
	
		t.sleep(0.2)
		maze_array = initMaze(maze_list_array,maze_size_square)	
		step+=1

if choice == 2:
	reach_goal_flag = 0
	dead_end_flag = 0
	
	step = 0
	termination_step = 999

	save_route = []

	while reach_goal_flag != 1 and step <= termination_step:

		available_route = routeDetection(current_car_square,current_direction,maze_array)	
		
		if routeDetection(current_car_square,current_direction,maze_array) == [[0,-1]]: # detect dead end 
			dead_end_flag = 1
		
		maze_array = initMaze(maze_list_array,maze_size_square)	
		print("==========================================================")
		print("                     STEP: ",step,"                  ")
		printMaze(maze_array,maze_size_square,current_car_square,current_direction)
		print("==========================================================")
		maze_array = initMaze(maze_list_array,maze_size_square)	
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
		else: # hit a junction
			if dead_end_flag == 0:
				for route in available_route:
					save_route.insert(0,directionEncoding(current_direction,route))
			else:
				dead_end_flag = 0 
		
			go = directionDecoding(current_direction,save_route.pop(0))
			current_direction = carTurn(current_car_square,current_direction,go)[1]
			current_car_square = carMove(current_car_square,current_direction)[0]	

		print("==========================================================")
		maze_array = initMaze(maze_list_array,maze_size_square)	
		print("QUEUE: ",save_route)
		print("==========================================================")

		if routeDetection(current_car_square,current_direction,maze_array) == []:	# detect goal end 
			reach_goal_flag = 1

		t.sleep(1)
		maze_array = initMaze(maze_list_array,maze_size_square)	
		
		step += 1
	print("...........⊂(◉‿◉)つ...............")
	print(".................................")
	print(".....NO MORE AVAILABLE ROUTE.....")
	print(".......YOU MIGHT HAVE WIN........")
	print("..............OR.................")
	print(".......THE SYSTEM CRASHED .......")
	print(".......ʕノ•ᴥ•ʔノ ︵ ┻━┻...........")
	print(".................................")
	print("............☜(⌒▽⌒)☞..............")	
	