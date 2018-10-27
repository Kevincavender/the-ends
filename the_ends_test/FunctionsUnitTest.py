import unittest
from the_ends.functions import function_finder


class TheEndsTestCases(unittest.TestCase):

    def setUp(self):
        pass

    # before test cases

    def tearDown(self):
        pass

    # after test cases

    def test_isupper(self):
        # example test
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # example test
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_empty_test(self):
        # checks for empty import pass
        equ = ' '
        fun_test = function_finder(equ)
        self.assertFalse(fun_test)

    def test_multiple_single_line(self):
        # checks for multiple functions called in a single line
        ans = [
                ['function1', 'function2'],
                [{1: '( x', 2: 'x', 3: ' 5/4', 4: ' 12^(2-1))', 5: ' 8'}, {1: 'y', 2: ' 7', 3: ' 11*(y-3)'}]
            ]
        equ = 'x=2*5+function1(( x=x, 5/4, 12^(2-1)), 8) * function2(y, 7, 11*(y-3))'
        fun_test = function_finder(equ)
        self.assertEqual(fun_test, ans)


if __name__ == '__main__':
    unittest.main()
