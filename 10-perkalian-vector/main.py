import numpy as np

# Create the vector arrays
a1 = np.array([1, 3])
b1 = np.array([3, 0])

# Dot product on vector arrays
c1 = np.dot(a1, b1)

# Display the result
print(c1)

# Cross product
a2 = np.array([1, 2, 0])
b2 = np.array([2, 1, 0])
c2 = np.cross(a2, b2)
c3 = np.cross(b2, a2)

# Display the results
print(c2)
print(c3)