import turtle
import world.text.world as textworld


obstacle_size = 4


def setup_turtle():
    """sets up the turtle"""
    
    turtle.goto(0,0)
    turtle.showturtle()
    turtle.title('toy-robot-4')
    turtle.shape('turtle')
    turtle.shapesize(0.5)
    turtle.setheading(90)
    turtle.color('#fff')
    turtle.bgcolor('#101010')
    turtle.speed(2)
    turtle.title('(0,0)')
    turtle.pendown()


def start_screen():
    """_Shows the start screen_"""

    turtle.write('''___________            __________      ___.           __       _____  
\__    ___/___ ___.__. \______   \ ____\_ |__   _____/  |_    /  |  | 
  |    | /  _ <   |  |  |       _//  _ \| __ \ /  _ \   __\  /   |  |_
  |    |(  <_> )___  |  |    |   (  <_> ) \_\ (  <_> )  |   /    ^   /
  |____| \____// ____|  |____|_  /\____/|___  /\____/|__|   \____   | 
               \/              \/           \/                   |__|\n''', font=('Courier',15), align='center')
    turtle.write('\nloading...\n', font=('Courier',15), align='center') 


def clear_screen():
    """_Clears the screen_"""

    turtle.clearscreen()


def display_constraint_box():
    """_Draws a constraint box on the screen_"""  

    turtle.bgcolor('#101010')    
    turtle.penup()
    turtle.pencolor('#fff')
    turtle.pensize(3)
    turtle.hideturtle()
    turtle.goto(110,210)
    turtle.pendown()
    turtle.goto(110,-210)
    turtle.goto(-110,-210)
    turtle.goto(-110,210)
    turtle.goto(110,210)
    # turtle.penup()


def update_degrees(com, deg_ind):
    """Update the degrees, which updates the direction robot is facing."""
    
    if com == 'left':
        turtle.left(90)
    elif com == 'right':
        turtle.right(90)
        
    return textworld.update_degrees(com, deg_ind)


def move_robot(name, com, steps, pos, deg, silent=False):
    """Moves the robot"""

    pos, pos_changed, string = update_position(pos, com, steps, deg)
    if pos_changed and not silent: 
        pass
    elif not pos_changed and not silent: 
        print(f"{name}: {string}")

    return pos


def update_position(pos, dir, steps, deg):
    """Updates the position of the robot.""" 

    pos, pos_changed, string = textworld.update_position(pos, dir, steps, deg)
    
    turtle.goto(pos[0], pos[1])
    turtle.title(f'({pos[0]},{pos[1]})')
 
    return pos, pos_changed, string


def can_move(info):
    """Checks if robot is allwoed to move given steps forward or back"""
    
    textworld.can_move(info)
    
    
def show_obstacles(obstacles):
    """_Displays the obstacles on screen_

    Args:
        obstacles (_list_): _list of obstacles_
    """
    clear_screen()
    display_constraint_box()
    for obstacle in obstacles:
        draw_obstacle(obstacle)
    setup_turtle()


def draw_obstacle(obstacle):
    """_Draws an obstacle on the screen_

    Args:
        obstacle (_list_): _list of obstacles_
    """ 
    
    x,y = obstacle
    turtle.speed(5)
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(x,y)
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(90)
    for _ in range(4):
        turtle.forward(obstacle_size)
        turtle.right(90)
    turtle.penup()