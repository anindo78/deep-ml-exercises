'''
Write a Python function that performs Principal Component Analysis (PCA) from scratch.
The function should take a 2D NumPy array as input, where each row represents a
data sample and each column represents a feature. The function should standardize 
the dataset, compute the covariance matrix, find the eigenvalues and eigenvectors,
and return the principal components (the eigenvectors corresponding to the largest 
eigenvalues). The function should also take an integer k as input, representing the
number of principal components to return.

Example:
Input:
data = np.array([[1, 2], [3, 4], [5, 6]]), k = 1
Output:
[[0.7071], [0.7071]]

'''
import numpy as np 


def pca(data: np.ndarray, k: int) -> np.ndarray:
    # center the data
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0, ddof=1)
    # avoid division by zero
    std[std == 0] = 1.0
    std_data = (data - mean) / std
    # covariance
    N = data.shape[0]
    cov_matrix = (std_data.T @ std_data) / (N - 1)

    # eigen decomposition
    eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)

    # sort eigenvalues descending and select corresponding eigenvectors (columns)
    rank_indices = np.argsort(eigen_values)[::-1]
    components = eigen_vectors[:, rank_indices[:k]]   # shape: (n_features, k)

    # creating a helper function to ensure signs are fixed
    def fix_signs_maxabs(components: np.ndarray) -> np.ndarray:
    # components shape: (n_features, k)
        comps = components.copy()
        for j in range(comps.shape[1]):
            col = comps[:, j]
            idx = np.argmax(np.abs(col))
            if col[idx] < 0:
                comps[:, j] = -col
        return comps

    components = fix_signs_maxabs(components)
    return np.round(components, 4)

data = np.array([[4,2,1],[5,6,7],[9,12,1],[4,6,7]])
print (pca(data, 2))


	


