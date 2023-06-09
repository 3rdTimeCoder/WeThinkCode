import sys


if 'turtle' in sys.argv:
    from world.turtle.world import *
    start_screen()
else:
    from world.text.world import *

if 'the_worlds_most_crazy_maze' in sys.argv:
    import maze.the_worlds_most_crazy_maze as obstacles
    from maze.the_worlds_most_crazy_maze import maze
elif 'random_maze' in sys.argv:
    import maze.random_maze as obstacles
    from maze.random_maze import maze
else: 
    import maze.obstacles as obstacles
