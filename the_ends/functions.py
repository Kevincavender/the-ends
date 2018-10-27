import re

'''
function identifies functions being called and creates a dictionary of variables
references a list of functions to determine if integrated function is allowed
'''


'''
ToDO.... Maybe.....

-determine if a variable of a function is a unlisted function???
-create a full program break for the related syntax errors
-replace .append method with marginally faster numpy.zeros() method
'''
integrated_fun_list = ('sqrt','integ','deriv','factorial')
#what if there is a space after the function name

def function_finder(equ):

  #removes spaces for better configuring. might be obsolete
  equ = equ.replace(' ','')
  
  #Finds all functions and how many
  #Define name for each function and create a returnable list of names
  fun_list1 = re.findall( r'\w+\(',equ, flags =0)
  number_of_functions = len(fun_list1)


  if number_of_functions == 0:
    return [],[] #might want to change this depending on other functions
  
  fun_list = []
  for i in range(number_of_functions):
    fun_list.append(fun_list1[i][:-1])

  #figure out index of each open and close parentheses
  #start of variable space
  start_list = []
  for j in range(number_of_functions):
    start_list.append(re.search(re.escape(fun_list[j]),equ).end())

  #figures out indexes of all parentheses
  parenthese_ranges = {} #soon to be filled dictionary of ranges
  hold = []
  for i, c in enumerate(equ):
    if c == '(':
         hold.append(i)
    if c == ')':
        try:
            parenthese_ranges[hold.pop()] = i
        except IndexError:
            raise SyntaxError('Too many closing parentheses')

  if hold:  # check if stack is empty afterwards
    raise SyntaxError('Too many opening parentheses')

  function_ranges = []#indecies of only the functions
  for k in range(number_of_functions):
    function_ranges.append((start_list[k],parenthese_ranges[start_list[k]]))

  #extract string, parse and return a dictionary of variables for each function
  variable_dictionary_list = [] #returned list of dictionaries
  for n in range(number_of_functions):
    extracted_string = equ[function_ranges[n][0]+1:function_ranges[n][1]] #extracts string

    #if statment about functions inside functions. Raises error is a non pre ordained function is within a function
    for m in range(number_of_functions):
      if fun_list[m] in integrated_fun_list:
        fun_list.remove(fun_list[m])

      if fun_list[m] in extracted_string:
        raise SyntaxError('Nested Non-integrated Function')
      
    extracted_strings = re.split(r'[=\\\,[^(.)]]', extracted_string)#will be problem if you want nested functions
    #deals with x=x issue
    if len(extracted_strings) > 1:
      if extracted_strings[0] == extracted_strings[1]:
        extracted_strings.pop(0)
    #creates a dictionary out of the extracted string
    var_dictionary = {}
    for b in range(len(extracted_strings)):
      var_dictionary[b+1] = extracted_strings[b]

    variable_dictionary_list.append(var_dictionary)

    
  #return values
  return(fun_list, variable_dictionary_list)



#I jumped down the rabbit hole of test cases but I want to
#be sure on what you are looking for before going crazy
#so I just did something

if __name__ == "__main__":
  equ = 'x=2*5+function1 ( x=x, 5/4, 12^(2-1), 8) * function2(y, 7, 11*(y-3))'
  print(function_finder(equ))
