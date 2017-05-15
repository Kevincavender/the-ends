import Eqn_solver.scipy_solver as sci

equation = 'A**2+B**2=C**2'
known_vars = ['A', 'B']
execute_list = sci.solver(equation, known_vars, True)
print(execute_list)
exec(execute_list)
# exec("print(C)")
