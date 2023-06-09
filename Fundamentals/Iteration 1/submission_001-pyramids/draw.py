

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shapes = ['pyramid', 'square', 'triangle', 'diamond', 'rectangle', 'parallelogram']
    shape = input("Shape?: ").lower()

    # Keep prompting unitl user enter valid shape
    while shape not in shapes:
        shape = input("Shape?: ").lower()
    
    return shape
    


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")
    
    # Keep prompting unitl user enter valid height
    while height > str(80) or not height.isnumeric():
        height = input("Height?: ")
    
    return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    if not outline:
        stars = 1
        spaces = height - 1
        for i in range(1, height + 1):
            print(" " * spaces + "*" * stars)
            spaces -= 1
            stars += 2
    else:
        print(" " * (height - 1) + "*") #frist row
    
        left_hand_side_space = height - 1
        for i in range(0, height - 2): # height -2 (subtract 1st and last row)
            left_hand_side_space -= 1 
            print(" " * left_hand_side_space + "*" + " " + " " * i * 2 + "*")
            
        print("*" * (height * 2 - 1)) #last row


# TODO: Step 3
def draw_square(height, outline):
    if not outline:
        for i in range(height):
            print("*" * height)
    else:
        for row in range(height):
            if row == 0 or row == height - 1: #first and last row
                print("*" * height)
            else:
                print("*" + " " * (height - 2) + "*")


# TODO: Step 4
def draw_triangle(height, outline):
    if not outline:
        for i in range(1, height + 1):
            print("*" * i)
    else:
        print("*") #frist row
        for i in range(0, height-2): # height -2 (subtract 1st and last row)
            print("*" + " " * i + "*")
        print("*" * height) #last row


def draw_rectangle(height, outline):
    length = int(input("length?: ") )
    
    if not outline:    
        #solid rectangle
        for row in range(height):
            print("*" * length)
    else:
        #outline rectangle
        print("*" * length) #first row
        for row in range(height - 2):
            print("*" + " " * (length - 2) + "*")
        print("*" * length) #last row
        
        
def draw_parallelogram(height, outline):
    space = height
    extra_stars = height -  1
    if not outline:
        for row in range(1, height+1):
            space -= 1
            print(" " * space + "*" * (row + extra_stars))
            extra_stars -= 1
    else:
        for row in range(1, height+1):
            space -= 1
            if row == 1 or row == height: #first or last row
                print(" " * space + "*" * (row + extra_stars))
            else:
                print(" " * space + "*" +  " " * (row + extra_stars - 2) + "*")
            extra_stars -= 1
    

def draw_diamond_outline(height):
    #upper half of diamond
    #initialize spaces and stars, helps me keep track of how many spaces and stars I shouuld be printing in each row
    stars = 1
    spaces = height // 2 
    for i in range(1, height//2 + 2):
        if i == 1: #first row of diamond
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * (stars -2 ) + "*")
            
        #update spaces and stars
        spaces -= 1
        stars += 2

    #lower half of diamond
    stars = height - 2
    spaces = 1
    k = 2 # changes based on whether height is even or odd. fixes a slight bug in my code.
    if height % 2 == 0:
        k = 1
        
    for i in range(height, 1, -2):
        #last row, when the for loop reaches the last row differs for odd and even height because step == 2
        if i == 3 and height % 2 != 0: 
            print(" " * spaces + "*")
        elif i == 2 and height % 2 == 0:
            print(" " * spaces + "*")
        else: #other rows
            print(" " * spaces + "*" + " " * (stars - k) + "*")
            
        #update spaces and stars
        spaces += 1
        stars -= 2  
        
def draw_diamond_solid(height):
    stars = 1
    spaces = height // 2  #
    for i in range(1, height//2 + 2):
        print(" " * spaces + "*" * stars)
        spaces -= 1
        stars += 2

    #lower half of diamond
    spaces = 1
    if height % 2 == 0:
        stars = height - 1
    else:
       stars = height - 2
    for i in range(height, 1, -2):
        print(" " * spaces + "*" * stars)
        spaces += 1
        stars -= 2


def draw_diamond(height, outline):
    if outline:
        draw_diamond_outline(height)
    else:
        draw_diamond_solid(height)


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'diamond':
        draw_diamond(height, outline)
    elif shape == 'rectangle':
        draw_rectangle(height, outline)
    elif shape == 'parallelogram':
        draw_parallelogram(height, outline)
    


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (Y/N): ").lower()
    if outline == 'y':
        return True
    elif outline == 'n':
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

