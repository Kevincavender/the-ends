import warnings
# THIS FILE HAS BEEN ABANDONED
# IT WILL BE REMOVED EVENTUALLY...


# from Eqn_solver.text_parsing import collect_variables
# Fix collect variables reference

# Define the expression whose roots we want to find
# take in an equation that needs to be reordered

"""
incorporate
Equation Object={...}
dictionary of all things

(from Solver.py)
exelist:
['A=2', 'B=5', 'C=4']
results list:
['A', 'B', 'C']

"""


def solve(equation, equation_variables, known_variables):
    '''
    :parameter
    equation
        string
    equation_variables
        list of strings
    known_variables
        list of strings
        This can be all variables or a small sub set of variables to compare
    :returns
    single_equation_run
        executable code to solve a single equation
        ['def equation(c): return (a+b+c - 2)', 'c = fsolve(equation, 1)', 'c=c[0]']
    [str(result_variable)]
        variable for results printing
    '''

    # Added to make the runtime warning exception work
    # changes warnings from scipy to exceptions
    warnings.filterwarnings(action="error", module="scipy")

    # puts equation on one side of the equals
    equation = reorder(equation)

    # separates known variables from variables in equation
    # this should be one variable
    result_variable = set(equation_variables).difference(known_variables)

    # this should raise an error if it's not going to work
    if len(result_variable) is not 1:
        raise Exception("FSOLVE: an Equation Variable Match Error has Occured")
    single_equation_run = func(equation, result_variable)
    return single_equation_run, [str(result_variable)]


def reorder(equation):
    import re
    left, right = re.split(r"[=]", equation)
    reordered = [left, '-', '(', right, ')']
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


def DivZeroCheck():
    from scipy.optimize import fsolve

    # 0= equation
    def equation(c):
        return 2 * c + 1
    try:
        ans = equation(0)
    except ZeroDivisionError:
        print("Divide by zero error")
    else:
        c = fsolve(equation, 2)
        c = c[0]
        print('C = ', c)
    return True

if __name__ == "__main__":
    import pprint
    # included fsolve import statement by default
    exec('from scipy.optimize import fsolve')
    singeq = solve("x+y=2+y", ["y", "x"], ["x", "z"])[0]
    singeq2 = solve("a+b+c=2", ["a", "b", "c"], ["a", "b", "d", "e"])[0]
    a = 2
    b = 2
    x = 3
    z = 5

    pprint.pprint(singeq2, indent=1, width=60)
    singeq = ['def equation(y): return (y)',
              'y = fsolve(equation, 1)',
              'y=y[0]']
    pprint.pprint(singeq, indent=1, width=60)
    try:
        for i in singeq+singeq2:
            exec(i)
        print("\nY = " + str(y))
        print("\nX = " + str(x))
        print("\nC = " + str(c))
    except RuntimeWarning:
        # add a thing to happen when this doesn't work
        print("\nTOO MANY COOKS: Not making progress on this equation")
        print("Possible issues:" +
              "\n- May be out of bounds for solver"
              "\n- May be inappropriate guess value"
              "\n- May result in (+/-) infinity"
              "\n- May be division by zero error")
    except NameError:
        print("NameError: solver not fully defined")
    print("\n Divzero check")
    DivZeroCheck()