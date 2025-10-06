'''
Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b. 
The function should iterate n times, rounding each intermediate solution to four decimal places, 
and return the approximate solution x.

Example:
Input: A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]], b = [-1, 2, 3], n=2
Output: [0.146, 0.2032, -0.5175]
'''

import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:

    # steps to solve the system of equations given by Ax = B
    # 1) start with initial guess of x
    # 2) iterate for each equation, update xi as = 1/aii (bi - sigma<j!=i> aij*xj)
    #    where aii are diagonal elements of A and aij are off diagonal
    # 3) repeat iterations till changes in x are less than a certain tolerance or run max. iterations

    # set tolerance
    # tolerance = 1e-10 # not using for now

    # set initial guess
    x = np.zeros_like(b)   # you can change this to anything. let's see how this changes results later



    # find diagonal and its inverse
    diag_elements = np.diag(A)

    # inverse of diagonal
    diag_inverse = np.diag(1 / diag_elements)

    # find the non diagonal matrix 

    #  - first create a matrix with just the diagonal elements in it
    D = np.diag(diag_elements)

    #  - then create the non diagonal matrix by subtracting D from A
    non_diag_matrix = A - D

    for _ in range(n):
        x = diag_inverse @ (b - non_diag_matrix @ x)

    return np.round(x, decimals=4)


A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b = np.array([-1, 2, 3])
n = 2

print(solve_jacobi(A, b, n))