capitals = {
    "Stockholm", "Budapest", 
    "Helsinki", "Copenhagen", "Oslo", "Paris"}

try:
    y = 10 / 0
# following line will throw key error: KeyError: ‘Washington’
# exception type is: KeyError
    capitals.remove("Washington")
except KeyError:
    print("This capital doesn't figure in the collection")
except ZeroDivisionError:
    print("Errr..., what are you doing???")
#this is way of handling multiple exceptions, but one exception can only be handled once
except (KeyError, ZeroDivisionError):
    print("Incorrect") 
    
except Exception:
    print("Exception")    
    
# interogation of Exception
try:
    capitals = {"Stockholm", "Budapest", "Helsinki", "Copenhagen", "Oslo", "Paris"}
    y = 10 / 0
    print("About to remove Washington...")
    capitals.remove("Washington")
except KeyError as err:
    print("No such capital in the collection.")
except Exception as err:
    print(type(err))
    print(err.args)
    print(err)
    
def divide(first,second):
    res =0
    try:
        res = first/second
    except ZeroDivisionError:
        print("Big NONO")
        raise
    return res 

try:
    res = divide(10,0)
    print(res)
    print("I am here")
except Exception as err:
    print(type(err))
    print(err.args)
    print(err)
finally:
    print("This statement is always executed.")
    print("...and this one as well.")
    

