import unittest
import calculator

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        #Passing Tests
        self.assertEqual(calculator.sum(10,5), 15)
        self.assertEqual(calculator.difference(10,5), 5)
        self.assertEqual(calculator.quotient(10,2), 5)
        self.assertEqual(calculator.product(2,5), 10)
        #Failing Tests
        self.assertEqual(calculator.sum(10,5), 12)
        self.assertEqual(calculator.difference(10,5), 8)
        self.assertEqual(calculator.quotient(10,2), 4)
        self.assertEqual(calculator.product(2,5), 3)


if __name__ == '__main__':
    unittest.main()
    