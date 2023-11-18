def carDetection(car_location,route_array):
	try:
		result = [
			route_array[car_location[0]-1][car_location[1]-1],
			route_array[car_location[0]-1][car_location[1]],
			route_array[car_location[0]-1][car_location[1]+1],
			route_array[car_location[0]][car_location[1]-1],
			route_array[car_location[0]][car_location[1]],
			route_array[car_location[0]][car_location[1]+1]
			]
		print(result)
		return result
	except:
		print("CRASH")
		return ["X"]
	
