import numpy as np
import time

start = time.time()
even_nums = [num for num in range(1001) if num % 2 == 0]
end = time.time()
print(f"The execution time that it took using list comprehension = {end - start}")

array = np.arange(1001, dtype=np.int32)
start = time.time()
even_nums = array[array % 2 == 0]
end = time.time()
print(f"The execution time that it took using numpy boolean mask array = {end - start}")
