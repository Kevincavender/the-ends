from the_ends.EquationObject import EquationsClass
import math


class Solver(object):
    """
    docstring
    take in list of equations
    parse them
    solve them
    spit them back at the user in a rather violent but satifactory manner
    """

    def __init__(self, input_equations, debug=False):
        self.looplimit = 50
        self.eqn_obj = EquationsClass(input_equations)
        self.vdict = self.eqn_obj.variable_dict()
        self.debug = debug
        self.equations = input_equations

    def solve(self):
        #MAIN
        # this is the order in which the solver class is completed.
        eqn_block, solvable_vars = self.primary_parser
        exelist, resultlist = self.export_sorted_equations(eqn_block, solvable_vars)
        return exelist, resultlist

    def primary_parser(self):
        '''
        :param
        self.equations

        :return:
        '''

        eqn_block = [self.equations, []]
        solvable_vars = []
        parsed = False
        count = 0
        block_num = 0

        while not parsed:
            count += 1
            # *****************************************************************
            # Loop Termination Items
            # *****************************************************************
            # Loop is terminated if:
            # A: self.looplimit is reached
            # B: Current block has run out of equations
            # C: (NEED TO ADD) Remaining Block has multiple (self-contingent) unknowns
            if count > self.looplimit:
                print("Loop Limit reached on block solver")
                raise SolutionError

                # break if loop limit is reached
            # DO NOT CHANGE FROM == TO is
            elif eqn_block[block_num] == []:
                # when there are no more equations to sort,
                # terminate the loop
                eqn_block.remove([])
                # DO NOT MODIFY THIS LINE! things will break, frustration will ensue
                if eqn_block[block_num] == []:
                    eqn_block.remove([])
                if self.debug == 1:
                    print("--------------------------------------------"
                          "--------------------"
                          "\nFinal Equation Block: ")
                    for i in range(0, len(eqn_block)):
                        print("     " + str(eqn_block[i]))
                break

            # *****************************************************************
            # Working with Current Block
            # *****************************************************************

            # by default the block is not solvable
            blockissolvable = False

            # simplify the reference to the current block
            current_block = eqn_block[block_num]

            # collect variables in the current_block
            current_block_vars = EquationsClass(current_block).variables()

            # adds solvable variables to the current block variables
            block_vars = solvable_vars + current_block_vars

            # list(set()) operation to sort and remove duplicates
            block_vars = list(set(block_vars))
            block_vars = list(filter(None, block_vars))
            solvable_vars = list(set(solvable_vars))

            if self.debug is True:
                print("\nCurrent Block: " + str(current_block))
                print("Block Number: " + str(block_num + 1))
                # prints activity for debugging

            # Check if the block is already solvable
            # if variables in current block and
            #                 previous blocks
            #                 == solvable variables
            # --> revisit order of logic
            if set(block_vars) == set(solvable_vars):
                blockissolvable = True
                if self.debug == 1: print("block vars and solvable vars are the same")

            elif set(block_vars) != set(solvable_vars):
                tmp_solvable_vars = []
                next_block_equation_list = []
                number_of_unsolvable_equations = 0
                for current_equation in current_block:
                    # *****************************************************************
                    # Working with Current Equation (sorting single unknowns)
                    # *****************************************************************
                    # 1. Determine if solvable
                    #       By comparing solvable vars to current equation
                    # 2. If not solvable
                    #       Push Equation to next Block
                    # 3. If solvable
                    #       Add variables to Solvable Variables
                    #       Leave Equation in current block

                    solvable = self.issolvable(current_equation, solvable_vars, False)
                    if solvable is False:
                        number_of_unsolvable_equations +=1
                        # move equation to next block
                        next_block_equation_list.append(current_equation)

                        if self.debug == 1: print("Not Solvable--> " + str(current_equation))
                    elif solvable is True:
                        # add variables to solvable variables
                        tmp_eqn_vars = self.vdict[current_equation]
                        for v in tmp_eqn_vars:
                            tmp_solvable_vars.append(v)
                        if self.debug == 1: print("Solvable        " + str(current_equation))
                        # print("variables in equation test" + str(tmp_eqn_vars))
                if len(current_block) == number_of_unsolvable_equations:
                    raise SolutionError(current_block)

                # what does this do
                for current_equation in next_block_equation_list:
                    eqn_block[block_num + 1].append(current_equation)
                    eqn_block[block_num].remove(current_equation)

                # append tmp_solvable_vars to solvable vars
                solvable_vars.extend(tmp_solvable_vars)
                # for variable in tmp_solvable_vars:
                #    solvable_vars.append(variable)
                if self.debug == 1: print("block vars and solvable vars are not the same")
                # iterate through current block equations
                # determine if not solvable

            if self.debug == 1:
                print("Block Variables \n     " + str(block_vars))
                print("Solvable Variables \n     " + str(solvable_vars))
                print("current equation block: ")
                for i in range(0, len(eqn_block)):
                    print("     " + str(eqn_block[i]))
                print("Is block solvable: " + str(blockissolvable))

            if blockissolvable is True:
                # If the block is solvable, advance to next block
                block_num += 1
                eqn_block.append([])
                if self.debug == 1: print("next block\n--------------------------"
                                          "--------------------------------------")
        return eqn_block, solvable_vars

    def export_sorted_equations(self, eqn_block, solvable_vars):
        # *****************************************************************
        # Export of solvable list of variables
        # *****************************************************************
        all_vars = sorted(set(solvable_vars))
        # executable list to be run by python interpreter
        execute_list = []
        results_list = []
        for current_block in eqn_block:
            for current_equation in current_block:
                execute_list.append(current_equation)
        for current_variable in all_vars:
            results_list.append(current_variable)
        return execute_list, results_list

    def solver_selection(self):
        """
        Will read in execute_list and apply additional solvers as nessesary?
        - python math
        - fsolve
        (solving actually happens in tmp.py (might have changed))
        :parameter:
        solve("equation", "for this variable", "with this guess")
        :return:
        float of answer
        error message?
        """
        pass

    def issolvable(self, equation, solvablevars, debug):
        """
        takes in a single equation and variables to compare it against
        determines variables in the equation
        returns a True/False condition
        :param equation: 
            str single equation 'X2=X1+1'
        :param solvablevars:
            list of already solvable variables
        :param debug:
            set True for debug of this function
        :return solvable: 
            True if the equation, given the solvable variables
            is able to be solved
        """

        solvable = False
        svariables = self.vdict[equation]
        common_variables = list(set(svariables).intersection(solvablevars))
        if debug:
            print(svariables)
            print(solvablevars)
            print(common_variables)
        for i in common_variables:
            svariables.remove(str(i))
        if len(svariables) <= 1:
            solvable = True
        return solvable


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class SolutionError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression):
        self.expression = expression
        self.message = "These equations are unsolvable: \n" + \
                       str(self.expression)


class KevinSolver1:
    '''
    NOT CURRENTLY WORKING
    WORKING IN EQUATION SOLVER RESIDUALS
    say this is block 1
    x*2 = 5+y
    y+2 = x-2
    splits to
    x, x*2
    y, 5+y
    y, y+2
    x, x-2
    creates equation going to

    '''
    def __init__(self):
        pass

    def stringtofunction(self, equationstring="6*x"):
        mydict = {'eq': equationstring}
        A = mydict['eq']
        return A

    def fn1_1(self, x):
        return 2 * x

    def fn1_2(self, y):
        return y + 5

    def fn2_1(self, y):
        return y+2

    def fn2_2(self, x):
        return x-2

    def fn1_solve(self):
        pass

    def fn2_solve(self):
        pass

    def firsttry(self):

        x=1.0
        y=-3.0
        var1 = "x"
        var2 = "y"
        tries = 4
        maxerr = .00001
        delta = .001
        for tries in range(tries):
            ans1 = (self.solve2(self.fn1_1, self.fn1_2, x, y, var1, var2))
            ans2 = (self.solve2(self.fn2_1, self.fn2_2, y, x, var2, var1))
            ans1_delta = (self.solve2(self.fn1_1, self.fn1_2, x+delta, y+delta, var1, var2))
            ans2_delta = (self.solve2(self.fn2_1, self.fn2_2, y+delta, x+delta, var2, var1))
            #print(ans1, ans2)
            print("--------------")
            print(var1, ans1[var1], ans2[var1])
            print(var2, ans1[var2], ans2[var2])
            err1 = ans1[var1]-ans2[var1]
            err2 = ans1[var2]-ans2[var2]
            err = err1*err2
            print("x error:", err1,"y error:", err2)
            #x=(ans1[var1]+ans2[var1])/2.0
            #y=(ans1[var2]+ans2[var2])/2.0
            slope1_1 = (ans1_delta[var1]-ans1[var1])/delta # add to ans dict
            slope1_2 = (ans2_delta[var1]-ans2[var1])/delta
            slope2_1 = (ans1_delta[var2]-ans1[var2])/delta  # add to ans dict
            slope2_2 = (ans2_delta[var2]-ans2[var2])/delta
            if slope1_2 == 0:
                slope1_2 = 1.0
            if slope2_2 == 0:
                slope2_2 = 1.0
            x -= err/(slope1_1*slope1_2)
            y -= err/(slope2_1*slope2_2)
            print("New X:", x, "New Y:", y)
        return

    def dx(self, fn, x, delta=0.001):
        return (fn(x + delta) - fn(x)) / delta

    def solve_old(self, fn, value, x=0.5, maxtries=1000, maxerr=0.00001):
        for tries in range(maxtries):
            err = fn(x) - value
            if abs(err) < maxerr:
                x = math.ceil(x * 100000) / 100000
                return x
            slope = self.dx(fn, x)
            x -= err / slope
        raise ValueError('no solution found')

    def solve2(self, fn1, fn2, x1, x2, x1str, x2str, maxtries=1000, maxerr=0.00001):
        # currently finds a solution to an indeterminate set of equations
        err = 1.0
        for tries in range(maxtries):
            err = fn1(x1) - fn2(x2)
            if abs(err) < maxerr:
                x1 = math.ceil(x1 * 100000) / 100000
                x2 = math.ceil(x2 * 100000) / 100000
                return {x1str: x1, x2str: x2}
            slope1 = self.dx(fn1, x1)
            x1 -= err / slope1
            slope2 = self.dx(fn2, x2)
            x2 -= err / slope2
        if maxtries == 1:
            return {x1str: x1, x2str: x2}
        else:
            raise ValueError('no solution found')



def testsolverclass():
    """
        Testing Solver Class------------------------
        """
    # test of is solvable
    try:
        import Eqn_solver.readfile as rf

        input_file = "1eqn"
        eqns = rf.readfile(input_file)
        equations_object = EquationsClass(eqns)
        print("Reading input file of name: " + input_file)
        equations = equations_object.equations
        variables = equations_object.variables()
        # print(equations)
        # print(variables)
        # print(Solver(equations).issolvable(equations[0], variables[2], 0))
        exelist, resultslist = Solver(equations, debug=True).solve()
        peqns = EquationsClass(eqns).equations
        print("exelist:")
        print(exelist)
        print("results list:")
        print(resultslist)
        print("equations from equations class:")
        print(peqns)
        print("--------------\nTESTING\n--------------")
        for i in exelist:
            print(i)
            exec(i)
        print("\n")
        for i in resultslist:
            print(i, "=", float(eval(i))) # implement this elsewhere!!!!
            # solve_and_print_results(peqns, exelist)
    except SolutionError:
        print("\n\nTHE SOLVER BROKE!\nOH NO!!\n"
              "maybe if you try again you will get the same result...")


def testkevinsolver1class():
    solver = KevinSolver1()
    solver.firsttry()
    return


if __name__ == "__main__":
    testsolverclass()
    #testkevinsolver1class()
