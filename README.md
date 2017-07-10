# the-ends
THermodynamic Engineering Equations NeeD Solving

## Work in progress
Working on open-sourced equation solver for the needs of a Thermo-Fluids Mechanical Engineer. 
The initial module is an explicit numerical equations solver (Eqn_solver) and will eventually be built out to include the packages listed below (subject to change).

## Install info
currently developing in Python 3.6. This is the only version currently semi-guaranteed to work.


## future libraries to integrate
### [Pint](https://github.com/hgrecco/pint)
    for unit checking and conversion

### [Uncertainties](https://github.com/lebigot/uncertainties/)
    for calculating and propogating uncertainties
    
### [zunzun3](https://github.com/zunzun/pyeq3)
    for curve fitting
    
### [CoolProp](https://github.com/CoolProp/CoolProp)
    :thermodynamic properties (open-source)
    http://coolprop.sourceforge.net/

### [Refprop](https://www.nist.gov/srd/refprop)
    :integrated most up to date thermodynamic equations of state

### Numpy
    :hard maths and arrays
    
### scipy
    :hard maths

### matplotlib
    :plotting stuff

### GUI
    :start with Tkinter and move to PyQt if nessesary

### version control for equation users files
    :likely some kind of github/git compatibility

### testing suite, py.test
    :for testing all the things
    https://docs.pytest.org/en/latest/

### travis CI
    :continuous integration
