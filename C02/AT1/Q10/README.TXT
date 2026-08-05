import numpy as np

# Given mean after averaging
mean_value = 48

# Sample threshold
T = 50

# Apply threshold
if mean_value >= T:
    output = 1
else:
    output = 0

print("Smoothed value:", mean_value)
print("Threshold:", T)
print("Final segmented output:", output)
