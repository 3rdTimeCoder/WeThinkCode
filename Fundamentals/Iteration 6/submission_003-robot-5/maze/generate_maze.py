import random


def generate_maze():
    """Generates a random maze, 2D list, Representing the maze grid."""
    
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