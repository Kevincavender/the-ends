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
from Eqn_solver.readfile import readfile
from Eqn_solver.EquationObject import EquationsClass
from Eqn_solver.Solver import Solver
from Eqn_solver.RunAndOutput import solve_and_print_results as results


def main(instring, debug=False):
    """ Main entry point of the app 
    add: equations = EquationsClass(rf.readfile("1eqn")
    
    
    """
    start_time = time.time()
    user_input = EquationsClass(instring)
    solve = user_input.check()

    if solve == 1:
        exelist, resultslist = Solver(user_input.equations, debug).primary_parser
        resultsout = results(user_input.entered_equations,exelist, resultslist)
        # print('**************************************************')
        # print('Number of Equations = ', len(user_input.equation_dict()))
        # print('Number of Variables = ', len(user_input.variables()))
        # print('List of Variables', ', '.join(user_input.variables()))
        # print("Time Elapsed: {:.3f}s".format(time.time() - start_time))
        # print('**************************************************')
    else:
        resultsout = "Unsolvable"
    return resultsout


if __name__ == "__main__":
    """ This is executed when run from the command line """
    resultout = main(readfile("1eqn"), debug=True)
    print(resultout)
