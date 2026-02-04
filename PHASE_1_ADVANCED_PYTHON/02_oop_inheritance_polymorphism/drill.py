# Drills - Muscle Memory Training
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a Vehicle parent class with __init__(brand, model) and a describe() method that returns a description string. Then create a Car child class that inherits from Vehicle.
class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def describe(self) -> str:
        return f'This Car is {self.brand}\'s {self.model}'
# Drill 2: In the Car class from Drill 1, override the __init__ to accept brand, model, and num_doors. Use super().__init__() to call the parent's __init__, then add num_doors as a new attribute.
class Car(Vehicle):
    def __init__(self, brand, model, num_doors) -> None:
        super().__init__(brand, model)
        self.num_doors = num_doors
# Drill 3: Create a Calculator parent class with an add(a, b) method. Create a ScientificCalculator child class that inherits from Calculator and adds a power(base, exponent) method.
class Calculator: 
    def add(self, a, b) -> float:
        return float(a + b)

class ScientificCalculator(Calculator):
    def power(self, base, exponent):
        return float(base ** exponent)
# Drill 4: Create a Bird parent class with a move() method that returns "Flying". Create two child classes: Penguin (override move to return "Swimming") and Eagle (keep the inherited move method).
class Bird:
    def move(self) -> str:
        return 'Flying'

class Penguin(Bird):
    def move(self) -> str:
        return 'Swimming'

class Eagle(Bird):
    def move(self) -> str:
        return super().move()
# Drill 5: Create a function called describe_animal(animal) that takes any animal object and calls its make_sound() method. Test it with at least two different animal types that have different make_sound() implementations (demonstrating polymorphism).
class Cat:
    def make_sound(self) -> str:
        return 'Meow~'
    
class Dog:
    def make_sound(self) -> str:
        return 'Woof! Woof!'
    
def describe_animal(animal):
    print(f'The animal says:{animal.make_sound()}')

kitty = Cat()
doggy = Dog()

describe_animal(kitty)
describe_animal(doggy)