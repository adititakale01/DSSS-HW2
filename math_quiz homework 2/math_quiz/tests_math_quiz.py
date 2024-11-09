import unittest
from math_quiz import RandomNumberGenerator, RandomOperator, solveFunction

class TestMathQuiz(unittest.TestCase):
    
    def testRandomNumberGenerator(self):
        result = RandomNumberGenerator(1, 10)
        self.assertTrue(1 <= result <= 10, "Number is outside the specified range")
    
    def testRandomOperator(self):
        operator = RandomOperator()
        self.assertIn(operator, ['+', '-', '*'], "Operator is not valid")
    
    def testSolveFunction(self):
        question, answer = solveFunction(5, 3, '+')
        self.assertEqual(answer, 8, "Addition answer is incorrect")
        
        question, answer = solveFunction(5, 3, '-')
        self.assertEqual(answer, 2, "Subtraction answer is incorrect")
        
        question, answer = solveFunction(5, 3, '*')
        self.assertEqual(answer, 15, "Multiplication answer is incorrect")

if __name__ == '__main__':
    unittest.main()