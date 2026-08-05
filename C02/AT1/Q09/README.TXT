import numpy as np

# Pixel intensities
pixels = np.array([40, 45, 48, 50, 52, 55, 60])

# Seed value
seed = 50

# Threshold difference
threshold = 5

# Select pixels belonging to the region
region = pixels[np.abs(pixels - seed) <= threshold]

print("Pixel values:", pixels)
print("Seed:", seed)
print("Threshold difference:", threshold)
print("Pixels in region:", region)
