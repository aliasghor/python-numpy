import numpy as np

a = np.array([[1, 2], 
              [3, 4]])

print(f"Matrix a:\n{a}")

b = np.ones((2, 2))

print(f"Matrix b:\n{b}")

# Multiplying matrix by another matrix (dot product)
c = np.dot(a, b)
print(f"Matrix c:\n{c}")
