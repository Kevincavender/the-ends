from EquationErrorCheck import EquationErrorCheck
import re


class EquationCollection_n_solve(object):
    
    """
    This Class is for interacting with metadata of the equations entered as a string

    Example of equations and variables dictionaries

    block_number : used for the solution order of the equations
    error: used for giving specific error results to the user
    variables and equations are cross listed to allow for storing resulting values in one place

    """

    def __init__(self, equation_string=''):
        self.equations_list = self.parse_by_line(equation_string)
        self.equation_string = equation_string
        # each equation dictionary within the self.equations dictionary
        # will get it's own index number
        # (starting at 1 because 0 is being used by the example listed here)
        
        self.number_of_equations = len(equations_list)
        self.number_of_variables = 0
        self.variable_list = []
        self.solved_variable_list = []
        self.solved_equation_list = []

        #solver initializations
        self.looplimit = 50
        self.vdict = self.variable_list
        self.eqn_block = []
        self.solvable_vars = []

        # will populate the previous variables
        self.parse_eqns_from_string(self.equation_string)
        self.update_class()

    def __repr__(self):
        # this needs a detailed printout of what's in the string
        return str(self.equations)

    def check_for_errors(self):
        okay = False
        for i in self.equations_list:
            equ = EquationErrorCheck(self.equations_list[i], i + 1)
            o = equ.checkline()
            k = equ.check_trailing_operators
            a = equ.check_symbols
            y = equ.check_matching_parenthesis
            ok = equ.check_matching_brackets
            if o == True and k == True and a == True and y == True and ok == True:
                okay = True
            else:
                print("Equation " + i + " has issues.\n")
            
        return okay

    def parse_by_line(self, string):
        list_of_lines = string.split("\n")
        return list_of_lines

    def parse_eqns_from_string(self, in_string):
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
        # Current functionality of this code:
        #   takes in a list of strings
        #   enumerates lines
        #   cleans up whitespace
        #   capitalizes all letters
        """
        list_of_lines = self.equations_list
        i = 0
        while i < len(list_of_lines):
            list_of_lines[i] = list_of_lines[i].replace(' ','') #removes spaces
            list_of_lines[i] = list_of_lines[i].replace('\t', '')  # remove tabs, neccesary? is it seen different than space?
            list_of_lines[i] = list_of_lines[i].replace("^", "**")  # for python to understand exponential's
            list_of_lines[i] = list_of_lines[i].upper()  # for upper casing the equations, so python isn't confused

            if list_of_lines[i] == '':
                list_of_lines.remove(list_of_lines[i])  # remove empty lines
            # TODO elif: the string starts with comment symbol (#)
            # TODO elif: the string starts with special character ($)

    def variables(self, equation=False):
        #takes in equation by equation or works as a . function for single equation blocks
        """
        split equations by the all known operators
        store in list for processing
        :param equation:
        :return:
            list of variables (without copies)
        """
        #TODO Reference list against function list from function finder
        
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

    def parse_line(self, line_string, line_number):
        line = EquationErrorCheck(line_string, line_number)
        try:
            line.checkline()
        except SyntaxError:
            print("Syntax Error Detected:\n\tLine error")
        equations = line_string.split("\n")
        equations = equations.replace(' ', '')
        return equations

    """
    def update_solved_variable_list(self):
        for i in self.variables:
            if self.variables[i]['solved'] is True:
                self.solved_variable_list.append(self.variables[i]['variable_name'])
                self.solved_variable_list = list(set(self.solved_variable_list))
    """
    
    def update_solved_equation_list(self):
        for i in self.equations:
            if self.equations[i]['solved'] is True:
                self.solved_equation_list.append(self.equations[i]['equation'])
                self.solved_equation_list = list(set(self.solved_equation_list))

    def update_list_from_dictionary(self, dictionary_name: dict, key_name: str, list_name: list) -> list:
        # function to update a list taking a key from the variable or equation dictionary
        # this is intended to ignore duplicates
        for i in dictionary_name:
            if dictionary_name[i][key_name] not in list_name:
                list_name.append(dictionary_name[i][key_name])
        list_name_output = list(set(list_name))
        return list_name_output

    def separate_functions(self, equation=False):
        # TODO integrate function separation here
        pass

    def separate_variables(self, equation=False):
        """
        split equations by the all known operators
        store in list for processing
        :param equation:
        :return:
            list of variables (without copies)
        """
        variables = []

        if equation is False:
            for k in self.equations:
                # regular expression for splitting strings with given characters
                split_equations = re.split(r"[=+\-^*/\\()\[\]]", self.equations[k]['equation'])
                for i in split_equations:
                    if self.is_variable(i) and i not in variables:
                        variables.append(i)
            return variables
        elif isinstance(equation, str): #for outside calls
            equation = equation.replace(' ','')
            split_equations = re.split(r"[=+\-^*/\\()\[\]]", equation)
            for i in split_equations:
                if self.is_variable(i) and i not in variables:
                    variables.append(i)
            return variables
        else:
            raise TypeError

    def is_variable(self, variable):
        if variable is '':
            return False
        elif variable.isnumeric():
            return False
        elif self.is_float(variable):
            return False
        return True

    def is_float(self, var):
        if isinstance(var, float) == True:
            return True
        else:
            return False
    
    def debug_output(self):
        from pprint import pprint
        print("------------------------------------------")
        print("--------------DEBUG-PRINTOUT--------------")
        print("------------------------------------------")
        pprint(self.master, depth=1)
        print("\n\n")
        pprint(self.master)



if __name__ == "__main__":
    EQ = EquationCollection("x=1\ny=2\n\na= x+y\nsqu=sqa(")
    EQ.add_equation_to_dictionary("words=1", 4)
    EQ.update_class()
    EQ.debug_output()
