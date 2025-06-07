# Python Basics: Introduction and key concepts

# General purpose: build anything with Python!
# Open source, free to use, tons of packages for data science and many other fields.

# Python script files end with `.py`

# Simple print statements
print("Hello World")
print(5 / 8)

# Python as a calculator - Addition, Division , Subtraction , Multiplication
print(4 + 5) 
print(10 / 2)     
print(5 - 5)      
print(3 * 5)      

# Variables and types
# Use variables to store values and call them by name

height = 7.79      # height in meters
weight = 68.7      # weight in kg

# Calculate BMI (Body Mass Index)
# BMI = weight / height squared
bmi = weight / height ** 2
print("BMI:", bmi)

# Check variable types
print(type(bmi))           # float
day_of_week = 7
print(type(day_of_week))   # int

# Strings and booleans
x = "body mass index"
y = 'this works too'
print(type(y))             # str

z = True
print(type(z))             # bool

# Behavior depends on type:
print(2 + 3)        # 5 (integer addition)
print('ab' + 'cd')  # 'abcd' (string concatenation)

# Variable assignment 
savings = 100
print("Savings:", savings)

monthly_savings = 10
num_months = 4
new_savings = monthly_savings * num_months
print("New savings:", new_savings)

# More variable types
half = 0.5
intro = "Hello! How are you?"
is_good = True

# Operations with variables
total_savings = savings + new_savings
print("Total savings:", total_savings)
print("Type of total_savings:", type(total_savings))

# String operations
doubleintro = intro + intro
print("Double intro:", doubleintro)
