#!/usr/bin/python
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
from readfile import readfile
from EquationObject import EquationsClass
from Solver import Solver
from RunAndOutput import solve_and_print_results as results


def main(instring, debug=False):
    """ Main entry point of the app 
    add: equations = EquationsClass(rf.readfile("1eqn")
    
    
    """
    start_time = time.time()
    user_input = EquationsClass(instring)
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
    return resultsout


if __name__ == "__main__":
    """ This is executed when run from the command line """
    debug = False
    try:
        results_out = main(readfile(sys.argv[1]), debug=debug)
        print(results_out)

    except:
        print("ERROR: I DON'T KNOW WHAT HAPPENED BUT SOMETHING BROKE")