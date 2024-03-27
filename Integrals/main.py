import rectangles as rectangles
import trapezoids as trapezoids
from Simpsons.a_third_simple import a_third_simple
from Simpsons.a_third_repeated import a_third_repeated
from Simpsons.three_eights_simple import three_eights_simple
from Simpsons.three_eights_repeated import three_eights_repeated
from gaussian_quadrature import gaussian_quadrature

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
    print("0. Exit")
    print("--> ")
    choice = int(input())
    
    SUBINTERVALS_PROMPT = "Enter the number of subintervals"

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
        print("0. Exit")
        print("--> ")
        choice = int(input())
        if choice == 0:
            break



def f(x):
    return x

if __name__ == "__main__":
    main()