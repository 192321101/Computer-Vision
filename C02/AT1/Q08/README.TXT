import numpy as np

# Sample 3×3 image matrix
image = np.array([
    [10, 10, 10],
    [20, 20, 20],
    [50, 50, 50]
])

# Horizontal Sobel mask
sobel = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

# Calculate gradient
gradient = np.sum(image * sobel)

print("Input matrix:")
print(image)

print("Sobel gradient:", gradient)
