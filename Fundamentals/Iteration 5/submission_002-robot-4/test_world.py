from test_base import captured_io
from io import StringIO
import unittest
from robot import *


class MyTestCase(unittest.TestCase):
        
    def test_update_degress(self):
        # deg_indexes 0 - 0deg, 1 - 90deg, 2 - 180deg, 3 - 270deg
        parameters = [('left', 1), ('right', 2), ('left', 3),('right', 0)]
        expected = [(2, 180), (1, 90), (0, 0), (3, 270)]
        for i, (command, index) in enumerate(parameters):
            self.assertEqual(update_degrees(command, index), expected[i])

    
    def test_move_robot_in_boundary(self):
        with captured_io(StringIO()) as (out, err):
            self.assertEqual(move_robot('HAL', 'forward', 100, [0,0], 180), [-100, 0])
            self.assertEqual(move_robot('HAL', 'forward', 200, [0,0], 90), [0, 200])
            self.assertEqual(move_robot('HAL', 'back', 100, [0,0], 180), [100, 0])
            self.assertEqual(move_robot('HAL', 'back', 200, [0,0], 90), [0, -200])
    

    def test_move_robot_out_boundry(self):
        with captured_io(StringIO()) as (out, err):
            self.assertEqual(move_robot('HAL', 'forward', 101, [0,0], 180), [0, 0])
            self.assertEqual(move_robot('HAL', 'back', 201, [0,0], 90), [0, 0])


    def test_update_position(self):
        position, steps = ([0,0], 10)
        result_1 = update_position(position, 'forward', steps, 90)
        self.assertEqual(result_1, ([0, 10], True, 'Sorry, I cannot go outside my safe zone.'))
        result_2 = update_position(position, 'forward', steps, 180)
        self.assertEqual(result_2, ([-10, 10], True, 'Sorry, I cannot go outside my safe zone.'))
        result_3 = update_position(position, 'back', steps, 0)
        self.assertEqual(result_3, ([-20, 10], True, 'Sorry, I cannot go outside my safe zone.'))
        result_4 = update_position(position, 'back', steps, 270)
        self.assertEqual(result_4, ([-20, 20], True, 'Sorry, I cannot go outside my safe zone.'))


    def test_can_move(self):
        pos = 0
        steps = [100, 200, 101, 201]
        degs = [180, 90, 0, 270]
        dirs = ['forward', 'back', 'forward','back']
        expected = [True, True, False, False]
        for i in range(len(steps)):
            self.assertEqual(can_move(pos, steps[i], degs[i], dirs[i]), expected[i])    
    
          
            
if __name__ == '__main__':
    unittest.main()