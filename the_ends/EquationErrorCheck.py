import re

class EquationErrorCheck:
    """
    This class if to check for errors in individual equations
    it is intended to interface with the gui
    the error message variable will be used for interactive
    feedback when coding in the equation solver

    equation is entered into this class in string format
    """

    def __init__(self, equation, line_number=0):
        self.equation = equation
        self.line_number = line_number
        self.left_equation = ''
        self.right_equation = ''
        self.contains_errors = True
        self.error_message = 'No Error'
        self.checkline()

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
            raise SyntaxError
        elif not self.check_trailing_operators():
            raise SyntaxError
        elif not self.check_symbols():
            raise SyntaxError
        elif not self.check():
            raise SyntaxError
        else:
            self.split_equation()

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
            lineend = re.search(r"\+$|-$|\*$|\^$|\($|/$", eqstring)
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
        symbols_not_allowed = ['?', '@', '&', '`', '~', '#', '!', '$', '%', '<', '>']
        for i in self.equation:
            if i in symbols_not_allowed:
                self.error_message = str(i) + " is not an allowed symbol"
                return False

        return True

    def check(self, line_number=0):
        """
        :return:
            boolean for passing syntax check
        """
        symbols_not_allowed = ['?', '@', '&', '`', '~', '#', '!', '$', '%']
        # string containing an equation
        # checks every equation line
        contains_operator = False
        for i in self.equation:
            # checks for individual characters in the equations
            # from symbols_not_allowed variable list
            if i in symbols_not_allowed:
                print("Error in equation " + str(line_number)
                      + ": \"" + i + "\" is not an allowed character")
                return False
                # join the characters back into one equation
            elif i == '=':
                # determines if equals sign is present in every line
                contains_operator = True

        if not contains_operator:
            print("There is a missing '=' sign or a lone variable in the equations list")
            return False
        return True

    def debug(self):
        pass


if __name__ == '__main__':
    EQ = EquationErrorCheck("x=4+4+a")
    try:
        EQ.checkline()
    except SyntaxError:
        print("Syntax Error")
    else:
        print("No Errors")
    # EQ.check_trailing_operators()
    # print(">>> Does the equation have the correct number of equals?")
    # print(EQ.check_for_equals())
    # print(">>> Does the equation have no trailing operators?")
    # print(EQ.check_trailing_operators())
    # print(EQ.errormessage)
