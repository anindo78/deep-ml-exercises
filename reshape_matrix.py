import numpy as np

a = a = [[1,2,3,4],[5,6,7,8]]


def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's 
    # tolist() method
	'''
	Write a Python function that reshapes a given matrix into a specified shape.
	 if it cant be reshaped return back an empty list [ ]

    Example:
    Input: a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
    Output: [[1, 2], [3, 4], [5, 6], [7, 8]]
    '''
	result = []
	a2 = np.array(a).flatten()
	if len(a2) != new_shape[0]*new_shape[1]:
		result = result
	else:
		for j in range(0, len(a2), new_shape[1]): 
			result.append(a2[j:j + new_shape[1]])
	
	return result.tolist()

# test
a = [[1,2,3,4],[5,6,7,8]]
print (reshape_matrix(a, (4,2)))