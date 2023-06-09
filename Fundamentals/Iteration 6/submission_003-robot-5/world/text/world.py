from maze.the_worlds_most_crazy_maze import *


def update_degrees(com, deg_ind):
    """Update the degrees, which updates the direction robot is facing."""

    DEGREES, first, last = [(0, 90, 180, 270), 0, 3]

    if com == 'left' and deg_ind != last: deg_ind += 1
    elif com == 'left': deg_ind = first
    if com == 'right' and deg_ind != first: deg_ind -= 1
    elif com == 'right': deg_ind = last

    return deg_ind, DEGREES[deg_ind]


def move_robot(name, com, steps, pos, deg, silent=False):
    """Moves the robot"""

    pos, pos_changed, string = update_position(pos, com, steps, deg)
    if pos_changed and not silent: print(return_action(com, steps, name))
    elif not pos_changed and not silent: 
        print(f"{name}: {string}")

    return pos


def return_action(com, steps=0, name=None):
    """Return the action robot will take"""
    
    commands = {'off': 'Shutting down..', 
                'forward': f" > {name} moved forward by {steps} steps.",
                'back': f" > {name} moved back by {steps} steps.",
                'right': f" > {name} turned right.",
                'left': f" > {name} turned left.",
                'sprint': f" > {name} moved forward by {steps} steps.",
                }
    return commands[com]


def update_position(pos, dir, steps, deg):
    """Updates the position of the robot.""" 

    axis = {0: 'x-axis', 90: 'y-axis', 180: 'x-axis', 270: 'y-axis'}
    coord_ind = {0: 0, 90: 1, 180: 0, 270: 1}
    pos_changed = True
    old_pos = pos[:] #clone old position
    
    if deg in [0, 90] and can_move(pos[coord_ind[deg]], steps, deg, dir):
        if dir == 'forward' : pos[coord_ind[deg]] += steps
        else: pos[coord_ind[deg]] -= steps
    elif deg in [180, 270] and can_move(pos[coord_ind[deg]], steps, deg, dir):
        if dir == 'forward' : pos[coord_ind[deg]] -= steps
        else: pos[coord_ind[deg]] += steps
    else: pos_changed = False

    if is_position_blocked(pos[0], pos[1]) or is_path_blocked(old_pos[0], old_pos[1], pos[0], pos[1], deg):
        return old_pos, False, "Sorry, there is an obstacle in the way."
    
    return pos, pos_changed, "Sorry, I cannot go outside my safe zone."


def can_move(pos, steps, deg, dir):
    """Checks if robot is allwoed to move given steps forward or back"""
    
    deg_constraint = {0: 100, 90: 200, 180: 100, 270: 200}
    
    if deg in (0,90):
        if dir == 'forward' and pos + steps > deg_constraint[deg]:
            return False
        elif dir == 'back' and pos - steps < -1*deg_constraint[deg]:
            return False
    elif deg in (180,270):
        if dir == 'forward' and pos - steps < -1*deg_constraint[deg]:
            return False
        elif dir == 'back' and pos + steps > deg_constraint[deg]:
            return False
    return True
        
        
def show_obstacles(obstacles):
    """_Displays the obstacles on the command line_

    Args:
        obstacles (_list_): _lsit of obstacles_
    """
    
    if len(obstacles) > 0:
        print("There are some obstacles:")
    for obstacle in obstacles:
        print(f"- At position {obstacle[0]},{obstacle[1]} (to {obstacle[0]+4},{obstacle[1]+4})")