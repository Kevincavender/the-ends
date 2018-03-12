def solve_and_print_results(equations, exelist, results_list):
    '''
    creates temporary python file to execute solving in it's own environment
    tmp python file records the results output to a tmp text file, which is 
    '''
    pyfile = open("tmp.py", "w")

    results = [
        'textfile = open("tmp.txt", "w")',
        r'textfile.write("Entered Equations: \n\n")',
        'for i in' + str(equations) + ': ',
        r'    textfile.write(i + "\n")',
        r'textfile.write("\nResults: \n\n")',
              ]
    for i in exelist:
        pyfile.write(i + "\n")
    for i in results:
        pyfile.write(i + "\n")
    for i in results_list:
        pyfile.write('print("'+i+' = " + str(float('+i+')), file=textfile)\n')
    pyfile.write('textfile.close()\n')
    pyfile.close()
    import os
    os.system("python tmp.py")
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

# def solve_and_print_results(equations, exelist, results_list):
#     print("\nEntered Equations: \n")
#     for i in equations:
#         print(i)
#     print("\nResults: \n")
#     for i in exelist:
#         exec(i)
#     return

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
    print(printed_output)