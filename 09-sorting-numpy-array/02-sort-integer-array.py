import numpy as np

np.random.seed(0)

# Create a random integer array numbers
a = np.random.randint(1, 10, size=5)
print(a)

# Find the maximum and minimum numbers in an array
print(f"The maximum number in an array = {np.max(a)}")
print(f"The value {np.max(a)} is located in index {np.argmax(a)}")
print(f"The minimum number in an array = {np.min(a)}")
print(f"The value {np.min(a)} is located in index {np.argmin(a)}")