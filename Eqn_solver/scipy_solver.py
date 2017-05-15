from Eqn_solver.text_parsing import collect_variables

# Define the expression whose roots we want to find
# take in an equation that can't be executed by mpmath


def solver(equation, known_variables, first_run):
    equation = reorder(equation)
    variables, variable_dict = collect_variables(equation)
    common_variables = []
    common_variables = set(variables).difference(known_variables)
    list1 = func(equation, common_variables)
    if first_run == True:
        import_string = '\"from scipy.optimize import fsolve\"'
        single_equation_run = import_string + "\n" + list1
    return single_equation_run


def reorder(equation):
    import re
    left, right = re.split(r"[=]", equation)
    reordered = [left, '-', right]
    reordered = ''.join(reordered)
    return reordered


def func(equation, solved_for_variable):
    initial_guess = 1
    v = str(list(solved_for_variable)[0])
    solver_list = [
        "\"" + v + " = fsolve(",
        "equation, ",
        str(initial_guess), ")\""
    ]
    equation_list = [
        "\"def equation(", v,"):",
        " return (", str(equation),
        ")\"\n"
    ]
    list1 = equation_list + solver_list
    list1 = ''.join(list1)
    # Use the numerical solver to find the roots
    # tau_solution = fsolve(funct, initial_guess)

    # print ("The solution is tau = %f" % tau_solution)
    # print ("at which the value of the expression is %f" % func(tau_solution))
    return list1