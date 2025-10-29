#CS Dessert Shop
from dessert import *
import tabulate


#tabulation practice
'''data = [["Bruce Wayne","Batman",3957208537],
        ["Oliver Queen","Green Arrow",2938475623],
        ["Clark Kent","Superman",654],
        ["Barry Allen","Flash",1], 
        ["J'onn J'onzz","Unemployed",32]]'''
#print(tabulate.tabulate(data, headers=["name","job","number"]))

#helper functions for user inpput
def int_input(message="Enter a number: "):
    while True:
        try:
            num=int(input(message))
            if num>=0:
                break
            else:
                print("Please enter a non-negative integer.")
        except:
            print("Invalid input. Please enter a valid integer.")
    return int(num)

def float_input(message="Enter a number: "):
    while True:
        try:
            num=float(input(message))
            if num>=0:
                break
            else:
                print("Please enter a non-negative number.")
        except:
            print("Invalid input. Please enter a valid number.")
    return float(num)


#Input handling
class DessertShop():
    def __init__(self):
        pass

    def user_prompt_candy(self):
        name=input("Enter the name of the candy: ")
        weight=float_input("Enter the weight of the candy (in pounds): ")
        price=float_input("Enter the price per pound: ")
        candy=Candy(name,weight,price)
        print("successfully added")
        return candy
    
    def user_prompt_cookie(self):
        name=input("Enter the name of the cookie: ")
        dozens=int_input("Enter the how many dozens you want: ")
        price=float_input("Enter the price per dozen: ")
        cookie=Cookie(name,dozens,price)
        print("successfully added")
        return cookie
    
    def user_prompt_icecream(self):
        name=input("Enter the name of the ice cream: ")
        scoops=int_input("Enter the number of scoops: ")
        price=float_input("Enter the price per scoop: ")
        ice_cream=IceCream(name,scoops,price)
        print("successfully added")
        return ice_cream
    
    def user_prompt_sundae(self):
        name=input("Enter the name of the sundae: ")
        scoops=int_input("Enter the number of scoops: ")
        price=float_input("Enter the price per scoop: ")
        topping_name=input("Enter the topping name: ")
        topping_price=float_input("Enter the topping price: ")
        sundae=Sundae(name,scoops,price,topping_name,topping_price)
        print("successfully added")
        return sundae


'''
Code to implement the main loop of terminal-based user interface for
Dessert Shop Part 4. Students should be able to paste this code into their own
main() method as-is and use it without change.
Author: George Rudolph
Date: 2 Jun 2023
'''
def main():
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
    '1: Candy',
    '2: Cookie',
    '3: Ice Cream',
    '4: Sundae',
    '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])
    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()

    for x in order.order:
        data.append([x.name,x.calculate_cost(),x.calculate_tax()])
    data.append(["Subtotal",order.order_cost(),f'{order.order_tax():.2f}'])
    data.append(["Total",(order.order_cost()+order.order_tax()),''])
    print(tabulate.tabulate(data,headers=["Name","Cost","Tax"]))
main()