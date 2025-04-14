import numpy as np

# Create a template of 2D lists
dtype = [("Name", "S5"), ("Height", int)]
values = [("Gerry", 165), ("Ali", 200)]

# Create a multitype array
mix_array = np.array(values, dtype=dtype)

# Sort the array based on its height 
mix_array.sort(order="Height")
print(mix_array)

# Sort the array based on its name
mix_array.sort(order="Name")
print(mix_array)