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

"""
import time
import sys
from the_ends.readfile import readfile
from the_ends.EquationObject import EquationsClass
from the_ends.Solver import Solver
from the_ends.RunAndOutput import solve_and_print_results as results


def main(args=None, debug=False):
    """ Main entry point of the app 
    add: equations = EquationsClass(rf.readfile("1eqn")
    
    
    """
    if args is None:
        args = sys.argv[1]
    else:
        print("something is wrong with how main is being called")
    input_filename = args
    input_string = readfile(input_filename)
    start_time = time.time()
    user_input = EquationsClass(input_string)
    solve = user_input.check()

    if solve == 1:
        exelist, resultslist = Solver(user_input.equations, debug).solve()
        resultsout = results(user_input.entered_equations,exelist, resultslist)
        # print('**************************************************')
        # print('Number of Equations = ', len(user_input.equation_dict()))
        # print('Number of Variables = ', len(user_input.variables()))
        # print('List of Variables', ', '.join(user_input.variables()))
        print("Time Elapsed: {:.3f}s".format(time.time() - start_time))
        # print('**************************************************')
    else:
        resultsout = "Unsolvable"
    print(resultsout)
    return resultsout


if __name__ == "__main__":
    main()