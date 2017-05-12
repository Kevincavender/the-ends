import Eqn_solver.text_parsing as tp


def parse_known_equations(equations):
    '''
        parses equations into 2 blocks
        block 1 is solvable with 1 step
        block 2 requires more steps
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
        if len(variable_dict[i]) == 0:
            print("error this equation: " + i + "has no variables")
        if len(variable_dict[i]) == 1:
            block_1.append(i)
        else:
            block_2.append(i)
    return block_1, block_2


def parse_all_equations(equations):

    variables, variable_dict = tp.collect_variables(equations)
    block_1, block_2 = parse_known_equations(equations)
    print("Block 1: " + str(block_1))
    print("Block 2: " + str(block_2))
    for i in block_1:
        print(i)
    for i in block_2:
        print(i)
    for i in variables:
        print('print("'+ i + ': " + str('+i+'))')
    return
