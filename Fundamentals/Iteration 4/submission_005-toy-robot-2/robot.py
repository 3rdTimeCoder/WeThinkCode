def robot_start():
    """Start the robot"""
    
    deg, deg_ind, pos = (90, 1, [0,0])
    name = get_name()
    
    while True:
        com, steps = get_command(name)
        if com == 'off': print(f"{name}: {return_action(com)}"); break
        else: 
            if com == 'left' or com == 'right': 
                deg_ind, deg = update_degrees(com, deg_ind)
            if com != 'sprint':
                pos = move_robot(name, com, steps, pos, deg)
            else: sprint(name,steps,pos, deg)
            print(f" > {name} now at position ({pos[0]},{pos[1]}).")


def get_name():
    """Gets and returns name of robot from user"""
    
    name = input("What do you want to name your robot? ").upper()
    while not name: get_name(); break
    if name: print(f"{name}: Hello kiddo!"); return name


def get_command(name):
    """Gets command from the user"""
    
    valid_coms = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint']
    com = ''

    while not com or com not in valid_coms: 
        com = input(f"{name}: What must I do next? ").lower()
        if not com: continue
        elif com in valid_coms and ' ' not in com: steps = 0; break
        elif ' ' in com and com.split(' ')[0] in valid_coms and com.split(' ')[1].isnumeric():
            com, steps = com.split(' '); break
        else: 
            print(f"{name}: Sorry, I did not understand '{com.capitalize()}'.")
            continue

    if com == 'help': print(help_menu()); return get_command(name)
    else: return com, int(steps)
    

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
            
            
def update_degrees(com, deg_ind):
    """Update the degrees, which updates the direction robot is facing."""

    DEGREES, first, last = [(0, 90, 180, 270), 0, 3]
    
    if com == 'left' and deg_ind != last: deg_ind += 1
    elif com == 'left' and deg_ind == last: deg_ind = first
    if com == 'right' and deg_ind != first: deg_ind -= 1
    elif com == 'right' and deg_ind == first: deg_ind = last
    
    return deg_ind, DEGREES[deg_ind]


def move_robot(name, com, steps, pos, deg):
    """Moves the robot"""

    pos, pos_changed = update_position(pos, com, steps, deg)
    if pos_changed: print(return_action(com, steps, name))
    else: print(f"{name}: Sorry, I cannot go outside my safe zone.")
    
    return pos

          
def sprint(name, steps, pos, deg):
    """Makes the robot sprint in whatever direction it's facing"""
    if steps == 0: return
    move_robot(name,'forward', steps, pos, deg)
    return sprint(name, steps-1, pos, deg)
    

def update_position(pos, dir, steps, deg):
    """Updates the position of the robot.""" 

    axis = {0: 'x-axis', 90: 'y-axis', 180: 'x-axis', 270: 'y-axis'}
    x, y , pos_changed = (0, 1, True)
    
    if deg == 0 and can_move(pos[x], steps, axis[deg]):
        if dir == 'forward' : pos[x] += steps
        else: pos[x] -= steps
    elif deg == 90 and can_move(pos[y], steps, axis[deg]):
        if dir == 'forward' : pos[y] += steps
        else: pos[y] -= steps
    elif deg == 180 and can_move(pos[x], steps, axis[deg]):
        if dir == 'forward' : pos[x] -= steps
        else: pos[x] += steps
    elif deg == 270 and can_move(pos[y], steps, axis[deg]):
        if dir == 'forward' : pos[y] -= steps
        else: pos[y] += steps
    else: pos_changed = False
 
    return pos, pos_changed


def can_move(pos, steps, axis):
    """Checks if robot is allwoed to move given steps forward or back"""
    if axis == 'y-axis' and (pos + steps > 200 or pos - steps < -200): 
        return False
    elif axis == 'x-axis'and (pos + steps > 100 or pos - steps < -100): 
        return False
    return True


def help_menu():
    """Returns the 'help' menu"""
    return ("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves robot forward. i.e. 'forward 10' moves robot forward by 10 steps.
BACK - moves robot back. i.e. 'back 10' moves robot back by 10 steps.
RIGHT - turns robot to the right by 90 degrees.
LEFT - turns robot to the left by 90 degrees.
SPRINT - sprints robot forward.\n""")

  
if __name__ == "__main__":
    robot_start()