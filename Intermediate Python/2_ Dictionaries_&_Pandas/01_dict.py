# List example (less convenient)
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]

ind_alb = countries.index("albania")
print(ind_alb)
print(pop[ind_alb])

#  Dictionary
print("\n# Dictionary example (more intuitive)")
world = {"afghanistan": 30.55, "albania": 2.77, "algeria": 39.21}
print(world.keys())
print(world["albania"])

print("\n# Working with europe dictionary")
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

# Add italy to europe
europe['italy'] = 'rome'

# Check if italy is in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe dictionary
print(europe)

print("\n# Update and remove entries")
europe = {
    'spain': 'madrid', 'france': 'paris', 'germany': 'bonn',
    'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw',
    'australia': 'vienna'
}

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
europe.pop('australia')

# Print europe dictionary after update
print(europe)
