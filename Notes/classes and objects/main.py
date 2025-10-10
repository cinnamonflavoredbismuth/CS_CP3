#CS Classes and Objects
"""What is a class?
   a blueprint for an object
What is an object?
    a thing
How is a class a form of encapsulation? 
    puts all the pieces of one thing in one place
How is a class an abstraction of an object?
    one level further from the specifics
How do you access information in an object?
    object.attribute
How do you initialize a class?
    class Class():
How do you set a default value 
    def __init__(value=1): (must be the last one on the list)
How do you use type hinting?
    method: type
How do you set an attribute to be private?
    _attribute
How do you make a class method?
    def Method(self):
Why do we include docstrings/
    so people know what the class or method does
What does "self" do as a parameter for class methods?
    it makes it so you can access the attributes and methods of the class, and only use it for current instance
What are getter and setter methods?
    a getter method gets the value, while a setter sets the value
What are magic methods?
    methods that have __ before and after them
Where are class objects saved? (heap or stack?)
    heap
"""

class Person():
    """Person class with first and last names as well as age
    full name returns the full name of a person
    there are ways to display the age and change the age by 1"""
    first_name: str
    last_name: str
    age: int
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return f"name: {self.full_name()} age:{self.age}"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def setAge(self):
        self.age += 1
    def getName(self):
        return self.full_name()


tia = Person("Tia","LaRose",28)
alex = Person("Alex","LaRose",37)
print(tia)
print(tia)