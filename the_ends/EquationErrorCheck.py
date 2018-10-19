import re

class EquationErrorCheck:
    """
    This class if to check for errors in individual equations
    it is intended to interface with the gui
    the error message variable will be used for interactive
    feedback when coding in the equation solver

    equation is entered into this class in string format
    """
    equation: str
    line_number: int

    def __init__(self, equation, line_number=0):
        self.equation = equation
        self.line_number = line_number
        self.left_equation = ''
        self.right_equation = ''
        self.contains_errors = True
        self.error_message = 'No Error'
        self.symbols_not_allowed = ['?', '@', '&', '`', '~', '#', '!', '$', '%', '<', '>']

    def checkline(self):
        """
        1. check for correct number of equals
        2. check for trailing symbols
        3. check for symbols not allowed
        :return:
        """
        # returns true if there is only one equals sign
        answer = re.findall(r"[=]", self.equation)
        if len(answer) is not 1:
            self.error_message = 'only 1 equals can be in an equation'
            raise SyntaxError
        elif not self.check_symbols():
            self.error_message = self.error_message
            raise SyntaxError
        elif not self.check_matching_parenthesis(self.equation):
            self.error_message = 'unmatched set of parenthesis'
            raise SyntaxError
        elif not self.check_matching_brackets():
            self.error_message = 'unmatched set of brackets'
            raise SyntaxError
        else:
            self.split_equation()

        if self.left_equation == self.right_equation:
            # self redundant equation
            raise SyntaxError
        elif not self.check_trailing_operators():
            raise SyntaxError

    def split_equation(self):
        # split equation by = first
        self.left_equation, self.right_equation = re.split(r"[=]", self.equation)

    def check_trailing_operators(self):
        """
        Checks front and back of each subequation(left and right of equals)
        for extraneous operators
        :return:
        """
        # r"[=+\-^*/\\()\[\]]"
        # does this pass the check?
        trailing_operators_pass = True
        for eqstring in [self.left_equation, self.right_equation]:
            lineend = re.search(r"\+$|-$|\*$|\^$|\($|/$=$", eqstring)
            linestart = re.search(r"^\+|^-|^\*|^\^|^\)|^/", eqstring)
            if lineend:
                end = lineend.group(0)
                self.error_message = \
                    "There is a trailing " + str(end) + \
                    " in this equation"
            elif linestart:
                start = linestart.group(0)
                self.error_message = \
                    "There is a trailing " + str(start) + \
                    " in this equation"
            # print(bool(linestart))
            # print(bool(lineend))
            if bool(linestart) or bool(lineend):
                trailing_operators_pass = False
        return trailing_operators_pass

    def check_symbols(self):
        for i in self.equation:
            if i in self.symbols_not_allowed:
                self.error_message = str(i) + " is not an allowed symbol"
                return False

        return True

    def check_matching_parenthesis(self, equation_string):
        count = 0
        for i in equation_string:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            if count < 0:
                return False
        return count == 0

    def check_matching_brackets(self):
        left = 0
        right = 0
        for i in self.equation:
            if i is "[":
                left=+1
            if i is "]":
                right=+1
        if left == right:
            return True
        else:
            return False

    def debug(self):
        pass


if __name__ == '__main__':
    EQ = EquationErrorCheck("x=4+4+a", 3)
    try:
        func_list = [EQ.checkline(), EQ.line_number, EQ.equation]
        print("[EQ.checkline(), EQ.line_number, EQ.equation]")
        print(str(func_list))
    except SyntaxError:
        print("Syntax Error Line "+  str(EQ.line_number) +": Debug manually")


    # EQ.check_trailing_operators()
    # print(">>> Does the equation have the correct number of equals?")
    # print(EQ.check_for_equals())
    # print(">>> Does the equation have no trailing operators?")
    # print(EQ.check_trailing_operators())
    # print(EQ.errormessage)
