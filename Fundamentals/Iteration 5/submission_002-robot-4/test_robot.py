from test_base import captured_io
from io import StringIO
import unittest
from robot import *


class MyTestCase(unittest.TestCase):
    def test_get_name(self):
        with captured_io(StringIO('\nTAL\n')) as (out, err):
            get_name()
        
        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? What do you want to name your robot? TAL: Hello kiddo!""", output)
            
    
    def test_get_command_nothing_then_off(self):
        with captured_io(StringIO('\nofF\n')) as (out, err):
            command = get_command('HAL')
            
        output = out.getvalue().strip()
        expected = ('off', 0)

        self.assertEqual("""HAL: What must I do next? HAL: What must I do next?""", output)
        self.assertEqual(expected, command)

    
    def test_get_command_back10(self):
        with captured_io(StringIO('\nBacK 10\n')) as (out, err):
            command = get_command('HAL')
            
        expected = ('back', 10)
        self.assertEqual(expected, command)


    def test_invalid_commands_then_off(self):
        with captured_io(StringIO('run\nback b\noff\n')) as (out, err):
            get_command('HAL')
            
        output = out.getvalue().strip()
        self.assertEqual("""HAL: What must I do next? HAL: Sorry, I did not understand 'run'.
HAL: What must I do next? HAL: Sorry, I did not understand 'back b'.
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
            self.assertEqual(return_action(command, 10, 'HAL'), actions[i])

        
    def test_update_degress(self):
        # deg_indexes 0 - 0deg, 1 - 90deg, 2 - 180deg, 3 - 270deg
        parameters = [('left', 1), ('right', 2), ('left', 3),('right', 0)]
        expected = [(2, 180), (1, 90), (0, 0), (3, 270)]
        for i, (command, index) in enumerate(parameters):
            self.assertEqual(update_degrees(command, index), expected[i])

    
    def test_move_robot_in_boundary(self):
        with captured_io(StringIO()) as (out, err):
            self.assertEqual(move_robot('HAL', 'forward', 100, [0,0], 180), [-100,0])
            self.assertEqual(move_robot('HAL', 'forward', 200, [0,0], 90), [0,200])
            self.assertEqual(move_robot('HAL', 'back', 100, [0,0], 180), [100,0])
            self.assertEqual(move_robot('HAL', 'back', 200, [0,0], 90), [0,-200])
    

    def test_move_robot_out_boundry(self):
        with captured_io(StringIO()) as (out, err):
            self.assertEqual(move_robot('HAL', 'forward', 101, [0,0], 180), [0,0])
            self.assertEqual(move_robot('HAL', 'back', 201, [0,0], 90), [0, 0])


    def test_update_position(self):
        position, steps = ([0,0], 10)
        result_1 = update_position(position, 'forward', steps, 90)
        self.assertEqual(result_1, ([0, 10], True, "Sorry, I cannot go outside my safe zone."))
        result_2 = update_position(position, 'forward', steps, 180)
        self.assertEqual(result_2, ([-10, 10], True, "Sorry, I cannot go outside my safe zone."))
        result_3 = update_position(position, 'back', steps, 0)
        self.assertEqual(result_3, ([-20, 10], True, "Sorry, I cannot go outside my safe zone."))
        result_4 = update_position(position, 'back', steps, 270)
        self.assertEqual(result_4, ([-20, 20], True, "Sorry, I cannot go outside my safe zone."))
    
    
    def test_help_menu(self):
        menu = help_menu().lower()

        self.assertTrue(
            'help' in menu and 'off' in menu and 
            'forward' in menu and 'back' in menu and 
            'right' in menu and 'left' in menu and 'sprint' in menu
            ) 
        
    
    def test_replay_function_replay(self):
            history = ['forward 10', 'right 0', 'forward 5']
            deg_ind, deg, pos = (1, 90, [0,0])
            self.assertEqual(replay('HAL', 'replay', history, deg_ind, deg, pos),
            (' > HAL replayed 3 commands.\n > HAL now at position (5,10).', 0, 0, [5,10]))
            
            
    def test_replay_function_replay2(self):
        history = ['forward 10', 'right 0', 'forward 5']
        deg_ind, deg, pos = (1, 90, [0,0])
        self.assertEqual(replay('HAL', 'replay 2', history, deg_ind, deg, pos),
        (' > HAL replayed 2 commands.\n > HAL now at position (5,0).', 0, 0, [5,0]))
        
        
    def test_replay_function_reversed(self):
        history = ['forward 10', 'right 0', 'forward 5']
        deg_ind, deg, pos = (1, 90, [0,0])
        self.assertEqual(replay('HAL', 'replay reversed', history, deg_ind, deg, pos),
                (' > HAL replayed 3 commands in reverse.\n > HAL now at position (10,5).', 0, 0, [10,5]))
        

    def test_replay_function_reversed_silent(self):
        history = ['forward 10', 'right 0', 'forward 5']
        deg_ind, deg, pos = (1, 90, [0,0])
        self.assertEqual(replay('HAL', 'replay reversed silent', history, deg_ind, deg, pos),
        (' > HAL replayed 3 commands in reverse silently.\n > HAL now at position (10,5).', 0, 0, [10,5]))


    def test_replay_function_replay3_1(self):
        history = ['forward 10', 'right 0', 'forward 5']
        deg_ind, deg, pos = (1, 90, [0,0])
        self.assertEqual(replay('HAL', 'replay 3-1', history, deg_ind, deg, pos),
        (' > HAL replayed 2 commands.\n > HAL now at position (0,10).', 0, 0, [0,10]))
        
    def test_replay_function_replay_3_1_reversed(self):
        history = ['forward 10', 'right 0', 'forward 5']
        deg_ind, deg, pos = (1, 90, [0,0])
        self.assertEqual(replay('HAL', 'replay 3-1 reversed silent', history, deg_ind, deg, pos),
        (' > HAL replayed 2 commands in reverse silently.\n > HAL now at position (0,5).', 0, 0, [0,5]))
        
        
    def test_replay_function_replay_out_of_range(self):
        history = ['forward 10', 'right 0', 'forward 5']
        deg_ind, deg, pos = (1, 90, [0,0])
        self.assertEqual(replay('HAL', 'replay 5', history, deg_ind, deg, pos),
        (' > HAL replayed 0 commands.\n > HAL now at position (0,0).', 1, 90, [0, 0]))
        
    
    def test_return_flags(self):
        self.assertEqual(return_flags('replay'), (False, False))
        self.assertEqual(return_flags('replay silent'), (True, False))
        self.assertEqual(return_flags('replay reversed'), (False, True))
        self.assertEqual(return_flags('replay reversed silent'), (True, True))
          
            
if __name__ == '__main__':
    unittest.main()