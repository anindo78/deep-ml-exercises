'''
Write a Python function called svd_2x2_singular_values(A) that finds an approximate singular value 
decomposition of a real 2 x 2 matrix using one Jacobi rotation. Input A: a NumPy array of shape (2, 2)

Rules You may use basic NumPy operations (matrix multiplication, transpose, element wise math, etc.). 
Do not call numpy.linalg.svd or any other high-level SVD routine. Stick to a single Jacobi step no 
iterative refinements.

Return A tuple (U, Î£, V_T) where U is a 2 x 2 orthogonal matrix, Î£ is a length 2 NumPy array containing
the singular values, and V_T is the transpose of the right-singular-vector matrix V.

Example:
Input: a = [[2, 1], [1, 2]]
Output: (array([[-0.70710678, -0.70710678],
                        [-0.70710678,  0.70710678]]),
        array([3., 1.]),
        array([[-0.70710678, -0.70710678],
               [-0.70710678,  0.70710678]]))

'''


import numpy as np 
def svd_2x2_singular_values(A: np.ndarray) -> tuple:

    # SVD takes any real matrix A and converts as A = U S V_T, where U and V are orthogonal (U_T*U = I)
    # S is the diagonal matrix with non zero entries called singular values

    # step1: convert A to a symmetric matrix via A_T * A
    A = np.array(A)
    A_2 = A.T @ A

    # We now need to diagonalize A_2, for that we need a rotation matrix R such that D = R_T * B * R
    # We only need one rotation to zero the off diagonal term, loop runs only once

    if (A_2[0][0] == A_2[1][1]):
        theta = np.pi / 4
    else:
        theta = (1/2) * np.arctan((2 * A_2[0][1]) / (A_2[0][0] - A_2[1][1]))
    
    # build rotation matrix
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

    # creating the diagonal matrix
    D = np.array(R.T @ (A_2 @ R))  # This should be a diagonal matrix

    # extracting singular values. The entities of D are eigen values of A_2. Singular values are their sq. root
    S = np.array([np.sqrt(D[0, 0]), np.sqrt(D[1, 1])])
    sorted_S_ascending = np.sort(S)

    # Reverse the sorted array to get descending order
    sorted_S_descending = sorted_S_ascending[::-1]


    # building U now. U = A * V * S_inv. V is equal to R
    S_inv = np.diag(1.0 / sorted_S_descending)

    U = np.array(A @ (R @ S_inv))

    return (U, S, R.T)




a = [[1, 2], [3, 4]]
print(svd_2x2_singular_values(a))



