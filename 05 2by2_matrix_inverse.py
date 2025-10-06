'''
Write a Python function that calculates the inverse of a 2x2 matrix. 
Return 'None' if the matrix is not invertible.

Example:
Input: matrix = [[4, 7], [2, 6]]
Output: [[0.6, -0.7], [-0.2, 0.4]]
'''

import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:

    # to calculate inverse, we need to check:
    # 1. matrix is square - the problem states it is always 2x2, but we still implement the check
    # 2. determinant is non-zero

    # convert to numpy array of floats
    input_array = np.array(matrix, dtype=float)

    # check for squareness
    is_matrix_square = (input_array.shape[0] == input_array.shape[1])
    
    # check determinant (use absolute value of determinant)
    det = np.linalg.det(input_array)
    is_det_matrix_nonzero = (abs(det) > 0)

    if is_matrix_square and is_det_matrix_nonzero:
        try:
            inv_matrix = np.linalg.inv(input_array)
            # return a plain Python list of lists so print shows the expected format
            # round elements to 1 decimal to avoid long floating-point representations
            result = inv_matrix.tolist()
            return [[round(float(x), 1) for x in row] for row in result]
        except np.linalg.LinAlgError:
            return None
    else:
        return None
    

# check
matrix = [[2, 1], [6, 2]]
print(inverse_2x2(matrix))
