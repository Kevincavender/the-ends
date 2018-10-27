# the-ends
THermodynamic Engineering Equations NeeD Solving

## How to use it

Written and test only in python 3.6

### Ubuntu or other linuxy OS's:

pip3 install the-ends

python3 -m the_ends <your_textfile_with_equations>

## Description
This is a side project for me as a cryo-mechanical engineer, i enjoy coding and problem solving. However i frequently desire a rapid numerical solution that simply can't be done currently without involving 3D FEA solutions. Those also don't do thermal system modeling. Integrating property libraries (fluid properties, heat transfer correlations, solid properties) has been the challange with other programming type solutions (Mathcad, matlab, python, C++, etc.) the problem lies in that it is not a simple task to sit down and model a thermal system like you would in CAD. The software packages that come close that i know of are EES (engineering equation solver) and maybe GFSSP (General Fluid Simulation Software Package?). These are not well known and not taught at many schools. I hope to solve these problems, creating an open sourced equation solver to allow an easier time modeling thermal systems. (or any system of equations for that matter). 

## Work in progress
Working on open-sourced equation solver for the needs of a Thermo based Mechanical Engineer.
Though this could be utilized by any kind.



The initial module is an explicit numerical equations solver (Eqn_solver) and will eventually be built out to include the packages listed below (subject to change).

## Install info
currently developing in Python 3.6. This is the only version currently semi-guaranteed to work.


## future libraries to integrate
### UNITS
#[Pint](https://github.com/hgrecco/pint)
 OR
#[Quantities](https://github.com/python-quantities/python-quantities)

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

### LaTex 
    :format equations

### GUI
    :start with Tkinter and move to PyQt

### version control for equation users files
    :duh

### testing suite, py.test
    :for testing all the things
    https://docs.pytest.org/en/latest/

### travis CI
    :continuous integration


