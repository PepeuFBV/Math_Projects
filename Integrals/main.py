import rectangles as rectangles
import trapezoids as trapezoids
from Simpsons.a_third_simple import a_third_simple
from Simpsons.a_third_repeated import a_third_repeated
from Simpsons.three_eights_simple import three_eights_simple
from Simpsons.three_eights_repeated import three_eights_repeated
from gaussian_quadrature import gaussian_quadrature
from euler_method import euler_method

def main():
    
    print("Enter the lower limit of the integral")
    a = float(input())
    print("Enter the upper limit of the integral")
    b = float(input())
    
    print("Choose a method to calculate the integral of a function")
    print("1. Rectangle method")
    print("2. Trapezoidal method")
    print("3. Simpson's 1/3 method (only 2 subintervals)")
    print("4. Simpson's 1/3 method repeated")
    print("5. Simpson's 3/8 method")
    print("6. Simpson's 3/8 method repeated")
    print("7. Gaussian Quadrature")
    print("8. Euler's Method")
    print("0. Exit")
    print("--> ")
    choice = int(input())
    
    SUBINTERVALS_PROMPT = "Enter the number of subintervals: "

    while True:
        if choice == 1:
            print(SUBINTERVALS_PROMPT)
            n = int(input())
            print(rectangles.rectangle_method(f, a, b, n))
        elif choice == 2:
            print(SUBINTERVALS_PROMPT)
            n = int(input())
            print(trapezoids.trapezoidal_method(f, a, b, n))
        elif choice == 3:
            print(a_third_simple(f, a, b))
        elif choice == 4:
            print(SUBINTERVALS_PROMPT)
            n = int(input())
            print(a_third_repeated(f, a, b, n))
        elif choice == 5:
            print(SUBINTERVALS_PROMPT)
            n = int(input())
            print(three_eights_simple(f, a, b, n))
        elif choice == 6:
            print(SUBINTERVALS_PROMPT)
            n = int(input())
            print(three_eights_repeated(f, a, b, n))
        elif choice == 7:
            print(gaussian_quadrature(f, a, b))
        elif choice == 8:
            print("Enter the initial value of x (x0)")
            x0 = float(input())
            print("Enter the initial value of y (y0)")
            y0 = float(input())
            print(SUBINTERVALS_PROMPT)
            n = int(input())
            print("Enter the step size")
            h = float(input())
            print(euler_method(f_derivative, x0, y0, h, n))            
        else:
            print("Invalid input")
        print("Choose a method to calculate the integral of a function")
        print("1. Rectangle method")
        print("2. Trapezoidal method")
        print("3. Simpson's 1/3 method (only 2 subintervals)")
        print("4. Simpson's 1/3 method repeated")
        print("5. Simpson's 3/8 method (only 3 subintervals)")
        print("6. Simpson's 3/8 method repeated")
        print("7. Gaussian Quadrature")
        print("8. Euler's Method")
        print("0. Exit")
        print("--> ")
        choice = int(input())
        if choice == 0:
            break



def f(x):
    return x

def f_derivative(x):
    return 1

if __name__ == "__main__":
    main()