# Linear Programming Optimization Solver

This Python script uses the `linprog` function from `scipy.optimize` to solve linear programming optimization problems. It allows users to input the type of optimization (maximization or minimization), coefficients of the objective function, number of constraints, coefficients for each constraint, and their bounds. It then calculates and displays the optimal value and corresponding point.

## Requirements

- Python 3.x
- scipy

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Vikranth3140/optimizer.git
```

2.  Navigate to the project directory:

```bash
cd optimizer
```

3.  Install the required dependencies:

```bash
pip install -r requirements.txt
```

4.  Run the script:

```bash
python optimizer.py
```

5.  Follow the prompts to input the optimization problem details as instructed.

Example
-------

Here's an example of how to use the script:

*   Maximize: `3x + 2y`
*   Subject to constraints:
    *   `x + y <= 4`
    *   `2x + y <= 5`
    *   `x >= 0`, `y >= 0`

The script will calculate the optimal value and point that maximizes the objective function under these constraints.

License
-------

This project is licensed under the [MIT License](LICENSE).