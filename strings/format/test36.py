#string concatenation, with + multiple strings are created
#using join to be more efficient

combined = "Welcome" + " to" + " my blog " + "dear " + "readers"
print(combined)

#two pairs of brackets, the inside one creates a tuple
#join is performed on a collection
#the first character is a delimiter
combined = '|'.join(("This", "is", "a", "delimited", "string"))
print(combined)

combined = '|'.join(["This", "is", "a", "delimited", "string"])
print(combined)

#spliting a delimited string
spl = combined.split('|')
print spl

#string partioning
time ="14:55"
partitioned = time.partition(':')
print partitioned

#also 
hour, partitioner, minute = time.partition(':')

print(' '.join([hour, minute]))

# string formating
myformat = "My name is {0}, I come from {1} and currently live in {2}"
formatted = myformat.format("John", "England", "Birmingham")
print formatted

# string formating- reusing
myformat = "My name is {0}, I come from {1} and currently live in {2}.I repeat, my name is {0}"
formatted = myformat.format("John", "England", "Birmingham")
print formatted

# string formating- no indexing
myformat = "My name is {}, I come from {} and currently live in {}."
formatted = myformat.format("John", "England", "Birmingham")
print formatted

#string formating - naming
myformat = "My current geographical position is {city}, {country}, {continent}."
formatted = myformat.format(city="Stockholm", country="Sweden", continent="Europe")
print formatted

#string formating - list
geo_args = ["Stockholm", "Sweden", "Europe"]
myformat = "My current geographical position is {geo_args[0]}, {geo_args[1]}, {geo_args[2]}"
formatted = myformat.format(geo_args=geo_args)
print formatted

