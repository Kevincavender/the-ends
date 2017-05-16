import time
start_time = time.time()
import Eqn_solver.readfile as rf
import Eqn_solver.text_parsing as tp
import Eqn_solver.equation_parsing as eq_pars

equations, num_line = rf.readfile('1eqn')
equations, solve = tp.syntax_processing(equations)

if solve == 1:
    equations = tp.preprocess_equations(equations)
    # print("Text Cleanup Equations: \n   " + str(equations))
    variables, equation_dict = tp.collect_variables(equations)
    # print("Variables: \n    " + str(variables))
    # print("Variables reference: \n    " + str(equation_dict))
    equation_dict2 = tp.equation_dict(equations)
    # print("Equation Dictionary:\n    " + str(equation_dict2))
    exelist = eq_pars.parse_single_unknown_equations(equations, 0)
    print("\nEntered Equations: \n")
    for i in equations:
        print(i)
    print("\nResults: \n")
    for i in exelist:
        exec(i)
else:
    print("solver cannot continue because it pooped")

if solve == 1:
    print('\n********************************')
    print('Number of Equations = ', len(equation_dict))
    print('Number of Variables = ', len(variables))
    print('List of Variables', ', '.join(variables))
    print("Time Elapsed: {:.3f}s".format(time.time() - start_time))

