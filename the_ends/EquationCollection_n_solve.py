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

    def update_class(self):
        pass
    
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

    """
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
    """

    def separate_functions(self, equation=False):
        # TODO integrate function separation here
        pass


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


    #Solver functions
    def solve(self):
        #MAIN
        # this is the order in which the solver class is completed.
        eqn_block, solvable_vars = self.primary_parser
        exelist, resultlist = self.exportSortedEquations(self.eqn_block, self.solvable_vars)
        return exelist, resultlist

    def primary_parser(self):
        '''
        :param
        self.equations

        :return:
        '''

        eqn_block = [self.equations, []]
        solvable_vars = []
        parsed = False
        count = 0
        block_num = 0

        while not parsed:
            count += 1
            # *****************************************************************
            # Loop Termination Items
            # *****************************************************************
            # Loop is terminated if:
            # A: self.looplimit is reached
            # B: Current block has run out of equations
            # C: (NEED TO ADD) Remaining Block has multiple (self-contingent) unknowns
            if count > self.looplimit:
                print("Loop Limit reached on block solver")
                raise SolutionError

                # break if loop limit is reached
            # DO NOT CHANGE FROM == TO is
            elif eqn_block[block_num] == []:
                # when there are no more equations to sort,
                # terminate the loop
                eqn_block.remove([])
                # DO NOT MODIFY THIS LINE! things will break, frustration will ensue
                if eqn_block[block_num] == []:
                    eqn_block.remove([])
                if self.debug == 1:
                    print("--------------------------------------------"
                          "--------------------"
                          "\nFinal Equation Block: ")
                    for i in range(0, len(eqn_block)):
                        print("     " + str(eqn_block[i]))
                break

            # *****************************************************************
            # Working with Current Block
            # *****************************************************************

            # by default the block is not solvable
            blockissolvable = False

            # simplify the reference to the current block
            current_block = eqn_block[block_num]

            # collect variables in the current_block
            current_block_vars = EquationsClass(current_block).variables()

            # adds solvable variables to the current block variables
            block_vars = solvable_vars + current_block_vars

            # list(set()) operation to sort and remove duplicates
            block_vars = list(set(block_vars))
            block_vars = list(filter(None, block_vars))
            solvable_vars = list(set(solvable_vars))

            if self.debug is True:
                print("\nCurrent Block: " + str(current_block))
                print("Block Number: " + str(block_num + 1))
                # prints activity for debugging

            # Check if the block is already solvable
            # if variables in current block and
            #                 previous blocks
            #                 == solvable variables
            # --> revisit order of logic
            if set(block_vars) == set(solvable_vars):
                blockissolvable = True
                if self.debug == 1: print("block vars and solvable vars are the same")

            elif set(block_vars) != set(solvable_vars):
                tmp_solvable_vars = []
                next_block_equation_list = []
                number_of_unsolvable_equations = 0
                for current_equation in current_block:
                    # *****************************************************************
                    # Working with Current Equation (sorting single unknowns)
                    # *****************************************************************
                    # 1. Determine if solvable
                    #       By comparing solvable vars to current equation
                    # 2. If not solvable
                    #       Push Equation to next Block
                    # 3. If solvable
                    #       Add variables to Solvable Variables
                    #       Leave Equation in current block

                    solvable = self.issolvable(current_equation, solvable_vars, False)
                    if solvable is False:
                        number_of_unsolvable_equations +=1
                        # move equation to next block
                        next_block_equation_list.append(current_equation)

                        if self.debug == 1: print("Not Solvable--> " + str(current_equation))
                    elif solvable is True:
                        # add variables to solvable variables
                        tmp_eqn_vars = self.vdict[current_equation]
                        for v in tmp_eqn_vars:
                            tmp_solvable_vars.append(v)
                        if self.debug == 1: print("Solvable        " + str(current_equation))
                        # print("variables in equation test" + str(tmp_eqn_vars))
                if len(current_block) == number_of_unsolvable_equations:
                    raise SolutionError(current_block)

                for current_equation in next_block_equation_list:
                    eqn_block[block_num + 1].append(current_equation)
                    eqn_block[block_num].remove(current_equation)

                # append tmp_solvable_vars to solvable vars
                solvable_vars.extend(tmp_solvable_vars)
                # for variable in tmp_solvable_vars:
                #    solvable_vars.append(variable)
                if self.debug == 1: print("block vars and solvable vars are not the same")
                # iterate through current block equations
                # determine if not solvable

            if self.debug == 1:
                print("Block Variables \n     " + str(block_vars))
                print("Solvable Variables \n     " + str(solvable_vars))
                print("current equation block: ")
                for i in range(0, len(eqn_block)):
                    print("     " + str(eqn_block[i]))
                print("Is block solvable: " + str(blockissolvable))

            if blockissolvable is True:
                # If the block is solvable, advance to next block
                block_num += 1
                eqn_block.append([])
                if self.debug == 1: print("next block\n--------------------------"
                                          "--------------------------------------")
        self.eqn_block = eqn_block
        self.solvable_vars = solvable_vars
        return None

    def exportSortedEquations(self, eqn_block, solvable_vars):
        # *****************************************************************
        # Export of solvable list of variables
        # *****************************************************************
        all_vars = sorted(set(solvable_vars))
        # executable list to be run by python interpreter
        execute_list = []
        results_list = []
        for current_block in eqn_block:
            for current_equation in current_block:
                execute_list.append(current_equation)
        for current_variable in all_vars:
            results_list.append(current_variable)
        return execute_list, results_list

    def issolvable(self, equation, solvablevars, debug):
        """
        takes in a single equation and variables to compare it against
        determines variables in the equation
        returns a True/False condition
        :param equation: 
            str single equation 'X2=X1+1'
        :param solvablevars:
            list of already solvable variables
        :param debug:
            set True for debug of this function
        :return solvable: 
            True if the equation, given the solvable variables
            is able to be solved
        """

        solvable = False
        svariables = self.vdict[equation]
        common_variables = list(set(svariables).intersection(solvablevars))
        if debug:
            print(svariables)
            print(solvablevars)
            print(common_variables)
        for i in common_variables:
            svariables.remove(str(i))
        if len(svariables) <= 1:
            solvable = True
        return solvable

    
    def debug_output(self):
        from pprint import pprint
        print("------------------------------------------")
        print("--------------DEBUG-PRINTOUT--------------")
        print("------------------------------------------")
        pass



if __name__ == "__main__":
    EQ = EquationCollection_n_solve("x=1\ny=2\n\na= x+y\nsqu=sqa(")
    EQ.add_equation_to_dictionary("words=1", 4)
    EQ.debug_output()
