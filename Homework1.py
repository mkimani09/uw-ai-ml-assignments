
import numpy as np


# ---- Problem 1, Part 1: Newton (A1) ----
# 1. Define the main function f(x)
def f(x):
    return x * np.sin(3 * x) - np.exp(x)


# 2. Define the derivative function df(x)
def df(x):
    return np.sin(3 * x) + 3 * x * np.cos(3 * x) - np.exp(x)


# 3. Set up the starting values
x = -1.6  # Our initial guess
tol = 1e-6  # Tolerance (how close to zero we want to get)
history = [x]  # A list to keep track of our guesses

# 4. Run the Newton's Method loop
while abs(f(x)) >= tol:
    # Newton's formula: next x = current x - ( f(x) / f'(x) )
    x = x - (f(x) / df(x))
    history.append(x)  # Save the new guess to our list

# The loop stops once f(x_n) is small enough. Following the PDF's note
# (check f(x_n), not f(x_{n+1})), x_{n+1} is still computed and saved.
x = x - (f(x) / df(x))
history.append(x)

# 5. Convert the final history list into a NumPy array
A1 = np.array(history)
newton_iterations = len(history) - 1  # every value after the initial guess is one iteration

print(A1)
print("Iterations:", newton_iterations)
print("Approximate root:", A1[-1])

#np.save("engr510-assignments/HW1/A1.npy", A1)


# ---- Problem 1, Part 2: Bisection (A2) ----
# The function whose root we want to find
def f(x):
    return x * np.sin(3 * x) - np.exp(x)

# Starting interval
a = -0.7
b = -0.4
tol = 1e-6

# Start with the first midpoint
mid = (a + b) / 2
history = [mid]

# Keep narrowing the interval until f(mid) is close enough to zero
while abs(f(mid)) >= tol:
    if f(a) * f(mid) < 0:
        b = mid
    else:
        a = mid

    mid = (a + b) / 2
    history.append(mid)

# Save all the midpoints as A2
A2 = np.array(history)
bisection_iterations = len(history)  # each midpoint is one iteration

print("Bisection guesses:", A2)
print("Iterations:", bisection_iterations)
print("Approximate root:", A2[-1])

#np.save("engr510-assignments/HW1/A2.npy", A2)

# ---- Problem 1, Part 3: Iteration counts (A3) ----
A3 = np.array([newton_iterations, bisection_iterations])

print("A3:", A3)
