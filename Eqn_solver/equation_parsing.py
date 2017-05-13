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


def parse_all_equations(equations):
    from Eqn_solver.text_parsing import collect_variables as vars
    all_variables, all_variable_dict = vars(equations)
    block_1, block_2 = parse_known_equations(equations)
    solvable_vars, solvable_vars_dict = vars(block_1)
    print(solvable_vars)
    eqn_block = [[block_1], [block_2]]

    parsed = False
    count = 0
    current_block = 0
    block_vars = [] # current list of block variables
    while parsed == False:
        count += 1
        if count > 5:
            break
        blockissolvable = False
        print("Current Block: " + str(eqn_block[current_block][0]))
        # prints activity for debugging
        current_block_vars, current_block_vars_dict = vars(eqn_block[current_block][0])
        # list variables in the block
        for i in current_block_vars:
            # add current block variables to main variable list
            block_vars.append(i)
        block_vars = list(set(block_vars))
        # order and remove duplicates
        print(block_vars)

            # if variables in block + variables in previous blocks = solvable variables
            # make it true
        if blockissolvable == True:
            current_block += 1
            # if the block is solvable, advance the block
# list(set(t)) will remove duplicates
    # check if block is solvable
        # read previous solveable variables (list them)
        # pull out solvable
        # move unsolvable to next level
    '''
    # executable list to be run by python interpreter
    execute_list = []
    for i in block_1:
        execute_list.append(i)
    for i in block_2:
        execute_list.append(i)
    for i in variables:
        execute_list.append('print("'+ i + ' = " + str('+i+'))')
        '''
    return
