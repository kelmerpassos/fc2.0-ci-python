from math import soma
import unittest

class TestMath(unittest.TestCase):

    def test_math(self):
        self.assertEqual(soma(10, 10), 20)
    
    def test_math(self):
        self.assertEqual(soma(20, 10), 10)
    
    

if __name__ == '__main__':
    unittest.main()