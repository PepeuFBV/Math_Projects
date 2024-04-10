import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def Lagrange():
    print("How many points do you have?")
    n = int(input())
    x = []
    y = []
    for i in range(n):
        print("Enter the x value of the point", i+1)
        x.append(float(input()))
        print("Enter the f(x)/y value of the point", i+1)
        y.append(float(input()))

    print("Do you want the formula or the value of the function?")
    print("1. Formula")
    print("2. Value")
    print("3. Both")
    print("--> ")
    choice = int(input())

    X = sp.symbols('x')
    lagrange_poly = 0

    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (X - x[j]) / (x[i] - x[j])
        lagrange_poly += y[i] * p

    if choice == 1 or choice == 3:
        print("The formula is:")
        print(sp.simplify(lagrange_poly))

    if choice == 2 or choice == 3:
        print("Enter the value of x")
        x0 = float(input())
        result = lagrange_poly.subs(X, x0)
        print("The value of the function at x =", x0, "is", result)

    # Plotting
    x_vals = np.linspace(min(x), max(x), 400)
    y_vals = [lagrange_poly.subs(X, val) for val in x_vals]

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label='Lagrange Polynomial')
    plt.scatter(x, y, color='red')
    plt.title('Lagrange Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()