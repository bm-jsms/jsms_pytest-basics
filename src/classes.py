class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def celebrate_birthday(self):
        self.age += 1
    
    def get_age(self):
        return self.age