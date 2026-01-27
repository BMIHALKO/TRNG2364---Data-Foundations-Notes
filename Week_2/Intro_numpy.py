# numpy is powerful library for numerical computing
# it provides support for arrays, matricies, and a wide range of mathematical functions
# to operate on these data structures
# Many libraries build on top of numpy (pandas, scipy, scikit-learn)

# numpy is written in C and Fortran, making it very fast for numerical computations

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 5, 6, 34, 81])
print(f"1D Array: {array_1d}")

# Create a 2D array
array_2d = np.array([[5, 9, 18],[91, 45, 16]])
print(f"2D Array: {array_2d}")

# Perform som bacsic operations
# addition
array_sum = array_1d + 10
print(f"Array after addition: {array_sum}")

# multiplication
array_multiplication = array_1d * 4
print(f"Array after multiplication: {array_multiplication}")

# calculate the mean
mean_value = np.mean(array_1d)
print(f"Mean: {mean_value}")

# calculate standard deviation
standard_dev = np.std(array_1d)
print(f"Standard Deviation: {standard_dev}")

# Reshape our 1d array to 2d array
reshaped_array = array_1d.reshape((6, 1))
print(f"Reshaped Array: {reshaped_array}")

# access elements
accessed_element = array_2d[0][2]
print(f"Accessed Element: {accessed_element}")