#class 

from domains import Person
from domains_new import *

# initiator, if call Person() exception, parameters will not match
person = Person("Mike",40)
print person.whats_your_name()
# dot notation
person.shout()

print(person.describe_me())
#this is using one argument initiator
#person = Person()
#print person.whats_your_name()

#there is no private properties, but you should not do it, using naming convension to prevent it
person._name ="Mr. President"
print person.whats_your_name()

person.shout_new("Hello",4)

person.name("Not John")

print person.get_name()

#using composite classes
name = Name("John", "Smith", "William")
telephone = Telephone("34535", "345345", "65765754")
address = Address("New street", 34, "324 56", "Los Angeles")
person = Person_New(name, address, telephone, 30)
print(person.describe_me())

person.format_me(print_as_xml)
person.format_me(print_as_json)



     
        
