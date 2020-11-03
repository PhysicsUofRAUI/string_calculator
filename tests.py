import unittest
import string_calculator

class TestStringMethods(unittest.TestCase):
    def test_empty(self):
        mystr = ''
        
        self.assertEqual(string_calculator.add(mystr), 0)
        
    def test_example(self):
        mystr = '1,2,5'
        
        self.assertEqual(string_calculator.add(mystr), 8)
        
    def test_end_with_comma(self):
        mystr = '1,2,'
        
        self.assertEqual(string_calculator.add(mystr), 3)
        
    def test_start_with_comma(self):
        mystr = ',2,6'
        
        self.assertEqual(string_calculator.add(mystr), 8)
        
if __name__ == '__main__':
    unittest.main()
