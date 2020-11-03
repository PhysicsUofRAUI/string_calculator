import unittest
import string_calculator

class TestBasicStringCalculator(unittest.TestCase):
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
        

class TestStringCalculatorWithNewlinesAndCommasAsDelimeters(unittest.TestCase):
    def test_empty(self):
        mystr = ''
        
        self.assertEqual(string_calculator.add(mystr), 0)
        
    def test_example_with_newline(self):
        mystr = '1,2,\n5'
        
        self.assertEqual(string_calculator.add(mystr), 8)
        
    def test_newline_in_middle(self):
        mystr = '1,\n2,3'
        
        self.assertEqual(string_calculator.add(mystr), 6)
        
    def test_newline_at_the_start(self):
        mystr = '\n5,2,6'
        
        self.assertEqual(string_calculator.add(mystr), 13)

if __name__ == '__main__':
    unittest.main()
