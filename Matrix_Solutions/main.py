import numpy as np
from Pivoting.pivoting_method import pivoting_method as solve_pm
from LU.lu_method import lu_method as solve_lu
from LLt.llt_method import llt_method as solve_llt
from Gauss_Jacobi.gaussjacobi_method import gauss_jacobi_method as solve_gj
from Gauss_Seidel.gaussseidel_method import gauss_seidel_method as solve_gs
import time

def main():
    # Usage
    matrix = np.array([[4, -1, 2],[-1, 5, -3],[2, -3, 6]])
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
            result = solve_gj(matrix, solution, 100)
        elif choice == 5:
            result = solve_gs(matrix, solution, 100)
        else:
            print("Invalid choice")
            continue

        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print("Result:", result)
        print("Execution time:", execution_time, "seconds")

if __name__ == "__main__":
    main()