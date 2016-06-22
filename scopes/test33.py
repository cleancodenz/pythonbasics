# variable scope


# this is global scope
user_input =10

def get_integer_input(prompt_text):
   
    #this is local scope, nothing to do with global scope
    # this shadows the global variable
    #actually it has nothing to do with outside
    user_input = raw_input(prompt_text)
    print user_input
    return int(user_input)
 
int_input = get_integer_input("Provide a number...")   
print(user_input)


# the way to reference outside one

def get_integer_input_from_outside(prompt_text):
    global user_input
    print("befor change")
    print user_input 
    user_input = raw_input(prompt_text)
    print("after change")
    print user_input
    return int(user_input)
 
int_input = get_integer_input_from_outside("Provide a number...")   
print(user_input)

# returning multiple values using Tuple
# Tuple is a collection delimited by parenthesis
# therefor list is [],dictionary {}
def calculate(first_number, second_number):
    sum = first_number + second_number
    diff = first_number - second_number
    div = first_number / second_number
    mult = first_number * second_number
    return sum, diff, div, mult
    
all_results = calculate(8,4)
 
print(all_results)
 
sum = all_results[0]
diff = all_results[1]
div = all_results[2]
mult = all_results[3]
 
