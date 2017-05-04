import time
start_time = time.time()
import Eqn_solver.readfile as rf
import Eqn_solver.text_parsing as tp

equations, num_line = rf.readfile('1eqn')
solve = tp.syntax_checking(equations)

if solve == 1:
    equations = tp.preprocess_equations(equations)
    print("preprocess: " + str(equations))
    variables, equation_dict = tp.collect_variables(equations)
    print("collecting variables: " + str(variables))
    print("collecting variables reference: " + str(equation_dict))
    equation_dict2 = tp.equation_dict(equations)
    print("here:" + str(equation_dict2))
    equ = tp.syntax_correction(equations)
    block_1, block_2 = tp.parse_known_equations(equations)
    print("Block 1: " + str(block_1))
    print("Block 2: " + str(block_2))
else:
    print("solver cannot continue")


if solve == 1:
    print('\n********************************')
    print('Number of Equations = ', len(equation_dict))
    print('Number of Variables = ', len(variables))
    print('List of Variables', ', '.join(variables))
    print("Time Elapsed: {:.2f}s".format(time.time() - start_time))


