import Lagrange as L
import Newton as N

def main():
    print("Choose the method you want to use:")
    print("1. Lagrange")
    print("2. Newton")
    print("--> ")
    choice = int(input())
    if (choice == 1):
        L.Lagrange()
    else:
        N.Newton()
    
    
    
if __name__ == "__main__":
    main()