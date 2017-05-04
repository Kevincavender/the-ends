
import Eqn_solver.readfile as rf
import Eqn_solver.text_parsing as tp

equations, num_line = rf.readfile('1eqn')
# collect variables
solve = tp.syntax_checking(equations)
equations = tp.preprocess_equations(equations)
if solve == True:
    variables = tp.collect_variables(equations)
    tp.parse_known_equations(equations)
else:
    print("solver cannot continue")

# printing output for debuging

# print('\n', equations)
# print('\n', equations2)


if solve == 1:
    print('\n********************************')
    print('Number of Equations = ', num_line)
    print('Number of Variables = ', len(variables))
    print('List of Variables', ', '.join(variables))


