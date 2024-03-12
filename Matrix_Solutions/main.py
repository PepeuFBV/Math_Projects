import numpy as np
from Pivoting.pivoting_method import pivoting_method as solve_pm
from LU.lu_method import lu_method as solve_lu
from LLt.llt_method import llt_method as solve_llt
from Gauss_Jacobi.gaussjacobi_method import gauss_jacobi_method as solve_gj
from Gauss_Seidel.gaussseidel_method import gauss_seidel_method as solve_gs
from norms import calculate_euclidian_norm, calculate_max_norm, calculate_frobenius_norm, calculate_infinity_norm, calculate_row_norm, calculate_column_norm
import time


def get_norm_choice():
    print("Chose a norm to calculate:")
    print("1. Euclidian Norm")
    print("2. Max Norm")
    print("3. Frobenius Norm")
    print("4. Infinity Norm")
    print("5. Row Norm")
    print("6. Column Norm")
    choice = int(input("--> "))
    
    if choice == 1:
        return calculate_euclidian_norm
    elif choice == 2:
        return calculate_max_norm
    elif choice == 3:
        return calculate_frobenius_norm
    elif choice == 4:
        return calculate_infinity_norm
    elif choice == 5:
        return calculate_row_norm
    elif choice == 6:
        return calculate_column_norm
    

def main():
    # Usage
    matrix = np.array([[4,2,1],[2,1,3],[2,3,1]])
    solution = np.array([1, 2, 3])
    
    while True:
        print("Chose a method to solve the system of linear equations:")
        print("1. LU Decomposition")
        print("2. Pivoting Method")
        print("3. LLt Decomposition")
        print("4. Gauss-Jacobi Method")
        print("5. Gauss-Seidel Method")
        print("6. Exit")
        choice = int(input("--> "))

        if choice == 6:
            break

        start_time = time.perf_counter()

        if choice == 1:
            result = solve_lu(matrix, solution)
        elif choice == 2:
            result = solve_pm(matrix, solution)
        elif choice == 3:
            result = solve_llt(matrix, solution)
        elif choice == 4:
            norm = get_norm_choice()
            result = solve_gj(matrix, solution, 100, norm, 0.0001)
        elif choice == 5:
            norm = get_norm_choice()
            result = solve_gs(matrix, solution, 100, norm, 0.0001)
        else:
            print("Invalid choice")
            continue

        end_time = time.perf_counter()
        execution_time = end_time - start_time

        if choice in [4, 5]:
            result, iterations = result
            print("Result:", result)
            print("Iterations:", iterations)
        else:
            print("Result:", result)
        print("Execution time:", execution_time, "seconds")

if __name__ == "__main__":
    main()