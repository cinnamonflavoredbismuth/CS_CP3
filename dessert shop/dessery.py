#CS Dessert shop
"""Create a separate folder (or repository) called Dessert Shop
Create a file named "dessert.py" containing the following classes: DessertItem, Candy, Cookie, IceCream, and Sundae.
Implement the DessertItem class as the parent class with a 'name' attribute and constructor.
Create Candy, Cookie, and IceCream classes as subclasses of DessertItem, each with their specific attributes and constructors.
Implement the Sundae class as a subclass of IceCream with additional attributes for toppings.
Ensure all classes have appropriate default values for their attributes.
Create an Order class in the same file with methods to add items and get the order length.
Create a separate file named "dessert_shop.py" to test the classes.
In dessert_shop.py, import the classes from dessert.py and create a main() function.
In the main() function, create an Order instance and add various dessert items to it.
Print the name of each DessertItem in the order and the total number of items.
Create separate test files for each class (DessertItem, Candy, Cookie, IceCream, Sundae) using pytest.
Write three test cases for each class: default values, provided values, and updated values.
Ensure proper Python syntax, including correct indentation and method definitions.
Use meaningful variable and method names for code clarity.
Add comments to explain code logic where necessary.
Test all classes thoroughly to ensure required functionality works as expected."""

class DessertItem:
    def __init__(self,name=''):
        self.name=name

class Candy(DessertItem):
    def __init__(self,name,candy_weight=0.0,price_per_pound=0.0):
        super().__init__(name)
        self.candy_weight=candy_weight
        self.price_per_pound=price_per_pound

class Cookie(DessertItem):
    def __init__(self,name,quantity=0,price_per_dozen=0.0):
        super().__init__(name)
        self.quantity=quantity
        self.price_per_dozen=price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name,scoop_count=0,price_per_scoop=0.0):
        super().__init__(name)
        self.scoop_count=scoop_count
        self.price_per_scoop=price_per_scoop

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop,topping_name=
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 ,topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name=topping_name
        self.topping_price=topping_price
        
class Order:
    def __init__(self,order):
        self.order=order
    def add(self,item):
        self.order.append(item)