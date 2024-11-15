import numpy as np
from tasks import *

# Matrices
input_matrix = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
kernel_matrix = np.array([[1, 0], [1, -1]])

# Kernel shapes
kernel_height, kernel_width = kernel_matrix.shape

# Specify return_size
height, width = compute_output_size_2d(input_matrix, kernel_matrix)
return_matrix = np.zeros([height, width])

# Per row
for i in range(height):
    for j in range(width):
        print(f"Heigth= {i}, Width= {j}")

        return_matrix[i, j] = np.sum(
            input_matrix[i:i + kernel_width, j:j + kernel_height] * kernel_matrix)

print(return_matrix)
