from maze import printMaze
from maze import initMaze
from robot import carDetection
from robot import carForward

route = [[0,0],[0,1],[0,2],[0,3],[0,4],
	 [1,1],[2,1],[3,1],[4,1]]
maze_size_square = 5

maze_array = initMaze(route,maze_size_square)
printMaze(maze_array,maze_size_square)

print(carDetection([1,1],[0,1],maze_array))
print(carForward([2,2],[0,1]))
print(carForward([2,2],[0,-1]))
print(carForward([2,2],[1,0]))
print(carForward([2,2],[-1,0]))