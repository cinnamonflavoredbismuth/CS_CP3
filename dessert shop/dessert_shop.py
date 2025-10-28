#CS Dessert Shop
from dessert import *
import tabulate
#test
data = [["Bruce Wayne","Batman",3957208537],
        ["Oliver Queen","Green Arrow",2938475623],
        ["Clark Kent","Superman",654],
        ["Barry Allen","Flash",1], 
        ["J'onn J'onzz","Unemployed",32]]
#print(tabulate.tabulate(data, headers=["name","job","number"]))
def int_input():
    while True:
        try:
            num=int(input("Enter a number: "))
            break
        except:
            print("Invalid input. Please enter a valid integer.")
    return num

def float_input():
    while True:
        try:
            num=float(input("Enter a number: "))
            break
        except:
            print("Invalid input. Please enter a valid number.")
    return num


def main():
    order=Order([])
    '''order.add(Candy("Sucker",5,2))
    order.add(Cookie("Chocolate Chip",24,2))
    order.add(IceCream("Chocolate",1,.5))
    order.add(Sundae("Banana Split",3,.5,"Banana",3))'''
    while True:
        dessert=int_input("What would you like to add to your order?\n1. Candy\n2. Cookie\n3. Ice Cream\n4. Sundae\n5. Finish Order\n")
        if dessert==1:
            name=input("Enter the name of the candy: ")
            weight=float_input("Enter the weight of the candy (in pounds): ")
            price=float_input("Enter the price per pound: ")
            candy=Candy(name,weight,price)
            order.add(candy)
        if dessert == 2:
            name=input("Enter the name of the cookie: ")
            dozens=int_input("Enter the how many dozens you want: ")
            price=float_input("Enter the price per dozen: ")
            cookie=Cookie(name,dozens,price)
            order.add(cookie)
        if dessert == 3:
            name=input("Enter the name of the ice cream: ")
            scoops=int_input("Enter the number of scoops: ")
            price=float_input("Enter the price per scoop: ")
            ice_cream=IceCream(name,scoops,price)
            order.add(ice_cream)
        if dessert == 4:   
            name=input("Enter the name of the sundae: ")
            scoops=int_input("Enter the number of scoops: ")
            price=float_input("Enter the price per scoop: ")
            topping_name=input("Enter the topping name: ")
            topping_price=float_input("Enter the topping price: ")
            sundae=Sundae(name,scoops,price,topping_name,topping_price)
            order.add(sundae)
        if dessert == 5:
            break

    data=[]
    for x in order.order:
        data.append([x.name,x.calculate_cost(),x.calculate_tax()])
    data.append(["Subtotal",order.order_cost(),f'{order.order_tax():.2f}'])
    data.append(["Total",(order.order_cost()+order.order_tax()),''])
    print(tabulate.tabulate(data,headers=["Name","Cost","Tax"]))
main()