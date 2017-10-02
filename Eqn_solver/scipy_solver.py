# from Eqn_solver.text_parsing import collect_variables
# Fix collect variables reference

# Define the expression whose roots we want to find
# take in an equation that needs to be reordered

"""
incorporate
Equation Object={...}
dictionary of all things


"""
def solver(equation, equation_variables, known_variables, first_run):
    '''
    equation
        string
    known_variables
        list of strings
    first_run
        determine whether this function has been used yet for import statement
        --> make first_run a global variable?
    '''
    equation = reorder(equation)
    common_variables = set(equation_variables).difference(known_variables)
    list1 = func(equation, common_variables)
    if first_run == True:
        import_string = ["from scipy.optimize import fsolve"]
        single_equation_run = import_string + list1
    else:
        single_equation_run = list1
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
        "" + v + " = fsolve(",
        "equation, ",
        str(initial_guess), ")"
    ]
    equation_list = [
        "def equation(", v,"):",
        " return (", str(equation),
        ")"
    ]
    formating = [
        v + "=" + v + "[0]"
    ]
    list1 = [''.join(equation_list), ''.join(solver_list), ''.join(formating)]
    return list1

if __name__ == "__main__":
    import pprint
    singeq = solver("x+y = 2", ["x", "y"], ["x"], 1)
    x = 1
    pprint.pprint(singeq)
    for i in singeq:
        exec(i)
    print(y)
