# Functions - Nothing new! , type() , piece of reusable code, Solves particular task , call function instead of writing code yourself

fam = [1.73, 1.68, 1.71, 1.89]
print(fam)

tallest = max(fam)  # max() - built-in function
print(tallest)

# round() - built-in function
print(round(1.68, 1))  # round(number , ndigits)
print(round(1.08))

# help(round)  --- Open up documentation

# sorting
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second
full_sorted = sorted(full, reverse=True)
print(full_sorted)


# ----------------------
# Methods

# Built-in Functions - max(), len()
# Get index in list ? , Reversing a list?

sister = "lizz"
height = 1.73

fam = ["liz", 1.73, "enna", 1.68, "mom", 1.71, "dad", 1.89]  # Object str , float , list
# Methods : Functions that belong to objects

# Example of methods - [capitalize() , replace()] - string
# [bit_length(), conjugate()] - int , float
# [index() , count()] - list

getIndex = fam.index("mom")
print(getIndex)

print(fam.count(1.73))

# str methods
print(sister.capitalize())  # first letter capitalize

replace_try = sister.replace("z", "sa")
print(replace_try)

# Methods - Everything = object , Object have methods associated , depending on type
# Some methods can change the objects they are called on

fam.append("me")
print(fam)

fam.append(1.79)
print(fam)


# ----------------------
# Summary 
# Functions
type(fam)  # Methods : call functions on objects

fam.index("mom")  # we can call methods on the object with dot notation

# methods : upper(), reverse(), count(), index(), append()


# ----------------------
# Packages

# Functions and methods are powerful
# All code in python distribution? - Huge code base : messy , Lots of code you won't use , maintenance problem - so use packages

# Packages - Directory of python scripts , each script = module
# Specify functions, methods, types , thousand of packages available - numpy , matplotlib , scikit-learn - for ml

# Install package - https://pip.pypa.io/en/stable/installation/
# For system : Download get-pip.py
# Terminal: python3 get-pip.py , pip3 install numpy


# Import package
import numpy
numpy.array([1, 2, 3])

import numpy as np
np.array([1, 2, 3])

from numpy import array
array([1, 2, 3])


# Using numpy - not very clear version
fam = ["liz", 1.73, "enna", 1.68, "mom", 1.71, "dad", 1.89]
fam_ext = fam + ["me", 1.79]

print(str(len(fam_ext)) + " elements in fam_ext")

np_fam = np.array(fam_ext)  # clearly using numpy


# ----------------------
# Math Package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Import pi directly
from math import pi

C = 2 * 0.43 * pi
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))


# ----------------------
# SciPy Example
from scipy.linalg import inv as my_inv
print(my_inv([[1, 2], [3, 4]]))
