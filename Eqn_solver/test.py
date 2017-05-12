import time
start_time = time.time()
import Eqn_solver.readfile as rf
import Eqn_solver.text_parsing as tp

equations, num_line = rf.readfile('1eqn')
solve = tp.syntax_checking(equations)

if solve == 1:
    equations = tp.preprocess_equations(equations)
    print("Text Cleanup: " + str(equations))
    variables, equation_dict = tp.collect_variables(equations)
    print("Variables: " + str(variables))
    print("Variables reference: " + str(equation_dict))
    equation_dict2 = tp.equation_dict(equations)
    print("Equation Dictionary:" + str(equation_dict2))
    equations = tp.syntax_correction(equations)

else:
    print("solver cannot continue")


if solve == 1:
    print('\n********************************')
    print('Number of Equations = ', len(equation_dict))
    print('Number of Variables = ', len(variables))
    print('List of Variables', ', '.join(variables))
    print("Time Elapsed: {:.3f}s".format(time.time() - start_time))


