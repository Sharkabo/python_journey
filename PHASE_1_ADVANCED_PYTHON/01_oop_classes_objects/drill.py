# Drills - OOP Basics: Classes and Objects
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a simple class called Dog with attributes name and age
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Drill 2: Add an __init__ method to initialize name and age


# Drill 3: Create a method called bark() that prints "{name} says Woof!"
    def bark(self):
        print(f'{self.name} says Woof!')

# Drill 4: Create two Dog objects with different names and ages
Shepherd = Dog('Corrine', 23)
German_Shepherd = Dog('Ian', 24)

# Drill 5: Call the bark() method on both dogs
Shepherd.bark()
German_Shepherd.bark()
# Drill 6: Create a class Car with attributes: brand, model, year
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
# Drill 7: Add a method get_age() that calculates how old the car is (2026 - year)
    def get_age(self, current_year):
        age = current_year - self.year
        return age
# Drill 8: Create a class BankAccount with balance attribute (starting at 0)
class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

# Drill 9: Add deposit(amount) and withdraw(amount) methods to BankAccount
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print('You don\'t have enough money.')
            return False

# Drill 10: Add a get_balance() method that returns the current balance
    def get_balance(self):
        return self.balance