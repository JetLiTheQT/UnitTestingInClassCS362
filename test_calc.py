import unittest
import calculator

class testCaseAdd(unittest.TestCase):
    def test_sum(self):
        #Passing Tests
        self.assertEqual(calculator.sum(10,5), 15)
        #Failing Test
        self.assertEqual(calculator.sum(10,5), 12)
        
        #Failing Tests
    def test_dif(self):
        #Passing Tests
        self.assertEqual(calculator.difference(10,5), 5)        
        #Failing Test
        self.assertEqual(calculator.difference(10,5), 8)
    def test_quotient(self):
        #Passing Tests
        self.assertEqual(calculator.quotient(10,2), 5)
        #Failing Test
        self.assertEqual(calculator.quotient(10,2), 4)
    def test_product(self):
        #Passing Test
        self.assertEqual(calculator.product(2,5), 10)
        #Failing Test
        self.assertEqual(calculator.product(2,5), 3)


if __name__ == '__main__':
    unittest.main()
    