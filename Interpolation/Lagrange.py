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
    if (choice == 1):
        print("The formula is:")
        for i in range(n):
            p = ""
            for j in range(n):
                if (i != j):
                    p += "(x - " + str(x[j]) + ")/(" + str(x[i]) + " - " + str(x[j]) + ")"
            print(str(y[i]) + " * " + p)
    elif (choice == 2):
        print("The formula is:")
        for i in range(n):
            p = ""
            for j in range(n):
                if (i != j):
                    p += "(x - " + str(x[j]) + ")/(" + str(x[i]) + " - " + str(x[j]) + ")"
            print(str(y[i]) + " * " + p)
            
        print("Enter the value of x")
        x0 = float(input())
        result = 0
        for i in range(n):
            p = 1
            for j in range(n):
                if (i != j):
                    p *= (x0 - x[j])/(x[i] - x[j])
            result += y[i] * p
        print("The value of the function at x =", x0, "is", result)
        
    else:
        print("Enter the value of x")
        x0 = float(input())
        result = 0
        for i in range(n):
            p = 1
            for j in range(n):
                if (i != j):
                    p *= (x0 - x[j])/(x[i] - x[j])
            result += y[i] * p
        print("The value of the function at x =", x0, "is", result)