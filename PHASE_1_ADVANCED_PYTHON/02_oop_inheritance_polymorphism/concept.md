# Unit 02: Inheritance and Polymorphism

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python inheritance tutorial"
- "Python polymorphism explained"
- "Python super() method"
- "Python 繼承教學"
- "Python 多型概念"

---

## 1. What is Inheritance?

Inheritance is a fundamental OOP concept that allows a class to inherit attributes and methods from another class. This promotes code reuse and creates a hierarchical relationship between classes.

**Key Terms:**
- **Parent Class (Base Class)**: The class being inherited from
- **Child Class (Derived Class)**: The class that inherits from the parent
- **Subclass**: Another term for child class
- **Superclass**: Another term for parent class

**Why use Inheritance?**
- Reuse existing code instead of duplicating it
- Create specialized versions of existing classes
- Establish logical relationships between classes
- Easier to maintain and update code

**Syntax:**
```python
class ParentClass:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def parent_method(self):
        return "This is from parent"

class ChildClass(ParentClass):  # Inherit from ParentClass
    def child_method(self):
        return "This is from child"
```

**Example:**
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Some generic sound"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):  # Override parent method
        return "Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} is fetching the ball"

class Cat(Animal):  # Cat also inherits from Animal
    def make_sound(self):  # Override parent method
        return "Meow!"
    
    def scratch(self):  # New method specific to Cat
        return f"{self.name} is scratching"

# Using the classes
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

print(dog.get_info())      # Buddy is 3 years old (inherited)
print(dog.make_sound())    # Woof! (overridden)
print(dog.fetch())         # Buddy is fetching the ball

print(cat.get_info())      # Whiskers is 2 years old (inherited)
print(cat.make_sound())    # Meow! (overridden)
print(cat.scratch())       # Whiskers is scratching
```

---

## 2. Using super() to Call Parent Methods

The `super()` function allows you to call methods from the parent class. This is especially useful when you want to extend parent functionality rather than completely replacing it.

**Syntax:**
```python
class ChildClass(ParentClass):
    def __init__(self, child_param, parent_param):
        super().__init__(parent_param)  # Call parent's __init__
        self.child_param = child_param
```

**Example:**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent __init__
        self.department = department    # Add new attribute
    
    def get_details(self):
        # Use parent's get_details and add more info
        parent_details = super().get_details()
        return f"{parent_details}, Department: {self.department}"

# Create a manager
manager = Manager("Alice", 80000, "Engineering")
print(manager.get_details())
# Output: Employee: Alice, Salary: $80000, Department: Engineering
```

**Why use super()?**
- Avoid code duplication
- Make code more maintainable
- Properly initialize parent class attributes
- Essential for multiple inheritance scenarios

---

## 3. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method that exists in the parent class.

**Example:**
```python
class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        return 0  # Default implementation
    
    def describe(self):
        return f"A {self.color} shape with area {self.area()}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):  # Override parent's area method
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):  # Override parent's area method
        return 3.14159 * self.radius ** 2

# Using the classes
rectangle = Rectangle("red", 10, 5)
circle = Circle("blue", 7)

print(rectangle.describe())  # A red shape with area 50
print(circle.describe())     # A blue shape with area 153.93804
```

---

## 4. Polymorphism

Polymorphism means "many forms". In OOP, it refers to the ability to use objects of different classes through the same interface. The same method name can behave differently depending on which object calls it.

**Key Benefit:**
- Write code that works with parent class but accepts any child class
- More flexible and extensible code

**Example:**
```python
class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def process(self):
        return "Processing payment"

class CreditCard(Payment):
    def process(self):
        return f"Processing ${self.amount} via Credit Card"

class PayPal(Payment):
    def process(self):
        return f"Processing ${self.amount} via PayPal"

class BankTransfer(Payment):
    def process(self):
        return f"Processing ${self.amount} via Bank Transfer"

# Polymorphism in action
def execute_payment(payment):
    # This function doesn't care what type of payment it is
    # It just calls process() and gets the right behavior
    print(payment.process())

# All these different payment types work with the same function
payments = [
    CreditCard(100),
    PayPal(50),
    BankTransfer(200)
]

for payment in payments:
    execute_payment(payment)

# Output:
# Processing $100 via Credit Card
# Processing $50 via PayPal
# Processing $200 via Bank Transfer
```

**Checking Object Types:**
```python
# Check if an object is an instance of a class
dog = Dog("Max", 5)
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog inherits from Animal)
print(isinstance(dog, Cat))     # False

# Check if a class is a subclass of another
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True
print(issubclass(Dog, Cat))     # False
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- In Unit 01, you learned how to create classes with `__init__` and methods
- Inheritance builds on this by allowing classes to share and extend functionality
- You've been using inheritance without knowing it (all classes inherit from `object`)

**Preparation for Next Lesson:**
- Unit 03 will teach Encapsulation and Properties
- You'll learn how to protect data in parent and child classes
- Understanding inheritance is essential for proper encapsulation
- Properties work with inherited attributes

**Real-World Application:**
- FastAPI uses inheritance for custom exception classes
- Database models often use inheritance for shared fields
- This is the foundation for building maintainable, scalable applications
