class Dog:
    species = "Canis familiaris"  # class variable
    count = 0  # class variable to count instances

    def __init__(self, name, age):
        self.name = name          # instance variable
        self.age = age
        Dog.count += 1           # increment count when a new dog is created

    def bark(self):
        return f"{self.name} says Woof!"
    
    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

d1 = Dog("Bruno", 3)
d2 = Dog("Max", 5)
print(d1)
print(d2.bark())
print(Dog.species)  # accessed on class

print(d1.species)   # also accessible on instance

print(d1.birthday())
print(d1)

print(f"Total number of dogs: {Dog.count}")
print(Dog.count)   # should print 2
d3 = Dog("Rocky", 2)
print(Dog.count)   # should print 3
