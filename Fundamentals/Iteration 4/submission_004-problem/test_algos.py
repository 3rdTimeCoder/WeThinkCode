import unittest
from super_algos import find_min, sum_all, find_possible_strings


class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        result = find_min([15,5,1,10,-5,11,12,-10,20,-15,100])
        self.assertEqual(-15, result)
    
    
    def test_sum_all(self):
        result = sum_all([1,2,3,4,5,-4,-3,-5,-2,-1])
        self.assertEqual(0, result)
    
    
    def test_find_possible_strings(self):
        result = find_possible_strings(['a','b','c','d'], 0)
        self.assertEqual([], result)


if __name__ == '__main__':
    unittest.main()