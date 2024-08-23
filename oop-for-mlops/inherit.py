# Simple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says something")
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(f"{self.name} says meow!")

dog = Dog("Dog")
cat = Cat("Cat")

dog.speak()
cat.speak()