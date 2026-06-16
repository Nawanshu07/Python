# Create a Dog class with:

# A name property (getter + setter)
# The setter should just make sure the name is stored in uppercase
# A read-only sound property that always returns "Woof!"

class dog:
    sound  = "woof!"
    def __init__(self,name):
        self.name = name.upper()
    
    @property
    def name(self):
        return self._name
    
    @property
    def sound(self):
        return "woof!"
    
    @name.setter
    def name(self , value):
        self._name = value.upper() 


tommy = dog("Tommy")
tommy.name = "Monika"
print(tommy.sound)
print(tommy.name)