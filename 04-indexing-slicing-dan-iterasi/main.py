import numpy as np

a = np.arange(10) ** 2
print(a)

# Indexing
print(f"First element of an array = {a[0]}")
print(f"The seventh element of an array = {a[6]}")
print(f"Last element of an array = {a[-1]}")

# Slicing
print(f"Element from 1-6 are = {a[:6]}")
print(f"Element from fourth position until so on are = {a[4:]}")
print(f"Reversing an array = {a[::-1]}")

# Iterating over an array
for index, value in enumerate(a):
    print(f"a[{index}] = {value}")
