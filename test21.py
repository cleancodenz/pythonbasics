import calendar
from calendar import formatstring
from calendar import format as fc
#colon means start of new block
#space indentation means the same block
for i in range(10):
    print(i+2)
    print(i*2)
    print(i-2)
    
for i in range(10):
    print(i+2)
print(i*2)
print(i-2)
 
for i in range(10):
     print(i+2)
     if i == 3:
         print(i*2)
         print(i-2)
     elif i == 5:
         print(i^2)   
     print("Current value of i: {}".format(i))
     
         
 
