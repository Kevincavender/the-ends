

class Solver(object):
    """
    docstring yo
    take in list of equations
    
    """
    def __init__(self, input_equations):
        self.looplimit = 20
        self.eqn_obj = EquationsClass(input_equations)
        self.vdict = self.eqn_obj.variable_dict()
        self.debug = False
        self.equations = input_equations

    def original_solver(self):
        eqn_block = [self.equations, []]
        solvable_vars = []
        parsed = False
        count = 0
        current_block_num = 0

        while not parsed:
            count += 1
            # *****************************************************************
            # Loop Termination Items
            # *****************************************************************
            if count > self.looplimit:
                print("Loop Limit reached on block solver")
                execute_list = ['print("Error: Loop Limit Reached on Solver")']
                return execute_list

                # break if loop limit is reached
            elif eqn_block[current_block_num] == []:
                # when there are no more equations to sort,
                # terminate the loop
                eqn_block.remove([])
                if eqn_block[current_block_num] == []:
                    eqn_block.remove([])
                if self.debug == 1:
                    print("--------------------------------------------"
                          "--------------------"
                          "\nFinal Equation Block: " + str(eqn_block))
                break
            # *****************************************************************
            # Working with Current Block
            # *****************************************************************

            # by default the block is not solvable
            blockissolvable = False
            # simplify the reference to the current block
            current_block = eqn_block[current_block_num]

            if self.debug == True:
                print("\nCurrent Block: " + str(current_block))
                print("Block Number: " + str(current_block_num + 1))
                # prints activity for debugging

            current_block_vars = EquationsClass(current_block).variables()
            # collect variables in the current_block
            for current_variable in solvable_vars:
                # add current block variables to main variable list
                # appends the previously solvable variables
                current_block_vars.append(current_variable)

            block_vars = current_block_vars
            block_vars = list(set(block_vars))
            solvable_vars = list(set(solvable_vars))
            # order and remove duplicates
            if set(block_vars) == set(solvable_vars):
                blockissolvable = True
                if self.debug == 1: print("block vars and solvable vars are the same")
                # if variables in block + variables in previous blocks = solvable variables
            elif set(block_vars) != set(solvable_vars):
                tmp_solvable_vars = []
                next_block_equation_list = []
                # print("Current Block: " + str(current_block))

                for current_equation in current_block:
                    # print("Current Equation: " + str(current_equation))
                    # print("Solvable Variables: " + str(solvable_vars))
                    # check each equation in the current block to see if they are solvable
                    solvable = self.issolvable(current_equation, solvable_vars, False)
                    if solvable == False:
                        # move equation to next block
                        next_block_equation_list.append(current_equation)

                        if self.debug == 1: print(str(current_equation) + " is not solvable")
                    if solvable == True:
                        # add variables to solvable variables
                        tmp_eqn_vars = self.vdict[current_equation]
                        for v in tmp_eqn_vars:
                            tmp_solvable_vars.append(v)
                        if self.debug == 1: print(str(current_equation) + " is solvable")
                        # print("variables in equation test" + str(tmp_eqn_vars))

                for current_equation in next_block_equation_list:
                    eqn_block[current_block_num + 1].append(current_equation)
                    eqn_block[current_block_num].remove(current_equation)

                for variable in tmp_solvable_vars:
                    solvable_vars.append(variable)
                if self.debug == 1: print("block vars and solvable vars are not the same")
                # iterate through current block equations
                # determine if not solvable
            if self.debug == 1:
                print("Block Variables " + str(block_vars))
                print("Solvable Variables " + str(solvable_vars))
                print("current equation block: " + str(eqn_block))
                print("Is block solvable: " + str(blockissolvable))
            if blockissolvable == True:
                current_block_num += 1
                eqn_block.append([])
                if self.debug == 1: print("next block\n--------------------------"
                                          "--------------------------------------")
                # if the block is solvable, advance the block
        # check if block is solvable
            # read previous solveable variables (list them)
            # pull out solvable
            # move unsolvable to next level
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


if __name__ == "__main__":
    # test of is solvable

    import Eqn_solver.readfile as rf
    from Eqn_solver.results import solve_and_print_results
    input_file = "1eqn"
    eqns = rf.readfile(input_file)
    equations_object = EquationsClass(eqns)
    print("Reading input file of name: " + input_file + "\n")
    equations = equations_object.equations
    variables = equations_object.variables()
    # print(equations)
    # print(variables)
    # print(Solver(equations).issolvable(equations[0], variables[2], 0))
    exelist, resultslist = Solver(equations).original_solver()
    peqns = EquationsClass(eqns).equations
    print(exelist)
    print(resultslist)
    print(peqns)
    # solve_and_print_results(peqns, exelist)


