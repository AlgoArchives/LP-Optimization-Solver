from scipy.optimize import linprog

# Ask the user for the optimization problem details
opt_type = input("Enter 'max' for maximization, 'min' for minimization: ")
obj_func = list(map(float, input("Enter the coefficients of the objective function, separated by spaces: ").split()))
num_constraints = int(input("Enter the number of constraints: "))

# Initialize the constraints matrix and bounds vector
constraints = []
bounds = []

# Get the constraints from the user
for i in range(num_constraints):
    constraint = list(map(float, input(f"Enter the coefficients for constraint {i+1}, separated by spaces: ").split()))
    bound = float(input(f"Enter the bound for constraint {i+1}: "))
    constraints.append(constraint)
    bounds.append(bound)

# If it's a maximization problem, we need to negate the objective function
if opt_type.lower() == 'max':
    obj_func = [-1 * i for i in obj_func]

# Solve the problem
res = linprog(c=obj_func, A_ub=constraints, b_ub=bounds, method='highs')

# If it's a maximization problem, we need to negate the result
if opt_type.lower() == 'max':
    res.fun = -1 * res.fun

print(f"The optimal value is {res.fun} at point {res.x}")