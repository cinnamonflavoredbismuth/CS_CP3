#CS Abstraction Notes
'''
Why can't you create an object from an abstract class?
    because it is used as a parent class
How do abstract classes and abstract methods work together?
    abstract classes are just parent classes
What does abc stand for?
    abstract base class
What are decorators? 
    designed to give further information to the computer
What is an abstract method?
    placeholder method
What is a concrete method?
    a normal method
What is an abstract class?
    A placeholder/ghost class (no objects. exists only to be a parent class). must have at least 1 abstract method
How do you make an abstract method?
    @abstractmethod
    def ...
How can you create a class that inherits from multiple parent classes?
    class name(mom,dad)
Why does the inheritance order matter?
    the first one takes higher precedence
What does the mro() method do when you call it on a class?
    it tells you what resolution of the method takes precedence
What is Method resolution order?
    it is the inheritence order
''' 
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self,name):
        super().__init__()
        self.name=name
    
    def __str__(self):
        return self.name

    @abstractmethod
    def move(self):
        pass

class Quadrapeds(Animal):
    def __init__(self,name):
        super().__init__(name)
    def move(self):
        print(f"{self.name} can walk or run")

class Aquatic(Animal):
    def __init__(self, name):
        super().__init__(name)
    def move(self):
        print(f"{self.name} can swim")

class Sealion(Aquatic,Quadrapeds):
    def __init__(self, name):
        super().__init__(name)
    def eats(self):
        print(f"{self.name} eats penguins")


sealion = Sealion('greg')
print(sealion)
print(Aquatic.mro())
