# String is immutable
myString ="hello world. this is python calling"
myOtherString = 'hello world, this is python calling'

# String cancatenation
myString1 = "hello " "world " "of " "Python"

myString2 ="He said :\" Hello World \""

print(myString2)

# Triple quote used as literal 
myString3 =""" this
is 
multiline"""

print(myString3)

myIntegerString = str(132)
myBooleanString = str(True)

# Extracting individual character
hello = "hello"
first = hello[0]
print(first)

helloCap = hello.upper()

print(helloCap)
# this returns true
helloStartWithH = hello.startswith('h') 
print(helloStartWithH)
# this returns false
helloStartWithH = hello.startswith('H') 
print(helloStartWithH)
