import re
from the_ends.EquationObject import EquationsClass


class EquationErrorCheck:
    '''
    This class if to check for errors in individual equations
    it is intended to interface with the gui
    the error message variable will be used for interactive
    feedback when coding in the equation solver
    
    '''
    def __init__(self, equation, line_number=0):
        self.equation = equation
        self.line_number = line_number
        self.variable_dict = EquationsClass(equation).variable_dictionary
        # error message that will be displayed line by line
        # includes active messages
        self.errormessage = ''
        self.leftequation = ''
        self.rightequation = ''
        self.contains_errors = True
        self.checkline()

    def checkline(self):
        """
        1. check for correct number of equals
        2. check for trailing symbols
        3. check for symbols not allowed
        :return:
        """
        # assumed to contain errors until proven false
        contains_errors = True
        while contains_errors is True:

            # returns true if there is only one equals sign
            check_equals = self.check_for_equals()
            if check_equals is False:
                # check for correct number of equals
                self.errormessage = "This equation must contain only one = "
                break
            # splits the equation into a left and right side
            # Split equation on the equals using
            # self.leftequation
            # self.rightequation
            elif check_equals is True:

                self.split_equation()

            # uses left and right equations
            # checks if there is a trailing opereator in both
            # returns True if there are no errors
            # returns False if an error is found
            check_trailing = self.check_trailing_operators()
            if check_trailing is False:
                break

            # checks for common symbols not allowed by the program
            check_symbols = self.check_symbols()
            if check_symbols is False:
                break

            # if no errors are found it will make it to here
            self.errormessage = "no errors"
            contains_errors = False

        # sets the contains errors variable for the class
        self.contains_errors = contains_errors
        return self.errormessage

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
        """
        Checks front and back of each subequation(left and right of equals)
        for extraneous operators
        :return:
        """
        # r"[=+\-^*/\\()\[\]]"
        # does this pass the check?
        trailing_operators_pass = True
        for eqstring in [self.leftequation, self.rightequation]:
            lineend = re.search(r"\+$|-$|\*$|\^$|\($|/$", eqstring)
            linestart = re.search(r"^\+|^-|^\*|^\^|^\)|^/", eqstring)
            if lineend:
                end = lineend.group(0)
                self.errormessage = \
                    "There is a trailing " + str(end) + \
                    " in this equation"
            elif linestart:
                start = linestart.group(0)
                self.errormessage = \
                    "There is a trailing " + str(start) + \
                    " in this equation"
            # print(bool(linestart))
            # print(bool(lineend))
            if bool(linestart) or bool(lineend):
                trailing_operators_pass = False
        return trailing_operators_pass

    def check_symbols(self):
        symbols_not_allowed = ['?', '@', '&', '`', '~', '#', '!', '$', '%']
        for i in self.equation:
            if i in symbols_not_allowed:
                self.errormessage = str(i) + " is not an allowed symbol"
                return False

        return True

    def debug(self):
        pass


if __name__ == '__main__':
    EQ = EquationErrorCheck("x=4+4+a")
    print(EQ.variable_dict)
    print("\n>>>Checkline results:")
    print(EQ.checkline())
    print("\n>>>Contains Errors? \n", EQ.contains_errors)
    # EQ.check_trailing_operators()
    # print(">>> Does the equation have the correct number of equals?")
    # print(EQ.check_for_equals())
    # print(">>> Does the equation have no trailing operators?")
    # print(EQ.check_trailing_operators())
    # print(EQ.errormessage)
