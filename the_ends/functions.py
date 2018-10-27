import re

'''
Write function to identify functions being called

example syntax:?

separate "function("

from:

"x=2*5+function(x=x, 5, 12^(2-1))"

example output (Updated 10/26/2018):

return {'function_name': 'function', 1:"x", 2: "5", 3: "12^(2-1)"}

write as a python function with a single line string as the input

Include a test case at bottom:

2018-10-22
Kevin Cavender
Instructions for Sev on requested python function

# TODO .... Maybe.....

-determine if a variable of a function is a unlisted function???
    >>> yes, but first is adding a single function SQRT? and integrating it into everything else
-create a full program break for the related syntax errors
    >>>This will be pushed more to the future
-replace .append method with marginally faster numpy.zeros() method
    >>>staying with python standard library wherever possible (re is included in this) 
    
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


def function_finder(equ, debug=False):
    """
  Finds all functions and how many within a single string
  Define name for each function and create a returnable list of names
  """
    fun_list1 = re.findall(r'\w+\(', equ, flags=0)
    number_of_functions = len(fun_list1)

    if number_of_functions == 0:
        return [], []  # might want to change this depending on other functions

    fun_list = []
    for i in range(number_of_functions):
        fun_list.append(fun_list1[i][:-1])

    # figure out index of each open and close parentheses
    # start of variable space
    start_list = []
    for j in range(number_of_functions):
        start_list.append(re.search(re.escape(fun_list[j]), equ).end())
        # TODO can these be combine to limit the number of looping sections?

    # figures out indexes of all parentheses
    parentheses_ranges = {}  # soon to be filled dictionary of ranges
    # .................................................................
    # TODO Replace this section with EquationErrorCheck.EquationErrorCheck()
    # Should be good practice dealing with multiple files
    # ____________________________________________________________
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
    # ..................................................................
    function_ranges = []  # indices of only the functions
    for k in range(number_of_functions):
        function_ranges.append((start_list[k], parentheses_ranges[start_list[k]]))

    # extract string, parse and return a dictionary of variables for each function
    variable_dictionary_list = []  # returned list of dictionaries
    for n in range(number_of_functions):
        extracted_string = equ[function_ranges[n][0] + 1:function_ranges[n][1]]  # extracts string

        # removes spaces. might be obsolete
        # will already be done
        # TODO remove this, it should be done before the string gets to this function
        # extracted_string = og_string.replace(' ', '')

        # if statement about functions inside functions. remove to make good program
        # why are you looping to find errors?
        for m in range(number_of_functions):
            if fun_list[m] in extracted_string:
                print('Syntax Error: Nested Function')
                raise SyntaxError
                # add something to kill everything
                # raise SyntaxError will kill everything and tell the user there is a syntax error
                pass

        extracted_strings = re.split(r"[=\\,]", extracted_string)  # will be problem if you want nested functions
        # deals with x=x issue
        if extracted_strings[0] == extracted_strings[1]:
            extracted_strings.pop(0)
        # creates a dictionary out of the extracted string
        var_dictionary = {}
        for b in range(len(extracted_strings)):
            var_dictionary[b + 1] = extracted_strings[b]

        variable_dictionary_list.append(var_dictionary)

    if debug is True:
        # TODO Make debug here much more detailed printout
        print("DEBUG: Functions.py")
        print("Input string: " + equ)
        print(function_ranges)
        print(fun_list)
        print(fun_list1)
        print("\nOutput: \n")
    # return values
    return fun_list, variable_dictionary_list


if __name__ == "__main__":
    print("\nTesting Functions.py.......\n")
    # I jumped down the rabbit hole of test cases but I want to
    # be sure on what you are looking for before going crazy
    # so I just did something simple
    equ = 'x=2*5+function1(( x=x, 5/4, 12^(2-1)), 8) * function2(y, 7, 11*(y-3))'
    print(function_finder(equ, debug=True))
