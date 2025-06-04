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
