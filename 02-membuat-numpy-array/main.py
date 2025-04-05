import numpy as np

# 1. Membuat vector (one dimensional array)
a = np.array([1, 2, 3, 4, 5], dtype=np.int16) # Manually specify the data type of an array
b = np.array([1.5, 2.5, 3.14])

# 2. Membuat vector dengan range
c = np.arange(0, 11, 2)
d = np.arange(1, 11, 0.5)

# 3. Membuat linspace
e = np.linspace(1, 10, 5)

# 4. Array multidimensi (matrix)
f = np.array([(1, 2), (3, 4)])

# 5. Matrix dengan nilai nol
g = np.zeros((5, 3))

# 6. Matrix dengan nilai 1
h = np.ones((5, 3))

# 7. Matrix identity
i = np.identity(5)

# Display
print(i)