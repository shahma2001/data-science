import numpy as np

def get_square_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    print(f"Enter the {n*n} elements row-wise:")
    elements = list(map(float, input().split()))
    if len(elements) != n * n:
        raise ValueError("Incorrect number of elements provided.")
    matrix = np.array(elements).reshape(n, n)
    return matrix


try:
    A = get_square_matrix()
    print("\nOriginal Matrix A:\n", A)

   
    U, S, VT = np.linalg.svd(A)
    print("\nMatrix U:\n", U)
    print("\nSingular Values (as vector):\n", S)
    print("\nMatrix VT (transpose of V):\n", VT)

    
    S_matrix = np.zeros_like(A, dtype=float)
    np.fill_diagonal(S_matrix, S)

    
    A_reconstructed = U @ S_matrix @ VT
    print("\nReconstructed Matrix A:\n", A_reconstructed)

    
    if np.allclose(A, A_reconstructed):
        print("\n✅ Reconstruction is accurate.")
    else:
        print("\n❌ Reconstruction is not accurate.")

except Exception as e:
    print("Error:", e)

