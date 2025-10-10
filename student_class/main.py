#CS Student Class
"""Write a program that uses a class to abstract a student. 
Students need to have a student id, name, and grade. 
The student class should have an __init__ method to initialize the values. 
Have the id default to 000, name to John Doe and grade to 100. 
Make a getter function that will display the student's grade.
Make a setter function that will change the student's grade. 
Create at least 5 student objects.
Print each object (note that means you will need a __str__ method), change the grades of at least 3 students and then use the getter method to display the new grades. """


class Student:
    def __init__(self,id = 100,name = "John Doe",grade = 100):
        self.id = id
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Grade: {self.grade}"
    def display_grade(self):
        return f"{self.name}'s grade: {self.grade}"
    def new_grade(self,new_grade):
        self.grade = new_grade
    


def main():
    students=[Student(1,"John",50),Student(2,"Jane",60),Student(3,"Jim",70),Student(4,"Jill",80),Student(5,"Jack",90)]
    for i in range(len(students)):
        print(students[i])
    for i in range(len(students)):
        students[i].new_grade(100)
    print("New grades:")
    for i in range(len(students)):
        print(f" {students[i].display_grade()}")
    return
main()