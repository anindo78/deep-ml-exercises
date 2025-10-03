def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	'''
	Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function 
	should return a list containing the eigenvalues, sort values from highest to lowest.

    Example:
    Input:
    matrix = [[2, 1], [1, 2]]
    Output:  [3.0, 1.0]
	'''
	
    # formula for eigen values
	# lambda ** 2 + lambda (trace of matrix) + (determinant of matrix) = 0
	# lambda = (-trace) +- ((trace)**2  - 4*(determinant)) ** 0.5
	
	tr = float(matrix[0][0] + matrix[1][1]) # since this is a 2x2 matrix
	det = float(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
	lambda1 = ((1 * tr) + ((tr ** 2) - (4 * det)) ** (1/2))/2
	lambda2 = ((1 * tr) - ((tr ** 2) - (4 * det)) ** (1/2))/2
	eigen_values = sorted([lambda1, lambda2], reverse=True)
	return eigen_values
	
    
matrix = [[2, 1], [1, 2]]
print(calculate_eigenvalues(matrix))
	



