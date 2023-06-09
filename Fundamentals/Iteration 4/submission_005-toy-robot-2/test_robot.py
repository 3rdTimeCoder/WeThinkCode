from test_base import captured_io
from io import StringIO
import unittest
import robot


class MyTestCase(unittest.TestCase):
    def test_get_name(self):
        with captured_io(StringIO('\nTAL\n')) as (out, err):
            robot.get_name()
        
        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? What do you want to name your robot? TAL: Hello kiddo!""", output)
            
    
    def test_get_command_nothing_then_off(self):
        with captured_io(StringIO('\nofF\n')) as (out, err):
            command = robot.get_command('HAL')
            
        output = out.getvalue().strip()
        expected = ('off', 0)

        self.assertEqual("""HAL: What must I do next? HAL: What must I do next?""", output)
        self.assertEqual(expected, command)

    
    def test_get_command_back10(self):
        with captured_io(StringIO('\nBacK 10\n')) as (out, err):
            command = robot.get_command('HAL')
            
        expected = ('back', 10)
        self.assertEqual(expected, command)


    def test_invalid_commands_then_off(self):
        with captured_io(StringIO('run\nback b\noff\n')) as (out, err):
            robot.get_command('HAL')
            
        output = out.getvalue().strip()
        self.assertEqual("""HAL: What must I do next? HAL: Sorry, I did not understand 'Run'.
HAL: What must I do next? HAL: Sorry, I did not understand 'Back b'.
HAL: What must I do next?""", output)


    def test_return_action(self):
        commands = ['off', 'forward', 'back', 'right', 'left', 'sprint']
        actions = ['Shutting down..',
         ' > HAL moved forward by 10 steps.',
         ' > HAL moved back by 10 steps.',
          ' > HAL turned right.',
          ' > HAL turned left.',
          ' > HAL moved forward by 10 steps.',
          ]
        for i, command in enumerate(commands):
            self.assertEqual(robot.return_action(command, 10, 'HAL'), actions[i])

        
    def test_update_degress(self):
        # deg_indexes 0 - 0deg, 1 - 90deg, 2 - 180deg, 3 - 270deg
        parameters = [('left', 1), ('right', 2), ('left', 3),('right', 0)]
        expected = [(2, 180), (1, 90), (0, 0), (3, 270)]
        i = 0
        for command, index in parameters:
            self.assertEqual(robot.update_degrees(command, index), expected[i])
            i += 1

    
    def test_move_robot_in_boundary(self):
        with captured_io(StringIO()) as (out, err):
            self.assertEqual(robot.move_robot('HAL', 'forward', 100, [0,0], 180), [-100, 0])
            self.assertEqual(robot.move_robot('HAL', 'forward', 200, [0,0], 90), [0, 200])
            self.assertEqual(robot.move_robot('HAL', 'back', 100, [0,0], 180), [100, 0])
            self.assertEqual(robot.move_robot('HAL', 'back', 200, [0,0], 90), [0, -200])
    

    def test_move_robot_out_boundry(self):
        with captured_io(StringIO()) as (out, err):
            self.assertEqual(robot.move_robot('HAL', 'forward', 101, [0,0], 180), [0, 0])
            self.assertEqual(robot.move_robot('HAL', 'back', 201, [0,0], 90), [0, 0])


    def test_update_position(self):
        position, steps = ([0,0], 10)
        result_1 = robot.update_position(position, 'forward', steps, 90)
        self.assertEqual(result_1, ([0, 10], True))
        result_2 = robot.update_position(position, 'forward', steps, 180)
        self.assertEqual(result_2, ([-10, 10], True))
        result_3 = robot.update_position(position, 'back', steps, 0)
        self.assertEqual(result_3, ([-20, 10], True))
        result_4 = robot.update_position(position, 'back', steps, 270)
        self.assertEqual(result_4, ([-20, 20], True))


    def test_can_move(self):
        # pos = 0
        pos, axis = [0, ('x-axis', 'y-axis')]
        steps = [100, 200, 101, 201]
        expected = [True, True, False, False]
        for i in range(len(steps)):
            self.assertEqual(robot.can_move(pos, steps[i], axis[i%2]), expected[i], 
                             f"{steps[i]} on the {axis[i%2]} should return {expected[i]}")    
    
    
    def test_help_menu(self):
        menu = robot.help_menu().lower()

        self.assertTrue(
            'help' in menu and 'off' in menu and 
            'forward' in menu and 'back' in menu and 
            'right' in menu and 'left' in menu and 'sprint' in menu
            ) 
            
            
if __name__ == '__main__':
    unittest.main()