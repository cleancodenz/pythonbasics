class Person:
    #there is no constructor python class, but there is a init function
    def __init__(self,name,age):
        #add some validations
        if name == "" or str(name).isspace():
            raise ValueError("Person's name must not be empty.")
        if not str(age).isdigit():
            raise ValueError("Age must be a number.")
        if age < 0 or age > 120:
            raise ValueError("Age must lie between 0 and 120.")
            
        self._name = name
        self._age = age
        
    #multiple initiators is not supported by ver 2
    #def __init__(self):
        #self._name ="Unknown"
   
    #every function has a default parameter self passed in
    def whats_your_name(self):
        return self._name
    def describe_me(self):
        return "My name is " + self._name + " and I am " + str(self._age) + " years old."
    
    def shout(self):
        print("HELLOOOOO")
    def shout_new(self, what, how_many_times):
        for i in range(0, how_many_times):
            print(what)
    #setters, as _name access is not recommended
    #if you do not see a machine setter, it might not be meant to be changed
    def name(self,name):
           #add some validations
        if name == "" or str(name).isspace():
            raise ValueError("Person's name must not be empty.")
        self._name = name
        
    def set_name(self, name):
        self._name = name
    #getters
    
    def get_name(self):
        return self._name
        
      
            
  