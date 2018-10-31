import re

'''
Notes from Last Sev Update:
    -Parenthese checking portion is used for the index so unless the error checking thing returns those I need that part
    -We should look at what should be done with the integrated functions. As it is they will just be treated as variables and their variables will not be noted
# TODO .... Maybe.....

-run the_ends_test >>> FunctionsUnitTest.py
    >>> This will help us refine the functionality of this as we progress. 
        Makes is a pass/fail condition for whether things are as we both expect them to act.
    
Functions initially to be integrated:
SQRT()
    square root (obvious function)
ABS()
    absolute value (again, obvious)

2018-10-26 Kevin added Notes 
'''

integrated_functions_list = ['SQRT','ABS']


def function_finder(equ, debug=False):
    """
    Finds all functions and how many within a single string
    Define name for each function and create a returnable list of names
    """

    equ = equ.replace(' ', '')


    fun_list = re.findall(r'\w+\(', equ, flags=0)
    number_of_functions_ = len(fun_list)

    if number_of_functions_ == 0:
        return [], []  # might want to change this depending on other functions

    #removes trailing parenthese and removes from the list any function on the integrated function list.
    #Add more here if you want to do something specific with them...
    #Other wise they will appear as any other variable in a dictionary
    for i in range(number_of_functions_):
        fun_list[i] = fun_list[i][:-1]
        if fun_list[i] in integrated_functions_list:
            fun_list.remove(i)

    number_of_functions_ = len(fun_list)
    
    # figure out index of each open and close parentheses

    # figures out indexes of all parentheses
    parentheses_ranges = {}  # soon to be filled dictionary of ranges
    # .................................................................
    # TODO Replace this section with EquationErrorCheck.EquationErrorCheck()
    # we can replace if you want to make the parentheses_ranges a returnable for the equation checking function
    hold = []  #
    for i, c in enumerate(equ):
        if c == '(':
            hold.append(i)
        if c == ')':
            try:
                parentheses_ranges[hold.pop()] = i
            except IndexError:
                print('Syntax Error: Too many closing parentheses')
                raise
    if hold:  # check if stack is empty afterwards
        # print('Syntax Error: Too many opening parentheses')
        raise SyntaxError

    start_list = [] #starting points for function variable ranges
    function_ranges = []  # indices of only the functions
    for k in range(number_of_functions):
        start_list.append(re.search(re.escape(fun_list[k]), equ).end())
        function_ranges.append((start_list[k], parentheses_ranges[start_list[k]]))

    # extract string, parse and return a dictionary of variables for each function
    variable_dictionary_list = []  # returned list of dictionaries
    for n in range(number_of_functions):
        extracted_string = equ[function_ranges[n][0] + 1:function_ranges[n][1]]  # extracts string


        # if statement about functions inside functions. remove to make good program
        # why are you looping to find errors?
        for m in range(number_of_functions):
            if fun_list[m] in extracted_string:
                print('Syntax Error: Nested Non-Integrated Function')
                raise SyntaxError

        #parses variables
        extracted_strings = re.split(r",\s*(?![^()]*\))",extracted_string)#vodo magic that dosn't split on commas between parentheses
        extracted_strings[0] = extracted_strings[0].split(r'=') #deals with x=x
        try:
            extracted_strings[0] = extracted_strings[0][0] #removes string within string, try stops python from dying...
        
        # creates a dictionary out of the extracted string
        var_dictionary = {}
        for b in range(len(extracted_strings)):
            var_dictionary[b + 1] = extracted_strings[b]

        variable_dictionary_list.append(var_dictionary)

    if debug is True:
        print("DEBUG: Functions.py")
        print("Input string: " + equ)
        print('functions ranges: ' + function_ranges)
        print('start list: ' + start_list)
        print('parentheses ranges: ' + parentheses_ranges)
        print('function ranges: ' + function_ranges)
        print("\nOutput: ")
    
    return fun_list, variable_dictionary_list


if __name__ == "__main__":
    print("\nTesting Functions.py.......\n")
    equ = 'x=2*5+function1(( x=x, 5/4, 12^(2-1)), 8) * function2(y, 7, 11*(y-3))'
    print(function_finder(equ, debug=True))

