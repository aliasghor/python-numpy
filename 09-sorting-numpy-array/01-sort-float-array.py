import numpy as np

np.random.seed(0)

a = np.random.randn(2, 2) * 10

print(a)

# print(f"Nilai max dari a = {a.max()}")
print(f"Nilai max dari a = {np.max(a)}")
# print(f"Posisi max dari a = {a.argmax()}")
print(f"Posisi max dari a = {np.argmax(a)}")
# print(f"Nilai min dari a = {a.min()}")
print(f"Nilai min dari a = {np.min(a)}")
# print(f"Posisi min dari a = {a.argmin()}")
print(f"Posisi min dari a = {np.argmin(a)}")

# Mengurutkan nilai
print(np.sort(a, kind="mergesort"))
print(np.argsort(a))