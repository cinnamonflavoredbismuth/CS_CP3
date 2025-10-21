from dessert import *
#Write three test cases for each class: default values, provided values, and updated values.
def IceCream_test():
    item=IceCream()
    assert item.name == ''
    assert item.scoop_count==0
    assert item.price_per_scoop==0.0

    item=Cookie("cheetos",1,1)
    assert item.name == "cheetos"
    assert item.scoop_count==1
    assert item.price_per_scoop==1

    item.name='children'
    item.scoop_count=2
    item.price_per_scoop=2

    assert item.name == "children"
    assert item.scoop_count==2
    assert item.price_per_scoop==2

IceCream_test()