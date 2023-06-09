import re


def get_name():
    """Gets and returns name of robot from user"""
    
    name = input("What do you want to name your robot? ").upper()
    while not name: get_name(); break
    if name: print(f"{name}: Hello kiddo!")

    return name


def get_command(name):
    """Gets command from the user"""
     
    com = ''
    valid_coms = ['off', 'help', 'right', 'left',
    'replay', 'replay silent','replay reversed', 'replay reversed silent']
    forward_back = ['forward', 'back', 'sprint']

    while not com or com not in valid_coms: 
        com = input(f"{name}: What must I do next? ").strip()
        com_copy = com.lower()
        
        if com_copy in valid_coms: steps = 0; break
        elif 'replay' in com_copy and is_valid(com_copy, valid_coms):
            steps = 0; break
        elif ' ' in com_copy and is_valid(com_copy, forward_back):
            com_copy, steps = com_copy.split(); break
        elif com and com_copy not in valid_coms: 
            print(f"{name}: Sorry, I did not understand '{com}'.")
            continue

    if com_copy == 'help': print(help_menu()); return get_command(name)
    else: return com_copy, int(steps)


def is_valid(com, coms):
    """"Checks the validity of commands with spaces in them"""

    str_digits = re.split(' |-', com)
    string = ' '.join([wrd for wrd in str_digits if wrd.isalpha()])
    digits = [i for i in str_digits if i.isdigit()]
    if string in coms and digits: 
        return True
    return False


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
            

def replay(name, com, history, deg_ind, deg, pos):
    """Replays all the movement commands a user has entered thus far."""
    
    silent, reverse = return_flags(com)
    history_len = len(history)
    limit = range(history_len)
    count = 0

    if reverse: history = history[::-1]
    
    split_com = re.split(' |-', com)
    digits = [int(i) for i in split_com if i.isdigit()] 

    if len(digits) == 1: limit = range(-1*digits[0], 0, 1)
    elif len(digits) == 2: limit = range(-1*digits[0], -1*digits[1])
    
    if len(digits) == 1 and digits[0] <= history_len: history_replayable = True
    elif len(digits) == 2 and digits[0] > digits[1]: history_replayable = True
    else: history_replayable = False
    
    if history and not digits or (history_replayable and digits[0] <= history_len): 
        deg_ind, deg, pos, count = \
        replay_history(name, limit, history, deg_ind, deg, pos, silent)
    elif digits: 
        print(f"{name}: Sorry, either there was an error in your command or there is not enough history to perform your command.")
    
    return replay_string(name, count, pos, silent, reverse)


def return_flags(com):
    """Sets and returns the state of the silent and reverse flags"""
    
    silent, reverse = (False, False)
    if 'silent' in com: silent = True
    if 'reversed' in com: reverse = True

    return silent, reverse


def replay_history(name, limit, history, deg_ind, deg, pos, silent):
    """Replays the history"""
    
    count = 0
    for i in limit:
        count += 1
        com, steps = re.split(' ',history[i])
        deg_ind, deg, pos = \
        do_command(name, com, int(steps), deg_ind, deg, pos, silent)

    return deg_ind, deg, pos, count


def replay_string(name, history_len, pos, silent, reverse):
    """Returns the replay string."""
    
    string = f" > {name} replayed {history_len} commands"
    
    if reverse: string += " in reverse"
    if silent: string += " silently"
            
    string += f".\n > HAL now at position ({pos[0]},{pos[1]})."
    
    return string


def do_command(name, com, steps, deg_ind, deg, pos, silent=False):
    """Handle the functionality of different commands"""
    
    if com == 'left' or com == 'right': 
        deg_ind, deg = update_degrees(com, deg_ind)
    if com != 'sprint':
        pos = move_robot(name, com, steps, pos, deg, silent)
    else: sprint(name,steps,pos, deg)
    if not silent: print(f" > {name} now at position ({pos[0]},{pos[1]}).")
    
    return  deg_ind, deg, pos
            
            
def update_degrees(com, deg_ind):
    """Update the degrees, which updates the direction robot is facing."""

    DEGREES, first, last = [(0, 90, 180, 270), 0, 3]
    
    if com == 'left' and deg_ind != last: deg_ind += 1
    elif com == 'left' and deg_ind == last: deg_ind = first
    if com == 'right' and deg_ind != first: deg_ind -= 1
    elif com == 'right' and deg_ind == first: deg_ind = last
    
    return deg_ind, DEGREES[deg_ind]


def move_robot(name, com, steps, pos, deg, silent=False):
    """Moves the robot"""

    pos, pos_changed = update_position(pos, com, steps, deg)
    if pos_changed and not silent: print(return_action(com, steps, name))
    elif not pos_changed and not silent: 
        print(f"{name}: Sorry, I cannot go outside my safe zone.")

    return pos

          
def sprint(name, steps, pos, deg):
    """Makes the robot sprint in whatever direction it's facing"""
    
    if steps == 0: return
    move_robot(name,'forward', steps, pos, deg)
    return sprint(name, steps-1, pos, deg)
    

def update_position(pos, dir, steps, deg):
    """Updates the position of the robot.""" 

    axis = {0: 'x-axis', 90: 'y-axis', 180: 'x-axis', 270: 'y-axis'}
    coord_ind = {0: 0, 90: 1, 180: 0, 270: 1}
    info = (pos[coord_ind[deg]], steps, axis[deg])
    pos_changed = True

    if deg in [0, 90] and can_move(info):
        if dir == 'forward' : pos[coord_ind[deg]] += steps
        else: pos[coord_ind[deg]] -= steps
    elif deg in [180, 270] and can_move(info):
        if dir == 'forward' : pos[coord_ind[deg]] -= steps
        else: pos[coord_ind[deg]] += steps
    else: pos_changed = False
 
    return pos, pos_changed


def can_move(info):
    """Checks if robot is allwoed to move given steps forward or back"""
    pos, steps, axis = info
    
    if axis == 'y-axis' and (pos + steps > 200 or pos - steps < -200): 
        return False
    elif axis == 'x-axis'and (pos + steps > 100 or pos - steps < -100): 
        return False
    return True


def robot_start():
    """Start the robot"""
    
    deg, deg_ind, pos = (90, 1, [0,0])
    name = get_name()
    history = []
    
    while True:
        com, steps = get_command(name)
        if com == 'off': print(f"{name}: {return_action(com)}"); break
        elif 'replay' in com: 
            print(replay(name, com, history, deg_ind, deg, pos))
        else: 
            history.append(f"{com} {steps}")
            deg_ind, deg, pos = do_command(name, com, steps, deg_ind, deg, pos)

  
if __name__ == "__main__":
    robot_start()