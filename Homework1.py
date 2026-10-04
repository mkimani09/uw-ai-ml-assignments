import numpy as np

def f(x):
    return x*np.sin(3*x) - np.exp(x)

def df(x):
    return np.sin(3*x) + 3*x*np.cos(3*x) - np.exp(x)

tol = 1e-6

#Exercise 1–1: - Newton - A1
x = -1.6
xs = [x]
while abs(f(x)) >= tol:
    x = x - f(x)/df(x)
    xs.append(x)
x = x - f(x)/df(x)  
xs.append(x)

A1 = np.array(xs)
n_newton = len(xs) - 1

#Exercise 1–1: - bisection - A2
a, b = -0.7, -0.4
mid = (a + b)/2
mids = [mid]
while abs(f(mid)) >= tol:
    if f(a)*f(mid) < 0:
        b = mid
    else:
        a = mid
    mid = (a + b)/2
    mids.append(mid)

A2 = np.array(mids)
n_bisect = len(mids)

#Exercise 1–1: - part 3 (A3)
A3 = np.array([n_newton, n_bisect])

#Exercise 1–2:
A = np.array([[1, 2], [-1, 1]])
B = np.array([[2, 0], [0, 2]])
C = np.array([[2, 0, -3], [0, 0, -1]])
D = np.array([[1, 2], [2, 3], [-1, 0]])
y = np.array([0, 1])
z = np.array([1, 2, -1])

#Exercise 1–2: A4
A4 = D @ y + z 

#Exercise 1–2: A5
A5 = A @ B

#Exercise 1–2: A6
A6 = B @ C

#Exercise 1–2: A7
A7 = C @ D

print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)