import numpy as np

# 1. Membuat array dengan tipe data tertentu
# nums1 = np.array([1, 2, 3, 4, 5], dtype='int16')
nums1 = np.array([1, 2, 3, 4, 5], dtype=np.int16)

# 2. Membuat array dengan menggunakan function
nums2 = np.fromfunction(lambda baris, kolom: kolom ** 2, (1, 10), dtype=np.int32)
nums3 = np.fromfunction(lambda kolom, baris: kolom + baris, (4, 4), dtype=np.float32)

# 3. Membuat array atau matrix dengan menggunakan iterable
iterable = [num ** 2 for num in range(5)]
nums4 = np.fromiter(iterable, dtype=np.int16)

# 4. Multitype array
grades = np.array([["Ali", 80], ["Gerry", 100], ["Mogi", 90]], dtype=object)

# Display
print(grades)
print(grades.dtype)