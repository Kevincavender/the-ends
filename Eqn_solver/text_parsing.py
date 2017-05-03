def preprocess_equations(equations):
    """
this block of text describes the function
also called a docstring
the purpose of this function is to take the list of equations,
remove spaces and uppercase all characters

example input
[['x = y+ 1'], ['y = 2'], ['squ = 2'], ['yo = 20']]
example output
['X=Y+1', 'Y=2', 'SQU=2', 'YO=20']
*************************
:future use:
semicolon ; shall denote new line

    """
    solve = True
    count = 0
    tmp_eqn = []
    output_equations = []
    symbols_not_allowed = ['?','@','&','`','~','#','!','$']
    for one_equation in equations:
        # list containing one string
        for text in one_equation:
            # string containing an equation
            tmp_letter = []
            for i in text:
                if i in symbols_not_allowed:
                    print("Error: \"" + i + "\" is not an allowed character")
                    solve = False
                # single character/num/operator
                # if the character is not a space
                if i.isspace() == 0:
                    # capitalize all characters and add them to list
                    tmp_letter.append(i.upper())
            # join the characters back into one equation
            tmp_eqn = ''.join(tmp_letter)
        output_equations.append(tmp_eqn)
    return output_equations, solve


def collect_variables(equations):
    """
    split equations by the '=' operator
    store in list for processing
    :param equations:
    :return:
    """
    variables = []
    for one_equation in equations:
        # regular expression for splitting strings with given characters
        split_equations = re.split(r'=|\+|-|\^|\*|/|\\', one_equation)
        # print('split equation ->', split_equations)
        for i in split_equations:

            if i.isnumeric() == 0 and i not in variables:
                # if the item in list (i) is not numeric append
                # and it's not already in the list of variables
                # it to the variables list
                variables.append(i)
    return variables


def parse_known_equations(equations):
    # reorder equations so that python can order them properly
    print(equations)
    for line in equations:
        # for a single equation
        for var in variables:
            if var in line:
                #print(var)
                var = 0
    return


import re
# open file
f = open('1eqn', mode='r')
num_line = 0
line_list = []
# read in lines
while True:
    line = f.readline()
    if len(line) == 0:
        break
    num_line += 1
    line_list.append([line])
f.close()
# close file

# split lines in code
equations = []
num_line = 0
for line in line_list:
    # go through each line in equations
    # and append non-empty lines
    eqin = line[0].splitlines()
    if eqin != ['']:
        # only if line is not empty
        equations.append(eqin)
        num_line += 1

# collect variables
equations, solve = preprocess_equations(equations)
if solve == True:
    variables = collect_variables(equations)
    parse_known_equations(equations)
else:
    print("solver cannot continue")

# printing output for debuging

# print('\n', equations)
# print('\n', equations2)
'''

if solve == 1:
    print('\n********************************')
    print('Number of Equations = ', num_line)
    print('Number of Variables = ', len(variables))
    print('List of Variables', ', '.join(variables))


    '''
