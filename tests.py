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
        
class TestStringCalculatorWithCustomDelimeters(unittest.TestCase):
    def test_with_semi_colon(self):
        mystr = '//;\n1;3;4'
        
        self.assertEqual(string_calculator.add(mystr), 8)
        
    def test_with_dollar_signs(self):
        mystr = '//$\n1$2$3'
        
        self.assertEqual(string_calculator.add(mystr), 6)
        
    def test_with_at_signs(self):
        mystr = '//@\n2@3@8'
        
        self.assertEqual(string_calculator.add(mystr), 13)
        
class TestCustomSplit(unittest.TestCase) :
    def test_semi_colon(self):
        mystr = '//;\n1;3;4'
        
        self.assertEqual(string_calculator.custom_split(mystr), ['1','3','4'])
        
    def test_dollar_signs(self):
        mystr = '//$\n1$2$3'
        
        self.assertEqual(string_calculator.custom_split(mystr), ['1','2','3'])
        
    def test_at_signs(self):
        mystr = '//@\n2@3@8'
        
        self.assertEqual(string_calculator.custom_split(mystr), ['2','3','8'])
        
if __name__ == '__main__':
    unittest.main()
