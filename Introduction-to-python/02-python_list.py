#Python Data Types
# float - real numbers , int - integer numbers, str- string,text ,bool - True,False

height = 1.73
tall = True #Each variable represents single value

# Problem 
# Datascience: many data points , Height of entire family

height1 = 1.73
height2 = 1.68
height3 = 1.79

# Inconvenient


# Python list
# [a,b,c]
fam = [1.73,1.68,1.79] # Name a collection of values, contain any type, contain different types


["liz",1.73,"sam",1.55]
fam2 = [["liz",1.7],
       ["sam",1.55]]
print(fam) 
type(fam2) # list - specific functionality, specific behavior



#problem 1
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall,kit,liv,bed,bath]

# Print areas
print(areas)

#Problem 2
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

#Problem 3
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ["bedroom", bed],
        ["bathroom",bath]]

# Print out house
print(house)


# Subsetting Lists
fam = ["liz",1.73,"emma",1.68,"mom",1.71,"dad",1.89]
print(fam)
print(fam[3])
print(fam[6])
print(fam[-1]) #Negative indexing

#List Slicing
print(fam[3:5]) # syntax: [start : end] -- start-inclusive , end-exclusive
print(fam[1:4])
print(fam[:4]) # start from index 0
print(fam[5:]) # until last element of the list

house = [
        ["hallway", "hall"],
        ["kitchen", "kit"],
        ["living room", "liv"],
        ["bedroom", "bed"],
        ["bathroom","bath"]]

# Print out house
print(house[4][1])


#Manipulating Lists -- change list elements , Add list elements , remove list elements

fam = ["liz",1.73,"emma",1.68,"mom",1.71,"dad",1.89]
print(fam)

# change index 7
fam[7]=1.86
print(fam)

# change entire list slice at once
fam[0:2]=["lisa",1.74]
print(fam)

#Adding and removing elements
fam_ext = fam +["me",1.79]
print(fam_ext)
del fam[2]
print(fam)

# Behind the scenes (1) -- Memory reference concept
x = ["a", "b","c"]
y=x
y[1]= "z"
print(y)
print(x)

# another 
a = [1, 2, 3]
b = a        # b references the same list as a
b.append(4)

print("a =", a)  # Output: a = [1, 2, 3, 4]
print("b =", b)  # Output: b = [1, 2, 3, 4]

#Behind the scenes(2)
x = ["a", "b","c"]
y= list(x)
y=x[:]
y[1]="z"
print(x)
print(y)





