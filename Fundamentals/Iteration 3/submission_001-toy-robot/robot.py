def move_square(size):
    '''
    Moves a square.
    Args: Size - must be int.
    Returns: None
    '''
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
        

def move_circle(degrees):
    '''
    Moves a circle.
    Args: Degrees - must be int.
    Returns: None
    '''
    print("Moving in a circle")
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        

def move_rectangle(length, width):
    '''
    Moves a rectangle.
    Args: length, width - both must be int.
    Returns: None
    '''
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_square_dancing(length):
    '''
    Moves a multiple squares.
    Args: length - must be int.
    Returns: None
    '''
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(length)
        

def move_crop_cicles(degrees, length):
    '''
    Moves multiple circles.
    Args: degrees, length - must be int.
    Returns: None
    '''
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle(degrees)



# TODO: Decompose into functions
def move():
    '''
    Moves various pre-defined shapes, incl. square, rectangle, circle. etc.
    move_shapes would be a better function name as it tells us exactly what the function does.
    Args: None
    Returns: None
    '''
    s  = 10
    length = 20
    width = 10
    degrees = 1
    
    move_square(s)
    move_rectangle(length, width)
    move_circle(degrees)
    move_square_dancing(length)
    move_crop_cicles(degrees, length)


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
