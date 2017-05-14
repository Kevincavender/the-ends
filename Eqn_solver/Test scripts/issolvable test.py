from Eqn_solver.equation_parsing import issolvable

equation = ['X3=X+1']
solvablevars = ['X1', 'X']

solvable = issolvable(equation, solvablevars, True)

print("Is equation solvable: " + str(solvable))