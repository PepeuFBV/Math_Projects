import rectangles as rectangles
import trapezoids as trapezoids

def main():
    
    print("Enter the lower limit of the integral")
    a = float(input())
    print("Enter the upper limit of the integral")
    b = float(input())
    print("Enter the number of subintervals")
    n = int(input())
    
    print("Choose a method to calculate the integral of a function")
    print("1. Rectangle method")
    print("2. Trapezoidal method")
    print("0. Exit")
    print("--> ")
    choice = int(input())

    while True:
        if choice == 1:
            print(rectangles.rectangle_method(f, a, b, n))
        elif choice == 2:
            print(trapezoids.trapezoidal_method(f, a, b, n))
        else:
            print("Invalid input")
        print("Choose a method to calculate the integral of a function")
        print("1. Rectangle method")
        print("2. Trapezoidal method")
        print("0. Exit")
        print("--> ")
        choice = int(input())
        if choice == 0:
            break



def f(x):
    return x**2

if __name__ == "__main__":
    main()