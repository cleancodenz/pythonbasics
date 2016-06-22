class Name:
    def __init__(self, first_name, last_name, middle_name):
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
 
    def name(self):
        return self._first_name + " " + self._middle_name + " " + self._last_name
        
class Address:
    def __init__(self, street_name, street_number, postal_code, city):
        self._street = street_name
        self._number = street_number
        self._postal_code = postal_code
        self._city = city
 
    def address(self):
        return str(self._number) + " " + self._street + " " + self._postal_code + " " + self._city
 
class Telephone:
    def __init__(self, home, office, mobile):
        self._home_number = home
        self._office_number = office
        self._mobile_number = mobile
 
    def home_number(self):
        return self._home_number
 
    def mobile_number(self):
        return self._mobile_number
 
    def office_number(self):
        return self._office_number
        
class Person_New:
 
    def __init__(self, name, address, telephone, age):
        self._name = name
        self._address = address
        self._telephone = telephone
        self._age = age
 
    def describe_me(self):
        return "My name is " + self._name.name() + ", I am " + str(self._age) + " years old, my address is " + self._address.address() \
            + " and you can reach me at home on " + self._telephone.home_number()
 
    def shout(self, what, how_many_times):
        for i in range(0,how_many_times):
            print(what)
    #this is polymophism, formatter is just a method that has same interface        
    def format_me(self, formatter):
        properties = {"name": self._name.name(), "age": str(self._age), "address": self._address.address()}
        formatter("person", properties) 
            
def print_as_xml(root_name, properties_dictionary):
    print("<" + root_name + ">")
    for prop in properties_dictionary:
        print("<" + prop + ">" + properties_dictionary[prop] + "</" + prop + ">")
    print("</" + root_name + ">")
 
def print_as_json(root_name, properties_dictionary):
    lines = []
    print("{\"" + root_name + "\": {")
    for prop in properties_dictionary:
        lines.append("\"" + prop + "\": \"" + properties_dictionary[prop] + "\"")
    print(",".join(lines))
    print("}}")
     