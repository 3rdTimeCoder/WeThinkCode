import sys


if 'turtle' in sys.argv:
    from world.turtle.world import *
    start_screen()
else:
    from world.text.world import *

import world.obstacles as obstacles
