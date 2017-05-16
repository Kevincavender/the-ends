import Eqn_solver.scipy_solver as sci

A = 2
B = 5
equation = 'A**2+B**2=C**2'
known_vars = ['A', 'B']
execute_list = sci.solver(equation, known_vars, True)
for i in execute_list:
    exec(i)
print("C = " + str(C))
