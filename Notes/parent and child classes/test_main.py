from main import *
def test_Animal_set():
    test_animal = Animal(0,"None")
    assert test_animal.age == 0
    assert test_animal.color == "None"