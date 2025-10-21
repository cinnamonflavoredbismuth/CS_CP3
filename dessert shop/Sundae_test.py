from dessert import *
#Write three test cases for each class: default values, provided values, and updated values.
def Sundae_test():
    item=Sundae()
    assert item.name == ''
    assert item.scoop_count==0
    assert item.price_per_scoop==0.0
    assert item.topping_name == ''
    assert item.topping_price == 0.0

    item=Sundae("cheetos",1,1,'orange',1)
    assert item.name == "cheetos"
    assert item.scoop_count==1
    assert item.price_per_scoop==1
    assert item.topping_name == 'orange'
    assert item.topping_price == 1

    item.name='children'
    item.scoop_count=2
    item.price_per_scoop=2
    item.topping_name='hair'
    item.topping_price=2

    assert item.name == "children"
    assert item.scoop_count==2
    assert item.price_per_scoop==2
    assert item.topping_name == 'hair'
    assert item.topping_price == 2

Sundae_test()