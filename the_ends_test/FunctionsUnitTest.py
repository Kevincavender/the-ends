import unittest
import sys
sys.path.append('../') #magic folder path helper

from the_ends.functions import function_finder

class TheEndsTestCases(unittest.TestCase):

    def setUp(self):
        #not sure what to do here. Couldn't find a good example of referencing
        pass

    # before test cases

    def tearDown(self):
        pass

    # after test cases

    def equal_index(self):
        equ = 'function1(x, 7, 8+9)*5 + function2(56, 89)'
        self.assertequal(len(function_finder(equ)[0]),len(function_finder(equ)[1]))

    def test_empty_test(self):
        # checks for empty import pass
        equ = ' '
        fun_test = function_finder(equ)
        self.assertFalse(fun_test)

    def test_multiple_single_line(self):
        # checks for multiple functions called in a single line
        ans = [
                ['function1', 'function2'],
                [{1: 'x', 2: ' 5/4', 3: ' 12^(2-1))', 4: ' 8'}, {1: 'y', 2: ' 7', 3: ' 11*(y-3)'}]
            ]
        equ = 'x=2*5+function1(( x=x, 5/4, 12^(2-1)), 8) * function2(y, 7, 11*(y-3))'
        fun_test = function_finder(equ)
        self.assertEqual(fun_test, ans)


if __name__ == '__main__':
    unittest.main()
