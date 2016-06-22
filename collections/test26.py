# all variables are reference types, x point to object "5" which is primitive type
x = 5
# in this case 5 will be garbage collected
x = 10

# both x and y will be pointing tot he same integer objects
x = 5
y = 5

# this returns true as both x and y point to the same value  
print(x==y)

s1 = "hello"
s2 = "hello"

# this returns true
print(s1 == s2)

# value euqality 
print( 5 ==5 )
# string comparison is case sensitive
print("hello" != "Hello")

# value equality also applies to collection

myFirstList = ["small", "medium", "large", "x-large"]
mySecondList = ["small", "medium", "large", "x-large"]
# True
print(myFirstList == mySecondList)

#reference equality aslo use is 
print( x is y)
#reference equality is does not apply to collection

# False
print(myFirstList is mySecondList)

x = 5
# this is reference assignment, y and x point to 5
y = x
# this is will change value for both x, 3 is a new object, this is called object immutability
# = only assign a new value to an object if right side is value object
# y will still be 5

x = 3
print(x)
print(y)

#same here
s1 = 'hello'
s2 = s1
s1 = 'bye'
#bye
print(s1)
#hello
print(s2)

# same here,  we will get two separate lists

myFirstList = ["small", "medium", "large", "x-large"]
mySecondList = myFirstList
myFirstList = ["smallish", "medium", "large", "x-large", "xx-large"]
print(myFirstList)
print(mySecondList)

# modification through direct access
myFirstDictionary = {"S": "Small", "M": "Medium", "L": "Large", "XL": "X-Large"}
mySecondDictionary = myFirstDictionary
myFirstDictionary["S"] = "Smallish"
myFirstDictionary["XXL"] = "XX-Large"
# same value but modified
print(myFirstDictionary)
print(mySecondDictionary)

#passing object by reference 
def modify_dictionary(dictionary):
    #this will change original dictionary as well
    dictionary["XL"] = "Extra Large"
    return dictionary
    
# keep the original value by making a deep copy 
def deep_copy_dictionary(dictionary):
    deep_copy={}
    for item in dictionary:
        deep_copy[item] = dictionary[item]
    return deep_copy




    
 






 