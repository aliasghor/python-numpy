import numpy as np

# 3. Operasi aritmatika

# Built-in lists type in Python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]


# NumPy arrays
anp = np.array(a)
bnp = np.array(b)

# Perform Elementwise operation on Python built-in lists type

# Addition
# result = a + b # This will yields a concatenation

# The correct way to perform elementwise operation on lists
result = []

for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)
# Elementwise operation on NumPy array

# 1. Addition
result = anp + bnp

# 2. Substraction
result = anp - bnp

# 3. Division
result = anp / bnp

# 4. Multiplication
result = anp * bnp

# 5. Eksponent
result = anp ** 2 # All elements in an array to the power of 2


# Display
print(result)