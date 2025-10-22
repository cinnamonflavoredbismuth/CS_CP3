#CS Dessert Shop
from dessert import *
def main():
    order=Order([])
    order.add(Candy("Sucker",5,2))
    order.add(Cookie("Chocolate Chip",24,2))
    order.add(IceCream("Chocolate",1,.5))
    order.add(Sundae("Banana Split","3",".5","Banana",3))
    
    for i in order.order:
        print(f"You Ordered: {i.name}")
    print(f"Your total order length was: {len(order.order)}")
main()