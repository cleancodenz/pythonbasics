# About lists/array

myFirstList=[]

myFirstList = ["small","medium","large","x-large"]

myFirstList= ["small", 7, "medium", 8, "large", True, "x-large", False]

# no clear in this version?
myFirstList.append("small")
myFirstList.append("medium")
myFirstList.append("large")

myFirstList.reverse()

print myFirstList[0]

for item in myFirstList:
    print item


myFirstDictionary = {}

myFirstDictionary = {"S":"Small", "M":"Medium", "L":"Large","XL": "X-Large"}

print myFirstDictionary

print myFirstDictionary["S"]

# add new key
myFirstDictionary["XS"] = "X-small"

# update 
myFirstDictionary["XL"] = "Very large"

print myFirstDictionary

for item in myFirstDictionary:
    print "Key " + item + ", value " +myFirstDictionary[item]
    
    
#for in range, zero based

for x in range(10):
    print x
    
for x in range(100,200,300):
    print x

collectionSize = len(myFirstList)

for x in range(collectionSize):
    print myFirstList[x]



    


