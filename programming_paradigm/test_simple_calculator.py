import unittest
from simple_calculator import SimpleCalculator

class  TstSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-3, 2), -1)
        
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(0, 2), 0)
        self.assertEqual(self.calc.multiply(-3, 0), 0)
                        
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(2, 10), 0.2)
        self.assertEqual(self.calc.divide(0, 5), "Error")
        self.assertEqual(self.calc.divide(5, 0), 0)
    
    if __name__ == "__main__":
        unittest.main()