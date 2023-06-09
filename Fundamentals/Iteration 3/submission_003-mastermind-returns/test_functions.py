import unittest
from unittest.mock import patch
from io import StringIO
from mastermind import create_code, check_correctness, get_answer_input, take_turn, check_positions


class MyTestCase(unittest.TestCase):

    def test_create_code(self):
        for i in range(100):
            code = create_code()
            # print(code)
            self.assertIsInstance(code, list, f"{code} is not a list.")
            self.assertEqual(len(code), 4)
            for num in code:
                self.assertTrue(num in range(1,9), f"{num} not in range 1-8")
                self.assertTrue(code.count(num) == 1)
                self.assertTrue(type(num) == int)
                
    
    def test_check_correctness(self):
        self.assertTrue(check_correctness(11, 4, test=True)  == True)
        self.assertTrue(check_correctness(5, 3, test=True) == False)
        self.assertTrue(check_correctness(2, 2, test=True)  == False)
        self.assertTrue(check_correctness(8, 1, test=True) == False)
        self.assertTrue(check_correctness(7, 0, test=True) == False)
        
        
    @patch("sys.stdin", StringIO("12345\n34d\abcd\n1230\n2397\n1234\n"))
    def test_get_user_input(self):
        self.assertEqual(get_answer_input(), "1234")
        
        
    @patch("sys.stdin", StringIO("8765\n1247\n6743\n1243\n2143\n1234\n"))
    def test_take_turns(self):
        code = [1,2,3,4]
        
        self.assertEqual((0,0), take_turn(code, test=True))
        self.assertEqual((2,1), take_turn(code, test=True))
        self.assertEqual((0,2), take_turn(code, test=True))
        self.assertEqual((2,2), take_turn(code, test=True))
        self.assertEqual((0,4), take_turn(code, test=True))
        self.assertEqual((4,0), take_turn(code, test=True))
        
    
    def test_check_positions(self):
        answers = ["8765","1347", "5743", "7254", "2745"]
        code = [2,7,4,5]
        
        self.assertEqual((2,0), check_positions(code, answers[0]))
        self.assertEqual((1,1), check_positions(code, answers[1]))
        self.assertEqual((2,1), check_positions(code, answers[2]))
        self.assertEqual((0,4), check_positions(code, answers[3]))
        self.assertEqual((4,0), check_positions(code, answers[4]))
        
                     

if __name__ == "__main__":
    unittest.main()

