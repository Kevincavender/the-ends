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
        list of equations
    :return:
        list of variables (without copies)
        variable dict = {equation:[variables], ..}
    """
    import re
    variables = []
    variable_dict = {}
    for one_equation in equations:
        # regular expression for splitting strings with given characters
        split_equations = re.split(r"[=+\-^*/\\()\[\]]", one_equation)
        # print('split equation ->', split_equations)
        tmp_vars = []
        for i in split_equations:
            if i != '':
                if i.isnumeric() == 0 and i not in variables:
                    # if the item in list (i) is not numeric append
                    # and it's not already in the list of variables
                    # it to the variables list
                    variables.append(i)
                if i.isnumeric() == 0:
                    tmp_vars.append(i)
                    variable_dict[one_equation]=tmp_vars
    return variables, variable_dict


def equation_dict(equations):
    # split equations by the equals sign
    import re
    equation_dict = {}
    for i in equations:
        split_equations = re.split(r"[=]", i)
        equation_dict[i] = split_equations
    return equation_dict


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
            # add section for requiring an equals sign
            for i in text:
                if i in symbols_not_allowed:
                    print("Error in equation " + str(count)
                          + ": \"" + i + "\" is not an allowed character")
                    solve = False
                    # join the characters back into one equation

        output_equations.append(tmp_eqn)
    return solve


def syntax_correction(equations):
    # input of equations
    corrected_equations = []
    for i in equations:
        tmp_list2 = []
        for j in i:
            if j == "^":
                j = "**"
            # make a carrot equal to python power **
            tmp_list2.append(str(j))
        tmp_list2 = ''.join(tmp_list2)
        corrected_equations.append(tmp_list2)
    return corrected_equations
