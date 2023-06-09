import re
from world import *


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
        elif com: 
            print(f"{name}: Sorry, I did not understand '{com}'.")
            continue

    if com_copy != 'help': 
        return com_copy, int(steps)
    
    print(help_menu())
    return get_command(name)


def is_valid(com, coms):
    """"Checks the validity of commands with spaces in them"""

    str_digits = re.split(' |-', com)
    string = ' '.join([wrd for wrd in str_digits if wrd.isalpha()])
    digits = [i for i in str_digits if i.isdigit()]
    return bool(string in coms and digits)


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

    if len(digits) == 1:
        limit = range(-1*digits[0], 0)
    elif len(digits) == 2: limit = range(-1*digits[0], -1*digits[1])

    if len(digits) == 1 and digits[0] <= history_len: history_replayable = True
    elif len(digits) == 2 and digits[0] > digits[1]: history_replayable = True
    else: history_replayable = False

    if history and not digits or (history_replayable and digits[0] <= history_len): 
        deg_ind, deg, pos, count = \
        replay_history(name, limit, history, deg_ind, deg, pos, silent)
    elif digits: 
        print(f"{name}: Sorry, either there was an error in your command or there is not enough history to perform your command.")

    return replay_string(name, count, pos, silent, reverse), deg_ind, deg, pos


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
    
    if com in ['left', 'right']: 
        deg_ind, deg = update_degrees(com, deg_ind)
    if com != 'sprint':
        pos = move_robot(name, com, steps, pos, deg, silent)
    else: sprint(name,steps,pos, deg)
    if not silent: print(f" > {name} now at position ({pos[0]},{pos[1]}).")

    return  deg_ind, deg, pos
            
          
def sprint(name, steps, pos, deg):
    """Makes the robot sprint in whatever direction it's facing"""
    
    if steps == 0: return
    move_robot(name,'forward', steps, pos, deg)
    return sprint(name, steps-1, pos, deg)


def help_menu():
    """Returns the 'help' menu"""
    return ("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves robot forward. i.e. 'forward 10' moves robot forward by 10 steps.
BACK - moves robot back. i.e. 'back 10' moves robot back by 10 steps.
RIGHT - turns robot to the right by 90 degrees.
LEFT - turns robot to the left by 90 degrees.
SPRINT - sprints robot forward by given steps.
REPLAY - replays all the movement commands you've typed thus far.
REPLAY SILENT - replays history silently.
REPLAY REVERSED - replays history in reverse.
REPLAY REVERSED SILENT - replays history in reverse silently.\n""")


def robot_start():
    """Start the robot"""
    
    deg, deg_ind, pos = (90, 1, [0,0])
    name = get_name()
    history = []
    global_obstacles = obstacles.get_obstacles()
    show_obstacles(global_obstacles)
    
    while True:
        com, steps = get_command(name)
        if com == 'off': print(f"{name}: {return_action(com)}"); break
        elif 'replay' in com: 
            replay_str, deg_ind, deg, pos = replay(name, com, history, deg_ind, deg, pos)
            print(replay_str)
        else: 
            history.append(f"{com} {steps}")
            deg_ind, deg, pos = do_command(name, com, steps, deg_ind, deg, pos)

  
  
if __name__ == "__main__":
    robot_start()