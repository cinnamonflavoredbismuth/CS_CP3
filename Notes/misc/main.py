# CS misc notes
 
# Named Tuples

from collections import namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])

    
color=Color(50,100,150)
print(color.red)

# dataclasses. automatically initilizes attributes
from dataclasses import dataclass, field
# frozen makes it read only
@dataclass(order=True,frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False) # field not included in init method
    name: str
    age: int
    city: str

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.age) # set sort_index to age for ordering

person1= Person("John", 60, "New York")
person2= Person("Jane", 30, "San Francisco")
# you can compare two dataclass objects directly
# you can also print them directly

print(person1)
print(person1 == person2)
print(person1 < person2)

# sorting

people = [person2, person1]
nums = [5,2,9,1]
sorted_nums=sorted(nums,reverse=True)
print(sorted_nums)

# lambda [info going in]: [info going out]. single line function
# attrgetter: built in lambda
from operator import attrgetter
sort_people = sorted(people,key=attrgetter('city'))
print(sort_people)

# args 
#  has to be the very last one

def hello(age,*names):
    print(age)
    for name in names:
        print(f'hello, {name}') 

# kwargs makes your input a dicitonary, and makes it so some can be optional
def another(names):
    if 'mname' in names.keys():
        print(f"hello {names['fname']} {names['mname']} {names['lname']}")
    else:
        print(f"hello {names['fname']} {names['lname']}")

# another(fname="jake",mname="howard",lname="wayne")

hello(1,'tiffany','stewart','elmo')