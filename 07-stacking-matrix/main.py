import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

print(f"Matrix a:\n{a}")
print(f"Matrix b:\n{b}")

# Stacking matrix (or also known as "menumpuk matrix" in Indonesia language)
c = np.hstack((a, b))
d = np.vstack((a, b))
print(d)

# Another way to stack a matrix using concatenate function, and axis key word argument
e = np.concatenate((a, b), axis=1) 
print(e)