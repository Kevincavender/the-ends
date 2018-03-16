class EquationsClass(object):
    """docstring
    Inputs
    -----------------------------
        eqn_input: text file as a string input into
                   solver for initial processing

    Availible outputs:
    -----------------------------
        self.equation_dict = {"equation":[LeftSide, RightSide]
        self.format
        self.variables
        self.solve
        self.check
        self.parse_eqns_from_string
        self.debug
    """

    def __init__(self, eqn_input):
        """Constructor"""

        if isinstance(eqn_input, str):
            self.equations = self.parse_eqns_from_string(instring=eqn_input)
            self.entered_equations = self.equations
            self.equations = self.format(self.equations)
        elif isinstance(eqn_input, list):
            self.entered_equations = eqn_input
            self.equations = eqn_input
            self.equations = self.format(self.equations)
        else:
            print(str(eqn_input) + "\n has generated an error going into the EquationsClass")
        self.variable_dictionary = self.variable_dict()

    def solve(self):
        from Eqn_solver.Solver import Solver
        solver_object = Solver(self.equations)

        return

    def check(self):
        """
        :return:
            boolean for passing syntax check

        """
        solve = True  # indication for no errors in preprocessing
        containsoperator = False
        count = 0
        tmp_eqn = []
        output_equations = []
        symbols_not_allowed = ['?', '@', '&', '`', '~', '#', '!', '$', '%']

        for text in self.equations:
            # string containing an equation
            # checks every equation line
            count += 1
            containsoperator = False
            for i in text:
                # checks for individual characters in the equations
                # from symbols_not_allowed variable list
                if i in symbols_not_allowed:
                    print("Error in equation " + str(count)
                          + ": \"" + i + "\" is not an allowed character")
                    solve = False
                    # join the characters back into one equation
                elif i == '=':
                    # determines if equals sign is present in every line
                    containsoperator = True
        output_equations.append(tmp_eqn)
        if not containsoperator:
            print("There is a missing '=' sign or a lone variable in the equations list")
            solve = False
        return solve

    # this don't work

    # def check(self):
    #     solve = True
    #     for equation in self.equations:
    #         has_errors = EquationErrorCheck.EquationErrorCheck(equation).contains_errors()
    #         if has_errors is True:
    #             solve = False
    #     return solve

    def parse_eqns_from_string(self, instring):
        stringequations = instring
        equations = stringequations.split("\n")
        equations2 = list(filter(None, equations))
        return equations2

    def format(self, equations):
        """
        the purpose of this function is to take the list of equations,
        - remove spaces 
        - uppercase all characters
        - change certain characters for processing
            ^ -> **
            
        example input
        ['x = y+ 1', 'y = 2^2', 'squ = 2', 'yo = 20']
        example output
        ['X=Y+1', 'Y=2**2', 'SQU=2', 'YO=20']
        *************************
        """
        output_equations = []
        for eqn in equations:
            eqn = eqn.replace(" ","") # remove spaces
            eqn = eqn.replace("^", "**") # for python to understand exponentials
            outeqn = eqn.upper()
            output_equations.append(outeqn)
        return output_equations

    def variables(self, equation=False):
        """
        split equations by the all known operators
        store in list for processing
        :param equation:
        :return:
            list of variables (without copies)
        """
        import re
        variables = []

        if equation is False:
            for one_equation in self.equations:
                # regular expression for splitting strings with given characters
                split_equations = re.split(r"[=+\-^*/\\()\[\]]", one_equation)
                for i in split_equations:
                    if self.isvariable(i) and i not in variables:
                        variables.append(i)
            return variables

        elif isinstance(equation, str):
            split_equations = re.split(r"[=+\-^*/\\()\[\]]", equation)
            for i in split_equations:
                if self.isvariable(i) and i not in variables:
                    variables.append(i)
            return variables

        else:
            raise TypeError

    def variables_in_eqn(self,equation):
        pass

    def variable_dict(self):
        """
        :rtype: dict
        :return:
            list of variables (without copies)
            variable dict = {equation:[variables], ..}
        """
        import re
        variables = []
        variable_dict = {}
        for each_equation in self.equations:
            # regular expression for splitting strings with given characters
            variable_dict[each_equation] = self.variables(each_equation)
        return variable_dict

    def isvariable(self, variable):
        if variable is '':
            return False
        elif variable.isnumeric():
            return False
        elif self.isfloat(variable):
            return False
        return True

    def isfloat(self, i):
        '''
        will determine if a string can be interpreted as a float
        :param i: string
        :return:
        '''
        try:
            float(i)
            return True
        except ValueError:
            return False

    def equation_dict(self):
        # split equations by the equals sign
        import re
        equation_dict = {}
        for i in self.equations:
            split_equations = re.split(r"[=]", i)
            equation_dict[i] = split_equations
        return equation_dict

    def debug(self):
        # print input equations
        output = ["\nEntered Equations: "]
        for i in self.entered_equations:
            output.append(i)

        # formatted equations and numbered
        debug_equations = self.format(self.equations)
        output.append("\nFormatted Equations: ")
        for i, item in enumerate(debug_equations):
            output.append(str(str(i+1) + " " + item))

        # check equations
        solve = self.check()
        # print variables input
        output.append("\nVariables")
        variables = self.variables()
        for i in variables:
            output.append(i)

        # Variable dictionary
        output.append("\nVariable Dictionary")
        for i in self.variable_dictionary:
            output.append(str(i))
            output.append(str(self.variable_dictionary[i]))

        # Equation dictionary
        output.append("\nEquation Dictionary")
        equation_dict = self.equation_dict()
        for i in equation_dict.items():
            output.append(str(i[0]))
            output.append(str(i[1]))

        # join all and print
        output = "\n".join(output)
        if solve:
            return print(output)
        else:
            return print("Error in equation checking")


if __name__ == "__main__":
    import readfile as rf
    input_file = "1eqn"
    eqns = rf.readfile(input_file)
    equations_object = EquationsClass(eqns)
    print("\nReading input file of name: " + input_file)
    equations_object.debug()
    print("\n")