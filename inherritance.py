# inherritance in Python

class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    pass

dog = Dog();
cat = Cat();
dog.walk()
dog.bark()
cat.walk()