# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

# With indexes
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for index, area in enumerate(areas):
    print("room " + str(index) + ": " + str(area))

#----------------
# Loop over List of Lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
for room , area in house:
    print("the " + str(room) + " is " + str(area) + " sqm")


#--------------------------------------
# Loop Over Dictionaries
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
for key, value in europe.items() :
    print("the capital of " + key + " is " + str(value))