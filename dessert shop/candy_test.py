from dessert import *
#Write three test cases for each class: default values, provided values, and updated values.
def candy_test():
    item=Candy()
    assert item.name == ''
    assert item.candy_weight==0.0
    assert item.price_per_pound==0.0

    item=Candy("cheetos",1,1)
    assert item.name == "cheetos"
    assert item.candy_weight==1
    assert item.price_per_pound==1

    item.name='children'
    item.candy_weight=2
    item.price_per_pound=2

    assert item.name == "children"
    assert item.candy_weight==2
    assert item.price_per_pound==2

candy_test()