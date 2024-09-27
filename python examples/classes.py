from typing import Any


class Dog():
    species = "mammal"
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    def bark(self, number):
        return number * "Hał " + f"My name is {self.name}"

my_dog = Dog(breed="Lab", name="Jabjadoj")

print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

print(my_dog.bark(2))



class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = Circle.pi * radius**2
    def __str__(self) -> str:
        return f"radius = {self.radius}, area = {self.area}, get_cicrumference = {self.get_cicrumference()}"
    def __eq__(self, other):
        return self.radius == other.radius    
    def __del__(self):
        print(f"Obiekt{__class__} został usunięty.")

    def get_cicrumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(radius=5)
other_circle = Circle(radius=4)

print(my_circle == other_circle)

# print(my_circle.radius)
# print(my_circle.pi)
# print(my_circle.area)
# print(my_circle.get_cicrumference())
print(my_circle)