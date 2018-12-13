from EquationErrorCheck import EquationErrorCheck
import re


class EquationCollection(object):
    
    """
    This Class is for interacting with metadata of the equations entered as a string

    Example of equations and variables dictionaries

    block_number : used for the solution order of the equations
    error: used for giving specific error results to the user
    variables and equations are cross listed to allow for storing resulting values in one place

    """

    def __init__(self, equation_string=''):
        self.equation_strings = self.parse_by_line(equation_string)
        self.equation_string = equation_string
        # each equation dictionary within the self.equations dictionary
        # will get it's own index number
        # (starting at 1 because 0 is being used by the example listed here)
        self.equations = {
            0: dict(
                equation='',
                variables=[],
                solved=False,
                line_number=0,
                error='',
                block_number=0),
            
        }
        self.variables = {
            0: dict(
                variable_name='',
                equations=[],
                value=1.0,
                initial_value=1.0,
                solved=False
            ),
        }
        self.number_of_equations = 0
        self.number_of_variables = 0
        self.variable_list = []
        self.equation_list = []
        self.solved_variable_list = []
        self.solved_equation_list = []
        self.master = {}
        #solver initializations
        self.looplimit = 50
        #self.eqn_obj = EquationsClass(input_equations)
        self.vdict = self.variable_list
        #self.debug = debug
        #self.equations = input_equations
        self.eqn_block = []
        self.solvable_vars = []

        # will populate the previous variables
        self.parse_eqns_from_string(self.equation_string)
        self.update_class()

    def __repr__(self):
        # this needs a detailed printout of what's in the string
        return str(self.equations)

    def update_class(self):
        # this order is important
        self.update_variable_dictionary()
        self.update_equation_list()
        self.update_variable_list()
        self.update_number_of_equations()
        self.update_number_of_variables()
        self.update_solved_equation_list()
        self.update_solved_variable_list()
        self.update_master()

    def check_for_errors(self):
        okay = False
        for i in self.equation_strings:
            equ = EquationErrorCheck(self.equation_strings[i], i + 1)
            o = equ.checkline()
            k = equ.check_trailing_operators
            a = equ.check_symbols
            y = equ.check_matching_parenthesis
            ok = equ.check_matching_brackets
            if o == True and k == True and a == True and y == True and ok == True:
                okay = True
            
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
        list_of_lines = self.equation_string.split("\n")
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
            else:
                self.add_equation_to_dictionary(list_of_lines[i], i+1)
            i += 1

    def add_equation_to_dictionary(self, equation_string, line_number=0):
        new_equation_number = line_number
        # need to check and parse equation string
        # need to check and parse variables in equation
        equation = equation_string  # must be string
        functions_in_equation = self.separate_functions(equation)
        variables_in_equation = self.separate_variables(equation)  # must be list of strings
        self.equations[new_equation_number] = {
            "equation": equation,
            "variables": variables_in_equation,
            "solved": False,
            "line_number": line_number,
            "error": '',
            "block_number": 0,
            "root_equation": '',
            "functions": functions_in_equation
        }

    def update_master(self):
        self.master = {
            "Equations": self.equations,
            "Variables": self.variables,
            "Number of Equations": self.number_of_equations,
            "Equation List": self.equation_list,
            "Solved Equations": self.solved_equation_list,
            "Number of Variables": self.number_of_variables,
            "Variable List": self.variable_list,
            "Solved Variable List": self.solved_variable_list

        }

    def update_variable_dictionary(self):
        # looks at equation dictionary to update variable dictionary
        # 1: {'equation': 'x=1', "variables": ['X'], 'solved': False, "line_number": 2, "error": ''},
        # 1: {'variable_name': 'a', 'equations': ['a=1'], 'value': 1.0, 'initial_value': 1.0, 'solved': False},

        # self.update_variable_list()
        # self.update_equation_list()
        #
        # for i in self.equations:
        #     # i = 3 (int)
        #     # i is a dictionary of equation information
        #     current_variable_list = self.equations[i]['variables']
        #     current_equation = self.equations[i]['equation']
        #     for j in current_variable_list:
        #         # j = 'x' (string, variable)
        #         self.update_variable_list()
        #         self.update_equation_list()
        #         new_variables_number = max(list(self.variables.keys())) + 1
        #         if j not in self.variable_list:
        #             self.variables[new_variables_number] = {
        #                 'variable_name': j,
        #                 'equations': [current_equation],
        #                 'value': 1.0,
        #                 'initial_value': 1.0,
        #                 'solved': False
        #             }
        #     print([current_equation])
        #     print(self.variables[i]['equations'])
        #     for k in self.variables:
        #         if (current_equation not in self.variables[k]['equations']) and (k not in current_variable_list):
        #             self.variables[k]['equations'].append(current_equation)
        for i in self.equations:
            # Creates new variable dictionary if none exists

            variable_list_in_equation = self.equations[i]['variables']
            equation_in_equation = self.equations[i]['equation']

            for var in variable_list_in_equation:
                self.update_variable_list()
                new_variables_number = max(list(self.variables.keys())) + 1
                if var not in self.variable_list:
                    self.variables[new_variables_number] = {
                                'variable_name': var,
                                'equations': [],
                                'value': 1.0,
                                'initial_value': 1.0,
                                'solved': False
                            }
            for j in self.variables:
                variable_in_variables = self.variables[j]['variable_name']
                equations_in_variables = self.variables[j]['equations']
                check1 = equation_in_equation not in equations_in_variables
                check2 = variable_in_variables in variable_list_in_equation
                if check1 and check2:
                    self.variables[j]['equations'].append(equation_in_equation)

        return

    def parse_line(self, line_string, line_number):
        line = EquationErrorCheck(line_string, line_number)
        try:
            line.checkline()
        except SyntaxError:
            print("Syntax Error Detected:\n\tLine error")
        equations = line_string.split("\n")
        equations = equations.replace(' ', '')
        return equations

    def update_number_of_equations(self):
        self.number_of_equations = len(self.equations)

    def update_number_of_variables(self):
        self.number_of_variables = len(self.variables)

    def update_variable_list(self):
        self.variable_list = self.update_list_from_dictionary(self.variables, 'variable_name', self.variable_list)

    def update_equation_list(self):
        self.equation_list = self.update_list_from_dictionary(self.equations, 'equation', self.equation_list)

    def update_solved_variable_list(self):
        for i in self.variables:
            if self.variables[i]['solved'] is True:
                self.solved_variable_list.append(self.variables[i]['variable_name'])
                self.solved_variable_list = list(set(self.solved_variable_list))

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
