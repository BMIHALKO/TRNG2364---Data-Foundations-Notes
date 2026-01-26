#Day 3

#Python is an object oriented programming language
#it makes use of classes and objects to create our systems and applications
#classes are blueprints, objects are generated based on those blueprints

class Animal:
    #In Python we have to override the __init__() to create our constuctor
    #Notice this is DOUBLE underscore
    #Double leading and trailing underscores are used for special methods that
    #Python calls automatically in certain situations(__init__(), __str__(), __len__())

    #passing in self references our freshly created object in our constructor
    def __init__(self, name, age):
        self.name = name
        self.__age = age  #Double underscores means private property
    
    #getter for private properties only
    def get_age(self): return self.__age

    #setter for private properties only
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0")
    
    def speak(self):
        print("The animal made a noise")

    def introduction(self):
        return f"My name is {self.name}, I am {self.get_age()} years old"

Bob = Animal("Bob", 3)
print(Bob.get_age())
print(Bob.introduction())


#Pillars of OOP: Abstraction, Inheritance, Polymorphism, Encapsulation
# Abstraction - the idea of showing only what the user needs to know and hiding the implementation details
# Inheritance - child classes can be resused and extend the bahviour of our parent classes
# Polymorphism - (many forms) meaning one interface but multiple implementation
# Encapsulation - the practice of bundling data/attributes and methods into a single unit and
#   restricting access to some of the object's components

#Inheritance demonstration - inheriting from Animal class
class Dog(Animal):
    def __init__(self, name, age, breed, color="Brown", **kwargs):    # "=" allows us to set default values
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.breed = breed
        self.color = color
    
    # Polymorphism example - we are overriding the definintion of the speak function
    def speak(self):
        return f"{self.name} barked at the mailman"
    
    #__str__ acts as our toString() method
    def __str__(self):
        return f"My name is {self.name}, I am a {self.color} {self.breed}."
    

Major = Dog("Major", 7, "German Shepard", "Black")
print(Major.speak())
print(Major)

class other:
    def __init__(self, place, time, **kwargs):
        super().__init__(**kwargs)
        self.place = place
        self.time = time
    
    def speak(self):
        return "This is from the other class"


#Classes can inherit from multiple classes using a "," seperated list
class Cat(other, Dog):
    def __init__(self, name, age, breed, color, hairLength, place, time):
        #using the super method we can call the Parent class constructor
        super().__init__(name = name, age = age, breed = breed, color = color, place = place, time = time)
        self.hairLength = hairLength

    def scratch(self):
        return f"{self.name} has scratched the doorframe"
    
    # def speak(self):
    #     return f"{self.name} meowed at the door"
    
Ash = Cat("Ash", 2, "Maine Coone", "Gray", "Medium Hair", "Here", "Now")
print(Ash.scratch())
print(Ash.speak())
# print(Ash.__age) throws an error because the property is private
print(Ash.get_age())
Ash.set_age(3)
print(Ash.get_age())