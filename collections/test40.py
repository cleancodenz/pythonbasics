cities = ["Stockholm", "Budapest", "Berlin", "Paris", "Birmingham", "Zürich"]
#negative indexes, -1 means last element
print cities[-1]
print cities[-2]

#insert elements, before the third element
cities.insert(3,"Oslo")

#append from end
cities.append("London")
print cities

# concatenating two lists
cities = ["Stockholm", "Budapest", "Berlin", "Paris", "Birmingham", "Zürich"]
more_cities = ["Barcelona", "Helsinki", "Copenhagen", "Moscow"]
joined_cities = cities + more_cities
cities += more_cities
print cities

cities.extend(more_cities)

print cities

# removing elements , this does not work with character based string

del cities[2]

# remove first appearance of it
cities.remove("Moscow")

print cities

# find the position of an item, if item does not exist then an exception
paris_pos = cities.index("Paris")

print paris_pos

# search start and end, if not found exception
#paris_pos = cities.index("Paris",4,5)

#slicing a list, index based

cities = ["Stockholm", "Budapest", "Berlin", "Paris", "Birmingham", "Zürich"]

reduced = cities[1:5]
#starting from 3
reduced = cities[3:]

#copy a list

#copy a list through slicing
cities_copy = cities[:]

#this is true
print(cities == cities_copy)
#this is false 
print(cities is cities_copy)

#copy a list though list constructor
cities_copy = list(cities)
#copy a list through copy function, not supported in ver2
#cities_copy = cities.copy()

#sorting a list, this gets a new sorted

cities.sort()

print cities

cities.sort(reverse=True)

print cities

#if you do not want to change the original list, using sorted function
sorted_cities = sorted(cities)

print cities, sorted_cities

sorted_cities = sorted(cities, reverse=True)

print cities, sorted_cities

# reverse a list

cities.reverse()

# keep the original
rev_iterable = reversed(cities)


# enumerate function, which returns a tuple with 2 elements, first one is index, second is item itself

for city_enum in enumerate(cities):
    print("City #{0}:{1}".format(city_enum[0],city_enum[1]))
    
for index,city in enumerate(cities):
    print("City #{0}:{1}".format(index,city))
    
    





