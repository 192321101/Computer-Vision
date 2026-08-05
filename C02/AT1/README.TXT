import numpy as np

# Sample frequency components
frequency = np.array([100, 80, 50, 30, 20])

# Create output with zeros
filtered = np.zeros(len(frequency))

# Retain only the first two components
filtered[0] = frequency[0]
filtered[1] = frequency[1]

print("Original frequency components:", frequency)
print("Filtered output:", filtered)
