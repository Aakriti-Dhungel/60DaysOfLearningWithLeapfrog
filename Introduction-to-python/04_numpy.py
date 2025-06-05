# List Recap:
# - Powerful collection of values
# - Can hold different types
# - Can change, add, remove items
# - Limitation: Not ideal for mathematical operations over collections

# NumPy in Data Science:
# - Enables fast, element-wise operations
# - Works well with large numerical datasets

# Python Lists
height = [1.75, 1.67]
weight = [65.4, 59.2]
print("Height list:", height)
print("Weight list:", weight)

# Problem: BMI = weight / height ** 2 (not possible directly with lists)

# Solution: Use NumPy
# Installation (in terminal): pip install numpy

import numpy as np

# Convert lists to NumPy arrays
np_height = np.array(height)
np_weight = np.array(weight)
print("NumPy Height:", np_height)
print("NumPy Weight:", np_weight)

# Calculate BMI
bmi = np_weight / np_height ** 2
print("BMI:", bmi)

# NumPy Example: Create array from list
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
print("Type of np_baseball:", type(np_baseball))  # <class 'numpy.ndarray'>

# Comparison: Python list vs NumPy array
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])
print("Python list + list:", python_list + python_list)  # Concatenation
print("NumPy array + array:", numpy_array + numpy_array)  # Element-wise addition

# NumPy Subsetting
print("BMI array:", bmi)
print("Second BMI value:", bmi[1])  # Indexing

# Boolean subsetting
print("BMI > 23:", bmi > 23)  # Boolean array
subsetting = bmi[bmi > 23]
print("BMI values > 23:", subsetting)


import numpy as np
# -----------------------
# 2D NumPy array
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(type(np_2d))     # Print type of np_2d
print(np_2d)
print(np_2d.shape)    # Shape: (2, 5) -> 2 rows, 5 columns

# Subsetting
print(np_2d[0])          # First row
print(np_2d[0][2])      # First row, third element
print(np_2d[0, 2])     # Same as above (recommended)
print(np_2d[:, 1:3])    # All rows, column 1 to 2
print(np_2d[1, :])        # Second row (all columns)

# 2D Baseball data
baseball = [
    [180, 72, 29],
    [215, 74, 33],
    [210, 73, 30],
    [188, 71, 27],
    [176, 70, 26]
]
np_baseball = np.array(baseball)

# Accessing specific data
print("5th player data:", np_baseball[4, :])
print("All player weights:", np_baseball[:, 0])
print("Height of 3rd player:", np_baseball[2, 1])

# Updated data for addition (must match shape)
updated = np.array([
    [5, 1, 0],
    [3, 0, 0],
    [4, 1, 1],
    [2, 0, 0],
    [3, 0, 0]
])

# Element-wise addition
print("Updated data added:", np_baseball + updated)

# Unit conversion
conversion = np.array([0.0254, 0.453592, 1])
print("Converted data (to metric):", np_baseball * conversion)
