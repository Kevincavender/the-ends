import os


def solve_and_print_results(equations, exelist, results_list):
    '''
    creates temporary python file to execute solving in it's own environment
    tmp python file records the results output to a tmp text file
    the output of the text file is send back to the user
    '''

    # open file that write execution code to
    pyfile = open("tmp.py", "w")

    # Write list of imported libraries into python
    librarylist = [
        ""
    ]
    for i in librarylist:
        pyfile.write(i + "\n")

    # Write python executable equations
    for i in exelist:
        pyfile.write(str(i) + "\n")

    results = [
        '\ntextfile = open("tmp.txt", "w")',
        '',
        r'textfile.write("Entered Equations: \n\n")',
        'for i in' + str(equations) + ': ',
        r'    textfile.write(i + "\n")',
        r'textfile.write("\nResults: \n\n")',
        '\n'
              ]

    # Have python evaluate the print out entered equations
    for i in results:
        pyfile.write(i + "\n")

    # Have python print results to each variable
    for i in results_list:
        pyfile.write('print("'+i+' = " + str(float('+i+')), file=textfile)\n')
    pyfile.write('textfile.close()\n')
    pyfile.close()

    # Run the just created python file
    os.system("python tmp.py")

    # Open text file that python created
    # Read the text file and return the results
    with open('tmp.txt', mode='r') as f:
        line_list = []
        # read in lines
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            line_list.append(line)
    outstring = "".join(list(filter(None, line_list)))
    return outstring


def solve_and_print_results_only(exelist, results_list):
    '''
    creates temporary python file to execute solving in it's own environment
    tmp python file records the results output to a tmp text file
    the output of the text file is send back to the user
    '''

    # open file that write execution code to
    pyfile = open("tmp.py", "w")

    # Write list of imported libraries into python
    # librarylist = [
    #     ""
    # ]
    # for i in librarylist:
    #    pyfile.write(i + "\n")

    # Write python executable equations
    for i in exelist:
        pyfile.write(str(i) + "\n")

    pyfile.write('textfile = open("tmp.txt", "w")\n')

    # Have python print results to each variable
    for i in results_list:
        pyfile.write('print("'+i+' = " + str(float('+i+')), file=textfile)\n')
    pyfile.write('textfile.close()\n')
    pyfile.close()

    # Run the just created python file
    os.system("python tmp.py")

    # Open text file that python created
    # Read the text file and return the results
    with open('tmp.txt', mode='r') as f:
        line_list = []
        # read in lines
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            line_list.append(line)
    outstring = "".join(list(filter(None, line_list)))
    return outstring


class OutputCode:
    """
    code in the class comes in to be collected into an executable form of python code
    NOT USED
    """
    def __init__(self):
        pass

    def funcname(self, inputvar):
        name = "def eq_" + inputvar
        return str(name)

    def createfunc(self, inputvar, inputequ):
        # use form
        # def solvefor_x(x):
        #     return x * 2

        firstline = "(" + inputvar + "):\n"
        secondline = "     return " + inputequ
        return str(firstline + secondline)

    def execfunc(self):
        pass


def testcreatefunc():
    outclass = OutputCode
    x = outclass.createfunc("x","x*2")
    print(x)
    exec(x)
    exec("print(eq_x(4))")
    return


if __name__ == '__main__':
    printed_output = solve_and_print_results(
        ['a = 2', 'b = 5', 'c = 4',
         'e = 4+f', 'f = b', 'g = b',
         'd = c + e', 'x1 = 20', 'x2 = x1+3',
         'x3 = x2 -10'],
        ['A=2', 'B=5', 'C=4',
         'X1=20', 'F=B', 'G=B', 'X2=X1+3',
         'E=4+F', 'X3=X2-10', 'D=C+E'],
        ['A', 'B', 'C', 'D', 'E', 'F',
         'G', 'X1', 'X2', 'X3'])
    # print(printed_output)
    # testcreatefunc()
