import numpy as np

def routeDetection(car_location,direction_array,maze_array):
	sensor_array = carDetection(car_location,direction_array,maze_array)
	if sensor_array == ["CRASH"]:
		return []
	elif sensor_array == [' ',' ',' ',' ','X','X']:
		return [[1,0]]
	elif sensor_array == [' ',' ',' ','X','X',' ']:
		return [[-1,0]]
	elif sensor_array == [' ','X',' ',' ','X','X'] :
		return [[0,1],[1,0]]
	elif sensor_array == [' ','X',' ','X','X',' ']:
		return [[-1,0],[0,1]]
	elif sensor_array == [' ','X',' ','X','X','X']:
		return [[-1,0],[0,1],[1,0]]
	elif sensor_array == [' ',' ',' ','X','X','X']:
		return [[-1,0],[1,0]]
	elif sensor_array == ['X','X','X','X','X','X']:
		return []
	elif sensor_array == [' ',' ',' ',' ',' ',' ']:
		return [[0,-1]]
	else:
		return [[0,1]]

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
	
def carMove(car_location,direction_array,reverse=False):
	X = direction_array[0]
	Y = direction_array[1]
	if reverse == False:	
		return [[car_location[0]-Y,car_location[1]+X],[direction_array]]
	else:
		return [[car_location[0]+Y,car_location[1]-X],[direction_array]]	
 
def carTurn(car_location,direction_array,turn_direction_array):
	current = np.array(direction_array)
	if turn_direction_array == [-1,0]:
		return [car_location, np.dot(np.array([[0,-1],[1,0]]),current).tolist()]
	elif turn_direction_array == [1,0]:
		return [car_location, np.dot(np.array([[0,1],[-1,0]]),current).tolist()]
	elif turn_direction_array == [0,-1]:
		return [car_location, np.dot(np.array([[-1,0],[0,-1]]),current).tolist()]
	elif turn_direction_array == [0,1]:
		return [car_location, [0,1]]
	else:
		return False