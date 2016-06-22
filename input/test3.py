import math

x=4
y=-4
#overflow?, no python does not have uplimit for it and it is signed
#it is called duck-typing 
z=math.factorial(100)

print(z)

b= 0b101
print(b)

i = int(5.75)
print(i)
 
i = int(-5.99)
print(i)
 
s = int("345")
print(s+5)

# double or float
d = 7.344

scientific = 4e10
print(scientific)
verysmall = 0.543e-2

# type casting
f = float("4.56")
f = float(13)

print(f)
 
x=10
y=2
# / division returns a float
z = x/y
print(z)
 
 #// is integer divison operator
 
z = x//y
print(z)
 
z = 10//3
print(z)
 
trueState = True
falseState = False
 
print(bool(0))
# all none zero based numbers will return True
print(bool(123))
print(bool(-12))

hello = None
res = hello == None
res1 =  hello is None
res2 = hello is not None

print(res1)
print(res2)

print(5 == 6)
print(5 != 6)
print(10 == 10)
print(3 < 5)
print(3 <= 3)
print(5 > 4)
print(5 >= 5)

val = 1
# if block start by :

if val <4:
    print('The value is greater than 4')
    print('I said that value is greater than 4')
    print('Which part of "The value is greater than 4" do you not understand?')
elif val <3:
     print('Carrying our the first elif block')
elif val<2:
     print('Executing the second elif block')
else :
     print('The value is smaller than 4')
     print('Bye')
     
upperLimit = 10
counter =0

while counter < upperLimit:
    print('We have not reached 10 yet')
    # do break
    if counter == upperLimit :
        break
    counter+=1


 #Accepting user input, not working in vscode
 
promptLessInput = raw_input()
 
print('Your promptless input was: ' + promptLessInput)

print('Your input1 was:')
print(promptLessInput)
 
promptInput = raw_input('What have you got to say: ')
print('Your prompted input was: ' + promptInput)

print('Your input2 was:')
print(promptInput)
  