# continue key word in loop just stops executing following lines and back to loop next
integers = [1, 2, 5, 3, 6, 10, 5, 6]
for i in integers:
    if i % 2 == 0:
        print('Jumping over iteration')
        continue
    print('Printing ', i)
    
#yield function which can be used in a for loop
#this is called generator function, the difference from list is it is not loaded in memory
def integer_yield():
    yield 1
    yield 2
    yield 3
    yield 4

integers = integer_yield()

for i in integers:
    print("Printing ",i)

#generator can remember the state    
def integer_yielder():
    print("In yield function at counter 100")
    counter = 100
    print("Counter: ", counter)
    yield 1
    print("In yield function at counter + 10")
    counter += 10
    print("Counter: ", counter)
    yield 2
    print("In yield function at counter + 20")
    counter += 20
    print("Counter: ", counter)
    yield 3
    print("In yield function at counter + 30")
    counter += 30
    print("Counter: ", counter)
    yield 4
    print("In yield function at counter + 40")
    counter += 40
    print("Counter: ", counter)
 
integers = integer_yielder()
for i in integers:
    print("In yielder calling function, printing ", i)
    
#list comprehension
capitals = ["Tirana", "Skopje", "Moscow", "Budapest", "Sofia", "Belgrade"]
#list comprehension is in [] result is a new list
#the second part : capital in capitals is standard loop of a list
#the first part is a function indicating what you do with each item

capitals_reversed = [''.join(reversed(capital)) for capital in capitals]
print(capitals_reversed)

capitals_capitalized = [capital.upper() for capital in capitals]
print(capitals_capitalized)

#dictionary comprehension
sizes = {"XS": "Extra-Small", 
"S": "Small", 
"M": "Medium", 
"L": "Large", 
"XL": "Extra-Large"}

lower_case_sizes = {
    size_key.lower():size_name.lower() 
    for size_key, size_name in sizes.items()}
print(lower_case_sizes)

# key and name flipped
sizes_flipped ={
    size_name : size_key 
    for size_key, size_name in sizes.items()}
    
print(sizes_flipped)

#filtering compprehension

capitals = ["Tirana", "Skopje", "Moscow", "Budapest", "Sofia", "Belgrade"]

capitals_upper = [capital.upper() for capital in capitals if len(capital)>6]
print capitals_upper


    
    