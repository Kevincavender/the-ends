import re
from Eqn_solver.myEquations import EquationsClass


class EquationErrorCheck():
    def __init__(self, equation, line_number):
        self.equation = equation
        self.line_number = line_number
        self.variable_dict = EquationsClass(equation).variable_dictionary
        # error message that will be displayed line by line
        # includes active messages
        self.errormessage = ''
        self.leftequation=''
        self.rightequation=''

    def checkline(self):
        '''
        1. check for correct number of equals
        2. check for trailing symbols
        3. check for symbols not allowed
        :return:
        '''
        print(self.variable_dict)
        error_msg = ""

        # check for correct number of equals
        correct_num_equals = self.check_for_equals()
        if correct_num_equals is False:
            error_msg = "Error the equation must contain only one '='"
        elif correct_num_equals is True:
            self.split_equation()
        else:
            error_msg = "something went horribly wrong"

        # check for trailing symbols

        # return error message
        return error_msg

    def check_for_equals(self):
        # need to find all = in line
        # only passes if there's one and only one
        answer = re.findall(r"[=]", self.equation)
        if len(answer) is 1:
            correct_equals = True
        else:
            correct_equals = False
        return correct_equals

    def split_equation(self):
        # split equation by = first
        self.leftequation, self.rightequation = re.split(r"[=]", self.equation)

    def check_trailing_operators(self):
        # r"[=+\-^*/\\()\[\]]"
        trailing_operators_pass = False
        for string in [self.leftequation, self.rightequation]:
            lineend = re.search(r"\+$|-$|\*$|\^$|\($|/$", self.equation)
            end = lineend.group()
            linestart = re.search(r"^\+|^-|^\*|^\^|^\)|^/", self.equation)
            start = linestart.group()
        return trailing_operators_pass
    # https://stackoverflow.com/questions/406230/regular-expression-to-match-a-line-that-doesnt-contain-a-word

    def debug(self):
        pass

if __name__ == '__main__':
    EQ = EquationErrorCheck("-x=4", 3)
    print(">>>Checkline results:")
    print(EQ.checkline())
    # EQ.check_trailing_operators()
    print(">>> Does the equation have the correct number of equals?")
    print(EQ.check_for_equals())
    print(">>> Does the equation have any trailing operators?")
    print(EQ.check_trailing_operators())