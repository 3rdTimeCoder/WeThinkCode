import queue
from world.turtle.world import obstacle_size
from maze.hand_design_maze import maze as m

#BFSA
# Legend
# S - starting point, E endpoint, v - visted


shortest_path = ""


def visualize_path(maze, starting_point, original_maze, path=""):
    "Displays the maze and path found on terminal"

    j, i = starting_point
    pos = set()

    for move in path:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print(". ", end="")
            else:
                print(original_maze[j][i] + " ", end="")
        print()
        


def valid(maze, moves, starting_point):

    j, i = starting_point

    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return (False, j, i)
        elif (maze[j][i] == "x"):
            return (False, j, i)

    return (True, j, i)


def findEnd(maze, moves, starting_point, original_maze):
    "Find the way out of the maze depending on the edge set chosen."
    global shortest_path
    j, i = starting_point

    for move in moves:
        if move == "L":
            i -= 1
            if maze[j][i] not in ["S", "v", "E"]:
                maze[j][i] = 'v'

        elif move == "R":
            i += 1
            if maze[j][i] not in ["S", "v", "E"]:
                maze[j][i] = 'v'

        elif move == "U":
            j -= 1
            if maze[j][i] not in ["S", "v", "E"]:
                maze[j][i] = 'v'

        elif move == "D":
            j += 1
            if maze[j][i] not in ["S", "v", "E"]:
                maze[j][i] = 'v'

    if maze[j][i] == "E":
        # print("Found: " + moves)
        shortest_path = moves
        visualize_path(maze, starting_point, original_maze, path=moves)
        return True

    return False


def create_maze_list(maze):
    return [list(row) for row in maze]



def find_edge(direction, maze):
    """Given a direction, returns a the index of an edge"""

    if direction == "top":
        for i in range(len(maze[0])):
            if maze[0][i] == " ": 
                return (0,i)
    elif direction == "bottom":
        for i in range(len(maze[0])):
            if maze[-1][i] == " ": 
                return (-1,i)
    elif direction == "left":
        for i in range(len(maze)):
            if maze[i][0] == " ": 
                return (i,0)
    elif direction == "right":
        for i in range(len(maze)):
            if maze[i][-1] == " ": 
                return (i,-1)


def find_center(maze):
    """return center of maze"""
    return len(maze)//2, len(maze[0])//2


def set_starting_point(maze, starting_point):
    """sets the starting point to S on maze list"""
    row, col = starting_point
    maze[row][col] = "S"
    return maze

    
def print_maze(maze):
    """Displays the maze"""
    for row in maze:
        for i in range(len(maze[0])):
            print(row[i], end="")
        print()


def findpath(maze_str, edge_dir="top"):
    """Finds amd returns the shortest path"""

    global shortest_path
    paths = queue.Queue()
    paths.put("")
    current_path = ""
    maze = create_maze_list(maze_str)
    original_maze = create_maze_list(maze_str)

    e_row, e_col = find_edge(edge_dir, maze)
    maze[e_row][e_col] = "E"
    starting_point = find_center(maze)
    maze = set_starting_point(maze, starting_point)

    while not findEnd(maze, current_path, starting_point, original_maze): 
        current_path = paths.get() # get 1st element in queue 

        for j in ["U", "R", "D", "L"]:
            put = current_path + j
            valid_move, row, col = valid(maze, put, starting_point)
            if valid_move and maze[row][col] != 'v':
                paths.put(put)

    return shortest_path


def create_instructions(path, edge_dir):
    print(path)
    path_list = list(path)
    instr = []
    i = 0

    for i, dir in enumerate(path_list):
        if edge_dir == "top":
            if i == 0: instr.append((dir, obstacle_size//2))
            else:instr.append((dir, obstacle_size))
        elif edge_dir == "bottom":
            if i == 0: instr.append((dir, obstacle_size + obstacle_size//2))
            else:instr.append((dir, obstacle_size))
        elif edge_dir == "left":
            if i == 0: instr.append((dir, obstacle_size + obstacle_size//2))
            else:instr.append((dir, obstacle_size))
        elif edge_dir == "right":
            if i == 0: instr.append((dir, obstacle_size + obstacle_size//2))
            else:instr.append((dir, obstacle_size))

    return instr

if __name__ == '__main__':
    p = findpath(m)
    print(p)