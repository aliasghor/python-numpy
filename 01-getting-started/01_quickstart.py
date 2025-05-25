import numpy as np

# 1. The Basics
# NumPy's main object is the 'ndarray' object, an object that only accepts elements of the same type.   

# Create the ndarray object:

# This array has one axis. This axis has three elements within it.
array1 = np.array([1, 2, 3, 4, 5])
print(array1)

# This array has two axes. The first axis has a length of two (its rows), the second axis has a length of three (its columns)
array2 = np.arange(6).reshape(2, 3)
print(array2)