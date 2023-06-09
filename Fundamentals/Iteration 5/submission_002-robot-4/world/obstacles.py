import random


global global_obstacles
global_obstacles = []
x_bound, y_bound = 100, 200
obstacle_size = 4

    
def get_obstacles():
    """_Randomly creates and returns a list of obstacles_

    Returns:
        _list_: _list of obstacles_
    """
    global global_obstacles
    rand_num = random.randint(1,10)
    global_obstacles = [(random.randint(-1 * x_bound, x_bound), \
             random.randint(-1 * y_bound, y_bound)) for _ in range(rand_num)]
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


# last thing to fix, sprint terminate if it runs into an obstacle or wall and only print th sorry message once.