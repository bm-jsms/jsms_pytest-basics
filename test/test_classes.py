from src.classes import Person

def test_greet():
    person = Person("Josué", 20)
    greeting = person.greet()
    assert greeting == "Hello, my name is Josué and I am 20 years old."

def test_celebrate_birthday():
    person = Person("Josué", 20)
    person.celebrate_birthday()
    assert person.age == 21

def test_get_age():
    person = Person("Josué", 20)
    age = person.get_age()
    assert age == 20