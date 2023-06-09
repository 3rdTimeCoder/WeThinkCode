import unittest
from word_processor import convert_to_word_list, words_longer_than, words_lengths_map, letters_count_map, most_used_character


class MyTests(unittest.TestCase):
    def test_word_to_list(self):
        string = 'This is a test string. Testing. Always TESTING;OKAY'
        expected = ['this', 'is', 'a', 'test', 'string', 'testing', 'always', 'testing', 'okay']
        self.assertEqual(convert_to_word_list(string), expected)
        
    
    def test_words_longer_than(self):
        string = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = ['interesting','understatement']
        self.assertEqual(words_longer_than(10, string), expected)
        
    
    def test_word_length_map(self):
        string = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        self.assertEqual(words_lengths_map(string), expected)
        
        
    def test_letters_count_map(self):
        string = 'These are indeed interesting, an obvious understatement, times. What say you?'
        expected = {'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual(letters_count_map(string), expected)
        
    
    def test_most_used_character(self):
        string = 'These are indeed interesting, an obvious understatement, times. What say you?'
        self.assertEqual(most_used_character(string), 'e')
        

if __name__ == '__main__':
    unittest.main()