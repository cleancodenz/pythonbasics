
class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
 
    #where number of legs and make_sound does not exist in this base class 
    #they have to be proivded by child classes
    # but describe_me will not be implemented by child classes
        
    def describe_me(self):
        print("My name is {}, I am {} years old , I have {} legs. My language sounds as follows: {}"
        .format(self._name, self._age, self.number_of_legs(), self.make_sound()))

class Dog(Animal):
    
    def make_sound(self):
        return "Woooff"
 
    def number_of_legs(self):
        return 4
 
    def catch_intruders(self, number_of_intruders):
        print("Caught {} intruders!".format(number_of_intruders))
        
class Duck(Animal):
 
    def make_sound(self):
        return "Quack"
 
    def number_of_legs(self):
        return 2
 
    def what_is_so_special(self):
        return "I am known for duck typing"
 
    def average_weight(self):
        return 3
    