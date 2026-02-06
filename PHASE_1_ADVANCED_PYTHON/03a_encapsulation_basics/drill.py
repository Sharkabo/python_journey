# Drills - Encapsulation Basics
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a Person class with name (public) and age (protected with _age)
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self._age = age
# Drill 2: Create a Product class with name and private price using __price (name mangling)
class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.__price = price
# Drill 3: Create a Student class with public id, protected _grade, and private __ssn
class Student:
    def __init__(self, id, grade, ssn) -> None:
        self.id = id
        self._grade = grade
        self.__ssn = ssn
# Drill 4: Create a Car class with public brand and protected _mileage
class Car:
    def __init__(self, brand, mileage) -> None:
        self.brand = brand
        self._mileage = mileage
# Drill 5: Create a Temperature class with private __celsius and a getter method
class Temperature:
    def __init__(self, celsius) -> None:
        self.__celsius = celsius
    
    def get_celsius(self) -> float:
        return self.__celsius
# Drill 6: Create a Book class with public title and private __isbn
class Book:
    def __init__(self, title, isbn) -> None:
        self.title = title
        self.__isbn = isbn
# Drill 7: Create a Circle class with private __radius and a method to calculate area
import math
class Circle:
    def __init__(self, radius) -> None:
        self.__radius = radius
    
    def calculate_area(self) -> float:
        return math.pi * self.__radius ** 2
# Drill 8: Create an Email class with public address, private __password, and verify method
class Email:
    def __init__(self, address, password) -> None:
        self.address = address
        self.__password = password
    
    def verify_password(self):
        input_password = input('Please input the password')
        if input_password == self.__password:
            return True
        else:
            return False
# Drill 9: Create a Counter class with private __count, increment() and get_count()
class Counter:
    def __init__(self, count) -> None:
        self.__count = count

    def get_count(self) -> float:
        return self.__count
    
    def increment(self, amount: float) -> None:
        if isinstance(amount, (int, float)):
            self.__count += amount
        else:
            raise ValueError('Please input number and number only')
# Drill 10: Create a Wallet class with private __amount, add_money(), remove_money(), get_balance()
class Wallet:
    def __init__(self, amount, ) -> None:
        self.__amount = amount

    def get_balance(self) -> float:
        return self.__amount  

    def add_money(self, income) -> None:
        if isinstance(income, (int, float)):
            self.__amount += income
        else:
            raise ValueError('Please input number and number only')
        
    def remove_money(self, cost) -> None:
        if not isinstance(cost, (int, float)):
            raise ValueError('Please input number and number only')
        
        if cost <= 0:
            raise ValueError('Cost must be positive')
        
        if cost > self.__amount:
            raise ValueError('The cost is greater than what you have')
        
        self.__amount -= cost