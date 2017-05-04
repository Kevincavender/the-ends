import time
start_time = time.time()
import Eqn_solver.readfile as rf
import Eqn_solver.text_parsing as tp

equations, num_line = rf.readfile('1eqn')
solve = tp.syntax_checking(equations)

if solve == 1:
    equations = tp.preprocess_equations(equations)
    # print("preprocess: " + str(equations))
    variables, equation_dict = tp.collect_variables(equations)
    # print("collecting variables: " + str(variables))
    # print("collecting variables reference: " + str(equation_dict))
    tp.parse_known_equations(equations)
else:
    print("solver cannot continue")
'''

if solve == 1:
    print('\n********************************')
    print('Number of Equations = ', len(equation_dict))
    print('Number of Variables = ', len(variables))
    print('List of Variables', ', '.join(variables))
    print("Time Elapsed: {:.2f}s".format(time.time() - start_time))
    
    '''


