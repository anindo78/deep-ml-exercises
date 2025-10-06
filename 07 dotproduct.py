# generate a 3 x 2 matrix
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])

# generate a vector of dimension 2
b = np.array([10,20])


# compute the dot product

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

    if len(a[0]) != len(b):
        res = [-1]
    else:
        res = [sum(i * j for i, j in zip(row, b)) for row in a]
    return res

print(matrix_dot_vector(a, b))

