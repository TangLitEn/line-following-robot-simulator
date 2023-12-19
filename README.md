
# Line Maze Robot Solver

## Description
This project is a Python-based maze navigation system. It simulates a robot car navigating through different mazes using algorithms to detect routes, move, and make decisions at junctions. The code includes functionalities for initializing mazes, detecting viable paths, and handling the movement of a robotic car within the maze environment.

## Features
- **Maze Initialization**: Create maze structures with custom sizes and wall placements.
- **Route Detection**: Algorithm to detect available paths based on the car's current location and direction.
- **Car Movement**: Functions to move the car forward, reverse, and turn based on the detected routes.
- **Direction Encoding and Decoding**: Transformations for direction changes.
- **Multiple Maze Configurations**: Pre-defined maze routes for different navigation challenges.

## Installation
No specific installation is required other than having Python and NumPy installed on your system. Ensure you have the latest version of Python, and you can install NumPy using the following command:
```
pip install numpy
```

## Usage
To use this system:
1. Import the required modules in your Python script.
2. Initialize the maze using `initMaze` function with your desired maze route and size.
3. Set the starting position and direction for the robotic car.
4. Use the `carMove`, `carTurn`, and `routeDetection` functions to navigate through the maze.

Example:
```python
import numpy as np
from maze import initMaze, outputMazeString
from robot import carMove, carTurn, routeDetection

# Initialize maze
maze_array = initMaze(route_maze_1, 22)

# Set starting position and direction
starting_square = [19,2]
starting_direction = [0,1]

# Navigate through the maze
# ... (navigation logic)
```

## Custom Maze Configuration
For users interested in navigating their own custom mazes, the system allows easy integration of new maze designs. Follow these steps to input your maze:

1. **Create Your Maze**: Define the maze layout in the `maze.py` file. Represent the maze as a list of coordinates where walls ('X') are located.
2. **Integrate the Maze**: Rename your maze array to follow the naming convention `route_maze_x` (where `x` is a unique identifier for your maze).
3. **Configure the Maze**: In your main script, replace the `maze_list_array` variable with your new maze. Also, modify the `maze_size_square` to fit the size of your custom maze, and adjust the `starting_square` and `starting_direction` of the robot as needed.
4. **Setting the Starting Direction**: The starting direction is crucial and is defined as follows:
   - Pointing Up: `[0, 1]`
   - Pointing Down: `[0, -1]`
   - Pointing Left: `[-1, 0]`
   - Pointing Right: `[1, 0]`

Set the `starting_direction` variable to one of these values to indicate the initial orientation of the robot.

## Interface Explanation

### Step Counter
The `STEP` represents the number of movements or actions taken by the robot car since the start of the navigation process. Each step can be a move or a turn.

### Sensor Detection
The `SENSOR DETECTION` array represents what the robot car is currently detecting in its immediate surroundings. It's an array that corresponds to the sensors labeled `[A, B, C, L, O, R]`:
- `A`, `B`, `C` represent the three sensors in front of the robot detecting obstacles or paths.
- `L` and `R` are the left and right side sensors, respectively.
- `O` represents the current position of the robot.

The values in the array will be 'X' if an obstacle is detected in that direction or ' ' (space) if the path is clear.

### Current Available Route
The `CURRENT AVAILABLE ROUTE` shows the possible directions the robot can move towards from its current position, based on the robot's viewing direction. The directions are encoded relative to the robot's current orientation:
- `[0, 1]` means straight ahead.
- `[0, -1]` means directly behind.
- `[-1, 0]` means to the left.
- `[1, 0]` means to the right.

These options are derived from the sensor readings and help decide the next move in the navigation algorithm.

### Visualization
Below is an example of the robot's view at step 24, with the sensor detections and available routes:

![Line Maze Robot Solver View at Step 24](https://github.com/TangLitEn/line-maze-robot-solver-simulator/assets/65808174/105131b2-9a06-4c2d-9aa3-0097ca5db927)

## Implemented Algorithms
The Line Maze Robot Solver incorporates two types of algorithms for navigating through mazes:

1. **Manual Method**: This method allows users to manually navigate the maze. The user can make decisions at each step, choosing which direction to move based on the available routes. This method is interactive and suitable for users who wish to manually explore the maze-solving process.

2. **DFS (Depth-First Search) Method**: This algorithm automatically navigates through the maze using a depth-first search approach. It explores as far as possible along each branch before backtracking, efficiently finding a path through the maze. This method is effective for programmatically solving mazes, showcasing the application of DFS in algorithmic problem-solving.

## Contributing
Contributions to this project are welcome. Please follow the standard fork-branch-pull request workflow. Make sure to update tests as appropriate and adhere to the existing coding style.

## License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Acknowledgments
- Inspiration for this project comes from robotics and maze-solving algorithms.
- Thanks to all contributors who have helped with the development and refinement of this system.
