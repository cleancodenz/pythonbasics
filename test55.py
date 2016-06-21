sizes = {"S": "Small", "M": "Medium", "L": "Large", "XL": "X-Large"}
# this is getting keys
for size in sizes:
    print "Key ", size, " Size ",sizes[size]
    
#this is getting keys
for key in sizes.keys():
      print "Key ", key, " Size ",sizes[key]
      
#this is getting values
for val in sizes.values():
      print " Value ",val
      
#this is getting tuple with key and value pairs
for item in sizes.items():
    print(item)
    
for key,value in sizes.items():
    print("Key: {0}, value: {1}".format(key, value))
    
# update dictionary with another dictionary, if the same key, the value will be overwrite

sizes = {"S": "Small", "M": "Medium", "L": "Large", "XL": "X-Large"}
more_sizes = {"XS": "Extra-Small", "XXL": "Double-extra-large", "S": "Smallish"}
print("Before: {0}".format(sizes))
sizes.update(more_sizes)
print("After: {0}".format(sizes))

# update can also accept tuples
sizes = {"S": "Small", "M": "Medium", "L": "Large", "XL": "X-Large"}
more_sizes = [("XS", "Extra-small"), ("XXL", "Double-extra-large")]
print("Before: {0}".format(sizes))
sizes.update(more_sizes)
print("After: {0}".format(sizes))
# update with comma separated list
sizes = {"S": "Small", "M": "Medium", "L": "Large", "XL": "X-Large"}
print("Before: {0}".format(sizes))
sizes.update(XS = "Extra-small", XXL = "Double-extra-large", S = "Smallish")
print("After: {0}".format(sizes))

# delete item using del

sizes = {"S": "Small", "M": "Medium", "L": "Large", "XL": "X-Large"}
print("Before: {0}".format(sizes))
del sizes["S"]
print("After: {0}".format(sizes))
