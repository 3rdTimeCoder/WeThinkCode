import maze.obstacles as obstacles
import unittest


class MyTestCase(unittest.TestCase):
        
    def test_is_position_blocked_false(self):
        obstacles.global_obstacles = [(1,1), (4,15), (-10,50)]
        self.assertFalse(obstacles.is_position_blocked(7,90))
        self.assertFalse(obstacles.is_position_blocked(-20,-0))
    
    
    def test_is_position_blocked_true(self):
        obstacles.global_obstacles = [(1,1), (4,15), (-10,50)]
        self.assertTrue(obstacles.is_position_blocked(1,1))
        self.assertTrue(obstacles.is_position_blocked(-10,50))
    
    
    def test_get_range(self):
        self.assertEqual(obstacles.get_range(0,0,0,5,90), range(6))
        self.assertEqual(obstacles.get_range(0,0,5,0,0), range(6))
        self.assertEqual(obstacles.get_range(0,0,-5,0,180),  range(0, -5, -1))
    
    
    def test_is_path_blocked_true(self):
        obstacles.global_obstacles = [(1,1), (4,15), (-10,50)]
        self.assertTrue(obstacles.is_path_blocked(5,0,5,17,90))
        self.assertTrue(obstacles.is_path_blocked(5,50,-12,50,180))
    
    
    def test_is_path_blocked_false(self):
        obstacles.global_obstacles = [(1,1), (4,15), (-10,50)]
        self.assertFalse(obstacles.is_path_blocked(5,40,5,40,270))
        self.assertFalse(obstacles.is_path_blocked(5,80,-12,80, 0))
    
    

if __name__ == '__main__':
    unittest.main()
    

