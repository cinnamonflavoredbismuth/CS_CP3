#CS Parent and Child Classes
"""
What is a parent/abstract class?
    a broader class that includes other classes inside it
How do you create a child class?
    class child(Parent)
How does a child class inherit from the parent class?
    it has all the same methods
What are class diagrams?
    when you have a diagram of a class with methods determining their information (public, private, type, ect)
How are class diagrams used to show a parent/child relationship?
    a child has a white arrow pointing to a parent
How do you overload operators in a class?
    you see if they are the same thing
What are test cases?
    testing the minimum and maximum limits of the function to see if they work normally
Why do we use test cases?
    so you can see the limits of the program and make sure the classes don't break
How do we create test cases?
    different file, same folder. test_filename.py, filename_test.py
"""

class Animal():
    def __init__(self,age,color):
        self.age=age
        self.color=color
    def move(self):
        pass
    def __str__(self):
        return f'age: {self.age}, color: {self.color}'
    def __eq__(self, other):
        return (self.age==other.age and self.color==other.color)
    
class dog(Animal):
    def __init__(self,age,color,owner,breed,name):
        super().__init__(age,color)
        self.owner=owner
        self.breed=breed
        self.name=name
    def __str__(self): 
        return f'name: {self.name}, age: {self.age}, color: {self.color}, owner: {self.owner}, breed: {self.breed}'
    def __eq__(self, other):
        return (self.age==other.age and 
                self.color==other.color and
                self.owner==other.owner and
                self.breed==other.breed and
                self.name==other.name)
    def move(self):
        print(f"{self.name} runs")
    
bobby = dog(5,"brown","jill","bulldog","bobby")
birdy = dog(1, "black", "Nikkie","Lab","birdy")
alex = Animal(16,"white")
nick = Animal(16,"white")
bobby.move()
print(bobby)
print(alex)

print(alex==nick)
print(bobby==birdy)