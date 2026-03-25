class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"Animal({self.name})"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # reuse parent init
        self.breed = breed

    def fetch(self):
        return f"{self.name} fetches the ball!"

class Cat(Animal):
    def __init__(self, name, indoor):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def speak(self):  # override parent method
        return f"{self.name} says Purrr... (not just Meow)"

d = Dog("Bruno", "Labrador")
c = Cat("Whiskers", True)
print(d.speak())   # inherited from Animal
print(d.fetch())   # Dog's own method
print(c.speak())   # Cat's overridden version

animals=  [Animal("Generic", "Sound"), Dog("Rex", "German Shepherd"),
            Cat("Mittens", False)]
for a in animals:
    print(a)        # __str__ method from Animal
    print(a.speak()) # speak method, overridden in Cat but not in Dog

class bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name, "Tweet")
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says {self.sound} and {'can fly' if self.can_fly else 'cannot fly'}"
    
b = bird("Tweety", True)
print(b.speak())  # bird's own speak method

print(isinstance(d, Animal))  # True, Dog is a subclass of Animal
print(isinstance(c, Dog))     # False, Cat is not a Dog
print(issubclass(Dog, Animal))  # True, Dog is a subclass of Animal
print(issubclass(Cat, Dog))     # False, Cat is not a subclass
print(issubclass(bird, Animal)) # True, bird is a subclass of Animal
print(issubclass(bird, Dog))    # False, bird is not a subclass of Dog
