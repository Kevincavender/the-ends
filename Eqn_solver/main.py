"""
Module Docstring

THEENDS (The Ends)
THermodynamic Engineering Equations NeeD Solving

"""

__author__ = "Kevin Cavender"
__version__ = "0.0.1"
__license__ = "None atm"


import time
start_time = time.time()
from Eqn_solver.readfile import readfile
from Eqn_solver.EquationsClass import EquationsClass
import Eqn_solver.results


def main():
    """ Main entry point of the app 
    add: equations = EquationsClass(rf.readfile("1eqn")
    
    
    """
    equations = EquationsClass(readfile("1eqn")[0])
    solve = equations.check()

    if solve == 1:
        equations.format()
        Eqn_solver.results.solve_and_print_results(equations.equations)
    else:
        print("solver cannot continue because it pooped")

    if solve == 1:
        print('\n**************************************************')
        print('Number of Equations = ', len(equations.equation_dict()))
        print('Number of Variables = ', len(equations.variables()))
        print('List of Variables', ', '.join(equations.variables()))
        print("Time Elapsed: {:.3f}s".format(time.time() - start_time))
    return


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()