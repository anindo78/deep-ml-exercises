'''
Write a Python function that computes the transpose of a given matrix.
a = [[1,2,3],[4,5,6]] - 2 x 3
output = [[1,4],[2,5],[3,6]] - 3 x 2

The transpose of a matrix is obtained by flipping rows and columns.
'''

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    This function takes a n dimensional matrix and returns it's transpose
    arg: a = [[1,2,3],[4,5,6]] - 2 x 3
    Output: = [[1,4],[2,5],[3,6]] - 3 x 2
    """

    ncol = len(a[0])
    nrow = len(a)

    result = [[0] * nrow for _ in range(ncol)]   # the rows and cols would be swapped in the new output

    for i in range(ncol):

        j = 0
        while j < len(a):
            result[i][j] = a[j][i]
            j += 1
    return result

a = [[1,2,3],[4,5,6]]
print(transpose_matrix(a))




	






	

