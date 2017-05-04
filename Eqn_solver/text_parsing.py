def preprocess_equations(equations):
    """
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
    count = 0
    tmp_eqn = []
    output_equations = []
    for one_equation in equations:
        # list containing one string
        for text in one_equation:
            # string containing an equation
            tmp_letter = []
            for i in text:
                # single character/num/operator
                # if the character is not a space
                if i.isspace() == 0:
                    # capitalize all characters and add them to list
                    tmp_letter.append(i.upper())
            # join the characters back into one equation
            tmp_eqn = ''.join(tmp_letter)
        output_equations.append(tmp_eqn)
    return output_equations


def collect_variables(equations):
    """
    split equations by the '=' operator
    store in list for processing
    :param equations:
    :return:
    """
    import re
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
    variables = collect_variables(equations)
    print(equations)
    for line in equations:
        # print("line:" + line)
        # for a single equation
        for var in variables:
            # print("var: " + var)
            if var is line:
                print(var)
                var = 0
    return


def syntax_checking(equations):
    '''
    :param equations: 
        list of equations 
    :return:
        boolean for passing syntax check
    '''
    solve = True  # indication for no errors in preprocessing
    count = 0
    tmp_eqn = []
    output_equations = []
    symbols_not_allowed = ['?', '@', '&', '`', '~', '#', '!', '$']
    for one_equation in equations:
        # list containing one string
        for text in one_equation:
            # string containing an equation
            count += 1
            tmp_letter = []
            for i in text:
                if i in symbols_not_allowed:
                    print("Error in equation " + str(count)
                          + ": \"" + i + "\" is not an allowed character")
                    solve = False
                    # join the characters back into one equation
        output_equations.append(tmp_eqn)
    return solve
