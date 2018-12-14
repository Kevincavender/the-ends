#!/usr/bin/python3
"""
Module Docstring

THEENDS (The Ends)
THermodynamic Engineering Equations NeeD Solving

1. Read in file of equations
    readfile.py
2. Create Equations Object from text
    EquationObject.py
3. Check Equations for errors
    EquationObject.py --> EquationErrorCheck.py
4. Run Equations through Solver/Parser
    Solver.py
5. run and export results
    RunAndOutput.py


TODO replace EquationObject with Equation Collection
"""
import time
import sys
from the_ends.readfile import readfile
from the_ends.EquationCollection_n_solve import EquationCollection_n_solve as EquationClass
from the_ends.RunAndOutput import solve_and_print_results as results


def main(args=None, debug=False):
    """ Main entry point of the app
    # args currently 1eqn (which si a text file of the input equations)
    add: equations = EquationsClass(rf.readfile("1eqn")
    
    
    """
    try:
        if args is None:
            args = sys.argv[1]
        else:
            print("\n--------------\nFiles read by \ncalling Main()\n--------------\n")
    except IOError:
        print("IOError: something is wrong with how main is being called")
    except TypeError:
        print("TypeError: something is wrong with how main is being called")
    except SyntaxError:
        print("SyntaxError: ... somewhere")

    input_filename = args
    input_string = readfile(input_filename)
    start_time = time.time()
    user_equations = EquationsClass(input_string)
    solve = user_equations.check_for_errors()

    if solve is True:
        execute_list, results_list = user_equations.solve
        results_out = results(user_equations.equations_list,execute_list, results_list)
        # print('**************************************************')
        # print('Number of Equations = ', len(user_equations.equation_dict()))
        # print('Number of Variables = ', len(user_equations.variables()))
        # print('List of Variables', ', '.join(user_equations.variables()))
        print("Time Elapsed: {:.3f}s".format(time.time() - start_time))
        # print('**************************************************')
    else:
        results_out = "Unsolvable by unknown error"

    if debug is True:
        print("\nDEBUG:")
        print("readfile.readfile(): " + str(input_string))
        print("EquationObject.EquationsClass(): " + repr(user_equations))
        print("user_equation.check(): " + repr(user_equations.check()))
        print("END DEBUG\n")
    # print(results_out)
    return results_out


if __name__ == "__main__":
    print(main(args='1eqn', debug=True))
