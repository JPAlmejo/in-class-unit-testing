import unittest
import calculator

class TestCaseCalculator(unittest.TestCase):

#testing addition (pass)
    def test1(self):
        self.assertEqual(calculator.addition(2, 1), 3)

#testing subtraction (pass)
    def test2(self):
        self.assertEqual(calculator.subtraction(2, 1), 1)

#testing multiplication (pass)
    def test3(self):
        self.assertEqual(calculator.multiplication(2, 1), 2)

#testing division (pass)
    def test4(self):
        self.assertEqual(calculator.division(2, 1), 2)

#==============================================================
#testing addition with floating point (fail)
    def test5(self):
        self.assertEqual(calculator.addition(2.5, 1.5), 4)

#testing subtraction with floating point (fail)
    def test6(self):
        self.assertEqual(calculator.subtraction(2, 0.5), 1.5)

#testing multiplication with floating point (fail)
    def test7(self):
        self.assertEqual(calculator.multiplication(2.5, 2), 5)

#testing division with floating point (pass)
    def test8(self):
        self.assertEqual(calculator.division(2.5, 2), 1.25)




if __name__== '__main__':
    unittest.main(verbosity=2)