import Eqn_solver.EquationsClass
from Eqn_solver.text_parsing import collect_variables as collectvars


def parse_known_equations(equations):
    '''
        parses equations into 2 blocks
        block 1 is solvable with 1 step
        block 2 requires more steps
        results in single unknown equations parsed out
    :param equations: 
        list of equations
    :return: 
        block_1: list with one variable
        block_2: list with more than one variable
    '''
    # reorder equations so that python can order them properly
    variables, variable_dict = collectvars(equations)
    block_1 = []
    block_2 = []
    for i in variable_dict:
        if len(variable_dict[i]) == 1:
            block_1.append(i)
        else:
            block_2.append(i)
    return block_1, block_2


def parse_single_unknown_equations(equations, debug):
    eqn_block = list(parse_known_equations(equations))
    solvable_vars, solvable_vars_dict = collectvars(eqn_block[0])
    parsed = False
    count = 0
    current_block_num = 0

    if debug == 1:
        looplimit = 10
    else:
        looplimit = 200
    block_vars = [] # current list of block variables

    while parsed == False:
        count += 1
        if count > looplimit:
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
            if debug == 1:
                print("--------------------------------------------"
                      "--------------------"
                      "\nFinal Equation Block: " + str(eqn_block))
            break

        # by default the block is not solvable
        blockissolvable = False
        # simplify the reference to the current block
        current_block = eqn_block[current_block_num]

        if debug == True:
            print("\nCurrent Block: " + str(current_block))
            print("Block Number: " + str(current_block_num+1))
            # prints activity for debugging

        current_block_vars, current_block_vars_dict = collectvars(current_block)
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
            if debug == 1: print("block vars and solvable vars are the same")
            # if variables in block + variables in previous blocks = solvable variables
        elif set(block_vars) != set(solvable_vars):
            tmp_solvable_vars = []
            next_block_equation_list = []
            # print("Current Block: " + str(current_block))

            for current_equation in current_block:
                # print("Current Equation: " + str(current_equation))
                # check each equation in the current block to see if they are solvable
                solvable = issolvable(current_equation, solvable_vars, False)
                if solvable == False:
                    # move equation to next block
                    next_block_equation_list.append(current_equation)

                    if debug == 1: print(str(current_equation) + " is not solvable")
                if solvable == True:
                    # add variables to solvable variables
                    tmp_eqn_vars, tmp_eqn_vars_dict = collectvars([current_equation])
                    for v in tmp_eqn_vars:
                        tmp_solvable_vars.append(v)
                    if debug == 1: print(str(current_equation) + " is solvable")
                    # print("variables in equation test" + str(tmp_eqn_vars))

            for current_equation in next_block_equation_list:
                eqn_block[current_block_num + 1].append(current_equation)
                eqn_block[current_block_num].remove(current_equation)

            for variable in tmp_solvable_vars:
                solvable_vars.append(variable)
            if debug == 1: print("block vars and solvable vars are not the same")
            # iterate through current block equations
            # determine if not solvable
        if debug == 1:
            print("Block Variables " + str(block_vars))
            print("Solvable Variables " + str(solvable_vars))
            print("current equation block: " + str(eqn_block))
            print("Is block solvable: " + str(blockissolvable))
        if blockissolvable == True:
            current_block_num += 1
            eqn_block.append([])
            if debug == 1: print("next block\n--------------------------"
                  "--------------------------------------")
            # if the block is solvable, advance the block
    # check if block is solvable
        # read previous solveable variables (list them)
        # pull out solvable
        # move unsolvable to next level

    all_vars = sorted(set(solvable_vars))
    # executable list to be run by python interpreter
    execute_list = []
    for current_block in eqn_block:
        for current_equation in current_block:
            execute_list.append(current_equation)
    for current_variable in all_vars:
        execute_list.append('print("'+ current_variable + ' = " + str(float('+current_variable+')))')
    return execute_list


def issolvable(equation, solvablevars, debug):
    '''
    takes in a single equation and variables to compare it against
    determines variables in the equation
    returns a True/False condition
    :param equation: 
        single equation ['X2=X1+1'] as single item in list
    :param solvablevars:
        list of already solvable variables
    :param debug:
        set True for debug
    :return: 
        
    '''
    solvable = False
    if isinstance(equation, str):
        equation = [equation]
        # in case equation is not a list yet
    vars, var_dict = collectvars(equation)
    common_variables = list(set(vars).intersection(solvablevars))
    if debug == True:
        print(vars)
        print(solvablevars)
        print(common_variables)
    for i in common_variables:
        vars.remove(str(i))
    if len(vars) <= 1:
        solvable = True
    return solvable
