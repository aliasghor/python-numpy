import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matrix a dengan ukuran: {a.shape}")
print(a)

# 1. Transpose matrix — a concept where all rows became columns
print(np.transpose(a))
# print(a.transpose()) # Another way to transpose a matrix 
# print(a.T) # Another way to transpose a matrix

# 2. Flatten array
print(f"Flatten matrix a: {np.ravel(a)}")

# 3. Reshape matrix
print(f"Reshape matrix a:\n{np.reshape(a, shape=(3, 2))}")

# 4. Resize matrix
a.resize(3, 2)
print(a)
print(f"Matrix a dengan ukuran: {a.shape}")