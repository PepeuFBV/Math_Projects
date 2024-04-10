import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def Newton():
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
    newton_poly = 0
    div_diff = y.copy()

    for i in range(n):
        term = div_diff[i]
        for j in range(i):
            term *= (X - x[j])
        newton_poly += term
        for j in range(n - i - 1):
            div_diff[j] = (div_diff[j + 1] - div_diff[j]) / (x[j + i + 1] - x[j])

    if choice == 1 or choice == 3:
        print("The formula is:")
        print(sp.simplify(newton_poly))

    if choice == 2 or choice == 3:
        print("Enter the value of x")
        x0 = float(input())
        result = newton_poly.subs(X, x0)
        print("The value of the function at x =", x0, "is", result)

    # Plotting
    x_vals = np.linspace(min(x), max(x), 400)
    y_vals = [newton_poly.subs(X, val) for val in x_vals]

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label='Newton Polynomial')
    plt.scatter(x, y, color='red')
    plt.title('Newton Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()