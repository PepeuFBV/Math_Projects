import numpy as np
from Pivoting.pivoting_method import pivoting_method as solve_pm
from LU.lu_method import lu_method as solve_lu
from LLt.llt_method import llt_method as solve_llt
from Gauss_Jacobi.gaussjacobi_method import gauss_jacobi_method as solve_gj
from Gauss_Seidel.gaussseidel_method import gauss_seidel_method as solve_gs

def main():
    # Usage
    matrix = np.array([[2, 1, -1], [4, -1, 3], [1, 3, -2]])
    solution = np.array([8, 9, 3])

    y = solve_lu(matrix, solution)
    x = solve_pm(matrix, solution)
    z = solve_llt(matrix, solution)
    w = solve_gj(matrix, solution, 100)
    v = solve_gs(matrix, solution, 100)
    while True:
        print("Chose a method to solve the system of linear equations:")
        print("1. LU Decomposition")
        print("2. Pivoting Method")
        print("3. LLt Decomposition")
        print("4. Gauss-Jacobi Method")
        print("5. Gauss-Seidel Method")
        print("6. Exit")
        choice = int(input("--> "))
        switch = {
            1: y,
            2: x,
            3: z,
            4: w,
            5: v
        }
        if choice == 6:
            break
        print(switch.get(choice, "Invalid choice"))
        
        
if __name__ == "__main__":
    main()