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
    f = open(filename, mode='r')
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
    return equations, num_line
