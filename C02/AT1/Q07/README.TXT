import numpy as np

# Sample pixel values
pixels = np.array([20, 40, 60, 80, 100])

# Threshold value
T = 50

# Apply threshold
binary_output = np.where(pixels >= T, 1, 0)

print("Original pixels:", pixels)
print("Threshold:", T)
print("Binary output:", binary_output)
