def carDetection(car_location,direction_array,maze_array):
	try:
		X = direction_array[0]
		Y = direction_array[1]

		result = [
			maze_array[car_location[0]-Y-X][car_location[1]-Y+X],
			maze_array[car_location[0]-Y][car_location[1]+X],
			maze_array[car_location[0]-Y+X][car_location[1]+Y+X],
			maze_array[car_location[0]-X][car_location[1]-Y],
			maze_array[car_location[0]][car_location[1]],
			maze_array[car_location[0]+X][car_location[1]+Y]
			]
		return result
	except:
		return ["CRASH"]
	
def carForward(car_location,direction_array):
	X = direction_array[0]
	Y = direction_array[1]	
	return [car_location[0]-Y,car_location[1]+X]
	
 