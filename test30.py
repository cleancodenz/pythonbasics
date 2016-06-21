# default argument
def multiply(base, multiplier=2, show_greeting = True):
    if show_greeting:
        print("Welcome to the multiply function")
    return base*multiplier
 
result = multiply(10)
 
result = multiply(10,3,False)

#bizar exaple

def modify_list(list_param=[]):
    list_param.append("Default")
    return list_param
 
l1 = modify_list()
print l1

#this is because the same function keeps using same object for arugment(evaluated at def line) in each call
# to avoid this the default aguments must be immutable object like int and string rather than a list 
l1 = modify_list()
l1 = modify_list()
l1 = modify_list()

print l1

def modify_list_rightway(list_param=None):
    if list_param is None:
        list_param = []
    else:
        list_param.append("Default")
   

def show_greeting(name, age, location):
    print("Welcome " + name + "! You are " + str(age) + " years old and live in " + location)
    
show_greeting("Andras", 36, "Stockholm")

# or with names that will ignore the order
show_greeting(location="Stockholm", age=36, name="Andras")

