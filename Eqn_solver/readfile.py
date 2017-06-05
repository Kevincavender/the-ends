def readfile(filename):
    '''
    :param 
    filename: 
        input is a text file for input
    :return: 
    Equations: 
        lines with potential equations on them
    num_line:
        number of equation lines
    '''
    # open file
    with open(filename, mode='r') as f:
        line_list = []
        # read in lines
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            line_list.append(line)
    outstring = "".join(list(filter(None, line_list)))
    return outstring


def readstring(input_string):
    '''
    :param 
    filename: 
        input is a text file for input
    :return: 
    Equations: 
        lines with potential equations on them
    num_line:
        number of equation lines
    '''

    num_line = 0
    # read in lines
    equations = []
    line_list = input_string.split("\n")
    for line in line_list:
        num_line += 1
        # go through each line in equations
        # and append non-empty lines
        equations.append(line)
    equations = list(filter(None, equations))
    return [equations, num_line]

if __name__ == "__main__":
    print(readfile("1eqn"))
    input_str = 'x4 = a + b+c+d+f+x3^2\na = 2\nb = 5\n' \
                'c = 4\ne = 4+f\nf = b\ng = b\nd = c + e\n' \
                'x1 = 20\nx2 = x1+3\nx3 = x2 -10\n'
    print(readstring(input_str))
