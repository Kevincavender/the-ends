import unittest
from the_ends.EquationObject import EquationsClass
from the_ends.Solver import Solver
from the_ends.RunAndOutput import solve_and_print_results_only as results


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

    def single_test_frame(self, input_string):
        user_equations = EquationsClass(input_string)
        syntax_check = user_equations.check()
        self.assertEqual(syntax_check, True)
        execute_list, results_list = Solver(user_equations.equations).solve()
        results_out = results(execute_list, results_list)
        return results_out

    def float_output(self, input_string):
        split_list = input_string.split(" ")
        output_float = float(split_list[2])
        return output_float

    def test_single_1(self):
        equation_input = 'x=1'
        equation_output = 'X = 1.0\n'
        result_output = self.single_test_frame(equation_input)
        self.assertEqual(equation_output, result_output)

    def test_single_2(self):
        equation_input = 'x=123456789123456789'
        equation_output = 'X = 1.2345678912345678e+17\n'
        result_output = self.single_test_frame(equation_input)
        self.assertEqual(equation_output, result_output)

    def test_single_3(self):
        equation_input = 'x=1'
        equation_output = 1.0
        result_output = self.single_test_frame(equation_input)
        result_output = self.float_output(result_output)
        self.assertEqual(equation_output, result_output)

    def test_single_4(self):
        equation_input = 'x=1E2'
        equation_output = 100.0
        result_output = self.single_test_frame(equation_input)
        result_output = self.float_output(result_output)
        self.assertEqual(equation_output, result_output)

    def test_single_5(self):
        equation_input = 'x=1+1-3'
        equation_output = -1.0
        result_output = self.single_test_frame(equation_input)
        result_output = self.float_output(result_output)
        self.assertEqual(equation_output, result_output)

    def test_single_6(self):
        equation_input = 'x=2^2'
        equation_output = 4.0
        result_output = self.single_test_frame(equation_input)
        result_output = self.float_output(result_output)
        self.assertEqual(equation_output, result_output)

    def test_single_7(self):
        equation_input = 'x=2**2'
        equation_output = 4.0
        result_output = self.single_test_frame(equation_input)
        result_output = self.float_output(result_output)
        self.assertEqual(equation_output, result_output)

    def test_single_8(self):
        equation_input = '1+1=x'
        equation_output = 2.0
        result_output = self.single_test_frame(equation_input)
        result_output = self.float_output(result_output)
        self.assertEqual(equation_output, result_output)

    def test_single_9(self):
        equation_input = 'x  =  12'
        equation_output = 12.0
        result_output = self.single_test_frame(equation_input)
        result_output = self.float_output(result_output)
        self.assertEqual(equation_output, result_output)

    def test_single_10(self):
        #this ones is expected to raise a syntax error
        equation_input = 'x=?'
        equation_output = 1.0
        with self.assertRaises(SyntaxError):
            result_output = self.single_test_frame(equation_input)
            result_output = self.float_output(result_output)

    def test_single_11(self):
        #this ones is expected to raise a syntax error
        equation_input = 'x=~1'
        equation_output = 1.0
        with self.assertRaises(SyntaxError):
            result_output = self.single_test_frame(equation_input)
            result_output = self.float_output(result_output)

    def test_single_12(self):
        #this ones is expected to raise a syntax error
        equation_input = 'x=<>'
        equation_output = 1.0
        with self.assertRaises(SyntaxError):
            result_output = self.single_test_frame(equation_input)
            result_output = self.float_output(result_output)

    def test_single_13(self):
        #this ones is expected to raise a syntax error
        equation_input = 'x=!!'
        equation_output = 1.0
        with self.assertRaises(SyntaxError):
            result_output = self.single_test_frame(equation_input)
            result_output = self.float_output(result_output)

    def test_single_14(self):
        #this ones is expected to raise a syntax error
        equation_input = 'x=&*'
        with self.assertRaises(SyntaxError):
            result_output = self.single_test_frame(equation_input)

    def test_single_15(self):
        # this ones is expected to raise a syntax error
        equation_input = 'x=1\nx=2'
        with self.assertRaises(SyntaxError):
            result_output = self.single_test_frame(equation_input)



if __name__ == '__main__':
    unittest.main()
