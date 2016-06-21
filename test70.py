#class 

from domains import Person
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

        
        
