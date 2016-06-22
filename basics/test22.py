
import sys

def addTwoNumbers(x,y):
    # no code after return 
    return x+y

sum1 = addTwoNumbers(3,4)
sum2 = addTwoNumbers(5,6)

    
# void method
def printMe(whatToPrint):
    print(whatToPrint)
#__name__ the system global, loaded into main thread? main entry point
# a module can be main module or imported by others, this check will make sure it only executes as main module
if __name__ =="__main__":
    printMe(sum1)
    printMe(sum2)
# multi lines comments
"""
 getting to command line arguments from the sys module
 the file name will always be the first item of sys.argv by default
 while for new aguments you can do :
  python ***.py argument1, argument2 ...m or using quotes "to have more words as one argument"
"""
# still it is better just to use #

if len(sys.argv)>0 :
    print sys.argv
else:
    print "No command line arguments"
 




#recommended naming convention: lowercase and connected with _ 
def add_two_numbers(firstNumber, secondNumber):
    return firstNumber+secondNumber
    

   


