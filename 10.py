# Dictionary comprehension

''' If i want to transfer list of strings in a dictionary
 i.e., strings ass KEYS and its number of letters in a word as VALUES then...'''

Names = ["Srujan", "Chandra", "Chandan", "Swamy", "Sachin", "Sujay"]

dict = {name:len(name) for name in Names}
print (dict)

# If want to tranfer data from 1 dict to another dict with some condition then...
city_population = {
    "Mumbai" : 97,
    "Bangalore" : 95,
    "Davanagere" : 60,
    "Hungund" : 25
}
# Now we separate the large cities based on population i.e., (population > 50)
large_cities = {city:pop for city,pop in city_population.items() if pop>50}
print(large_cities)
