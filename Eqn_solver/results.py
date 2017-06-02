import Eqn_solver.equation_parsing


def solve_and_print_results(equations):
    exelist = Eqn_solver.equation_parsing.parse_single_unknown_equations(equations, 0)
    print("\nEntered Equations: \n")
    for i in equations:
        print(i)
    print("\nResults: \n")
    for i in exelist:
        exec(i)
    return
