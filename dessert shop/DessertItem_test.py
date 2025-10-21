from dessert import *
#Write three test cases for each class: default values, provided values, and updated values.
def DessertItem_test():
    item=DessertItem()
    assert item.name == ''
    second_item=DessertItem("cheetos")
    assert second_item.name == "cheetos"
    second_item.name = "Children"
    assert second_item.name == "Children"
DessertItem_test()