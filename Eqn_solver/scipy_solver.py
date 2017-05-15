from scipy.optimize import fsolve

# Define the expression whose roots we want to find
# take in an equation that can't be executed by mpmath

a = 0.5
b = 1
c = 3
R = 1.7

# func = lambda tau : R - ((1.0 - np.exp(-tau))/(1.0 - np.exp(-a*tau)))
func = lambda c : c**2 - (a**2 + b**2)

# Use the numerical solver to find the roots

tau_initial_guess = 5
tau_solution = fsolve(func, tau_initial_guess)

print ("The solution is tau = %f" % tau_solution)
print ("at which the value of the expression is %f" % func(tau_solution))