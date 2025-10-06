'''
Write a Python function that transforms a given matrix A using the operation T^(-1)*A*S,
where T and S are invertible matrices. The function should first validate if the matrices T and S 
are invertible, and then perform the transformation. In cases where there is no solution return -1

Example:
Input:
A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]
Output:
[[0.5,1.5],[1.5,3.5]]
'''

import numpy as np



def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

    # 1: Convert list into numpy arrays
    A = np.array(A)
    T = np.array(T)
    S = np.array(S)

    # Check for squareness and invertibilty
    is_T_invertible = (T.shape[0] == T.shape[1] and abs(np.linalg.det(T)) > 0)
    is_S_invertible = (S.shape[0] == S.shape[1] and abs(np.linalg.det(S)) > 0)

    if is_T_invertible and is_S_invertible:
        try:
            T_inv = np.linalg.inv(T)
            result = T_inv @ A @ S
            return result.tolist()
        except np.linalg.LinAlgError:
            return -1
    else:
        return -1
    
# Example Run:
A = [[1, 2], [3, 4]]
T = [[2, 0], [0, 2]]
S = [[1, 1], [0, 1]]

print(transform_matrix(A, T, S))
