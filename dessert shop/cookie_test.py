from dessert import *
#Write three test cases for each class: default values, provided values, and updated values.
def cookie_test():
    item=Cookie()
    assert item.name == ''
    assert item.quantity==0
    assert item.price_per_dozen==0.0

    item=Cookie("cheetos",1,1)
    assert item.name == "cheetos"
    assert item.quantity==1
    assert item.price_per_dozen==1

    item.name='children'
    item.quantity=2
    item.price_per_dozen=2

    assert item.name == "children"
    assert item.quantity==2
    assert item.price_per_dozen==2

cookie_test()