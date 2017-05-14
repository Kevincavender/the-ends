import Eqn_solver.text_parsing as tp


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
    variables, variable_dict = tp.collect_variables(equations)
    block_1 = []
    block_2 = []
    for i in variable_dict:
        if len(variable_dict[i]) == 1:
            block_1.append(i)
        else:
            block_2.append(i)
    return block_1, block_2


def parse_all_equations(equations, debug):
    from Eqn_solver.text_parsing import collect_variables as cvars
    block_1, block_2 = parse_known_equations(equations)
    solvable_vars, solvable_vars_dict = cvars(block_1)
    eqn_block = [block_1, block_2]

    parsed = False
    count = 0
    current_block_num = 0
    if debug == 1:
        looplimit = 15
    else:
        looplimit = 200
    block_vars = [] # current list of block variables
    while parsed == False:
        count += 1
        if count > looplimit:
            break
        elif eqn_block[current_block_num] == []:
            eqn_block.remove([])
            if debug == 1:
                print("--------------------------------------------"
                      "\nFinal Equation Block: " + str(eqn_block))

            break
        blockissolvable = False
        current_block = eqn_block[current_block_num]
        if debug == True:
            print("\nCurrent Block: " + str(current_block))
            print("Block Number: " + str(current_block_num+1))
        # prints activity for debugging

        current_block_vars, current_block_vars_dict = cvars(current_block)
        # list variables in the block
        for i in solvable_vars:
            # add current block variables to main variable list
            current_block_vars.append(i)
        block_vars = current_block_vars
        block_vars = list(set(block_vars))
        solvable_vars = list(set(solvable_vars))
        # order and remove duplicates
        if set(block_vars) == set(solvable_vars):
            blockissolvable = True
            # if variables in block + variables in previous blocks = solvable variables
        elif block_vars != solvable_vars:
            for i in current_block:
                # check each equation in the current block to see if they are solvable
                solvable = issolvable(i, solvable_vars, False)
                if solvable == False:
                    # move equation to next block
                    eqn_block[current_block_num+1].append(i)
                    eqn_block[current_block_num].remove(i)
                    if debug == 1: print(str(i) + " is not solvable")
                if solvable == True:
                    # add variables to solvable variables
                    tmp_eqn_vars, tmp_eqn_vars_dict = cvars([i])
                    for v in tmp_eqn_vars:
                        solvable_vars.append(v)
                    if debug == 1: print(str(i) + " is solvable")
                    # print("variables in equation test" + str(tmp_eqn_vars))
            if debug == 1:print("block vars and solvable vars are not the same")
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
    for b in eqn_block:
        for i in b:
            execute_list.append(i)
    for i in all_vars:
        execute_list.append('print("'+ i + ' = " + str('+i+'))')
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
    vars, var_dict = tp.collect_variables(equation)
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
