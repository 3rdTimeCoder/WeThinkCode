import random
from .hand_design_maze import maze


global global_obstacles
global_obstacles = []
x_bound, y_bound = 100, 200
obstacle_size = 8


def generate_maze():
    numRows = 50
    numCols = 25
    maze = []
    row = ""

    for i in range(numRows):
        for j in range(numCols):
            if i == 0 and j in [1, 2]:
                row += " "
            elif i == numRows - 1 and j in [numCols - 2, numCols - 3]:
                row += " "
            elif i == 0 or j == 0 or i == numRows - 1 or j == numCols -1:
                row += "x"
            elif i%2 == 0 and  random.random() < 0.6:
                row += "x"
            elif i%5 == 0 and random.random() < 0.5:
                row += "x"
            else:
                row += " "
        maze.append(row)
        row = ""
    return maze


def setup_maze(maze): 
    blocks = []
    for y in range(len(maze)): #y - rows
        for x in range(len(maze[y])): #x - cols
            character = maze[y][x]

            # calculate the screen x,y coords
            screen_x, screen_y = [-99 + (x * obstacle_size), 192 - (y * obstacle_size)]
            # Check if it is an X (representing a wall)
            if character == 'x':
                blocks.append((screen_x, screen_y))
                
    return blocks


    
def get_obstacles(name):
    """_Randomly creates and returns a list of obstacles_

    Returns:
        _list_: _list of obstacles_
    """
    print(f"{name}: Loaded the_worlds_most_crazy_maze.")
    global global_obstacles
    global_obstacles = setup_maze(maze)
    return global_obstacles


def is_position_blocked(x,y):
    """_Checks if the position is blocked and returns a bool_

    Args:
        x (_int_): _x position of robot_
        y (_int_): _y position of robot_

    Returns:
        _Boolean_: _True if position is blocked and false otherwise_
    """
    global global_obstacles
    return any(obstacle[0] <= x <= obstacle[0] + obstacle_size and 
               obstacle[1] <= y <= obstacle[1] + obstacle_size for 
               obstacle in global_obstacles)
            
    
def get_range(x1,y1, x2, y2, deg):
    """Returns the range of where robot is to where it wants to go

    Args:
        x1, y1 (_int_): _The current position of the robot_
        x2, y2 (_int_): _The position the robot wants to go to_
        deg (_int_): _The direction the robot is facing_

    Returns:
        _range_: _The range of robot's position_
    """
    if deg == 0: 
        my_range = range(x1, x2+1)
    elif deg == 180: 
        my_range = range(x1,x2,-1)
    elif deg == 90: 
        my_range = range(y1, y2+1)
    elif deg == 270: 
        my_range = range(y1,y2,-1)
    return my_range
    

def is_path_blocked(x1, y1, x2, y2, deg):
    """Detects whether there is an obstacle obstructing the robot's way.

    Args:
        x1, y1 (_int_): _The current position of the robot_
        x2, y2 (_int_): _The position the robot wants to go to_
        deg (_int_): _The direction the robot is facing_

    Returns:
        _Boolean_: _True if the path is blocked, False if it is not_
    """
    if y1 == y2: # if y is not changing, x is changing
        for x_coord in get_range(x1,y1, x2, y2, deg):
            if is_position_blocked(x_coord, y2):
                return True
    elif x1 == x2:
        for y_coord in get_range(x1,y1, x2, y2, deg):
            if is_position_blocked(x2, y_coord):
                return True
            
    return False                


