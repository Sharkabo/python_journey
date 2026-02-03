# Unit 03: Encapsulation and Properties

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python encapsulation tutorial"
- "Python @property decorator"
- "Python getter setter"
- "Python 封裝概念"
- "Python property 裝飾器"

Recommended Channels:
- Corey Schafer (Python)
- Tech With Tim (Python)
- freeCodeCamp.org
- 彭彭的課程 (Chinese)

---

## 1. What is Encapsulation?

Encapsulation is the OOP principle of bundling data (attributes) and methods together, while controlling access to that data. It's about hiding internal details and only exposing what's necessary.

**Key Benefits:**
- Protect data from accidental modification
- Control how data is accessed and changed
- Add validation when setting values
- Change internal implementation without breaking external code

**Visibility Conventions in Python:**
- `public_attribute`: Accessible from anywhere (default)
- `_protected_attribute`: Intended for internal use (convention, not enforced)
- `__private_attribute`: Name mangling applied, harder to access from outside

**Example:**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._account_number = "12345"  # Protected (by convention)
        self.__balance = balance        # Private (name mangled)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

# Using the class
account = BankAccount("Alice", 1000)
print(account.owner)           # Alice (public, OK)
print(account._account_number) # 12345 (still accessible, but you shouldn't)
# print(account.__balance)     # AttributeError (private, protected)
print(account.get_balance())   # 1000 (access through method)
```

**Important Note:**
Python's "privacy" is more about convention than enforcement. The single underscore `_` means "please don't access this directly" but doesn't prevent it. The double underscore `__` makes it harder but still not impossible.

---

## 2. The @property Decorator

The `@property` decorator allows you to define methods that can be accessed like attributes. This gives you control over how attributes are accessed and modified while keeping a clean syntax.

**Why use @property?**
- Add validation when setting values
- Compute values on the fly
- Maintain backward compatibility when changing implementation
- Make read-only attributes
- Keep the clean attribute access syntax

**Basic Syntax:**
```python
class ClassName:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        """Getter method"""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Setter method"""
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value
```

**Example:**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit (computed)"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self._celsius = (value - 32) * 5/9

# Using the class
temp = Temperature(25)
print(temp.celsius)      # 25 (calls the getter)
print(temp.fahrenheit)   # 77.0 (computed from celsius)

temp.celsius = 30        # Calls the setter with validation
print(temp.celsius)      # 30
print(temp.fahrenheit)   # 86.0

temp.fahrenheit = 32     # Set using Fahrenheit
print(temp.celsius)      # 0.0 (automatically converted)

# temp.celsius = -300    # ValueError: Temperature below absolute zero!
```

---

## 3. Getter and Setter Methods

Before `@property` was available, Python used explicit getter and setter methods. Understanding this helps you appreciate `@property` and recognize it in older code.

**Old Style (Explicit Methods):**
```python
class OldStylePerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0 or age > 150:
            raise ValueError("Invalid age")
        self._age = age

# Usage
person = OldStylePerson("Alice", 30)
print(person.get_name())  # Alice
person.set_age(31)
print(person.get_age())   # 31
```

**New Style (Using @property):**
```python
class ModernPerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value

# Usage (cleaner syntax)
person = ModernPerson("Alice", 30)
print(person.name)  # Alice (looks like attribute access)
person.age = 31     # Looks like assignment, but calls setter
print(person.age)   # 31
```

---

## 4. Read-Only Properties

You can create read-only properties by defining only the getter without a setter.

**Example:**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def diameter(self):
        """Read-only property (no setter)"""
        return self._radius * 2
    
    @property
    def area(self):
        """Read-only property (computed)"""
        return 3.14159 * self._radius ** 2

# Using the class
circle = Circle(5)
print(circle.radius)    # 5
print(circle.diameter)  # 10
print(circle.area)      # 78.53975

circle.radius = 10      # OK, has setter
print(circle.diameter)  # 20 (automatically updated)

# circle.diameter = 20  # AttributeError: can't set attribute
# circle.area = 100     # AttributeError: can't set attribute
```

---

## 5. Encapsulation with Inheritance

Encapsulation works together with inheritance. Protected attributes (single underscore) are meant to be accessible by child classes, while private attributes (double underscore) are not.

**Example:**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance      # Protected, child classes can access
        self.__transaction_fee = 0   # Private to this class
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        # Can access _balance (protected)
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        
        # Cannot easily access __transaction_fee (private to parent)
        # self.__transaction_fee would create a new attribute, not access parent's

# Using the classes
savings = SavingsAccount("Bob", 1000, 0.05)
print(savings.balance)      # 1000
savings.add_interest()
print(savings.balance)      # 1050.0
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01: You learned to create classes with attributes
- Unit 02: You learned inheritance, where child classes access parent attributes
- Unit 03: Now you're learning to control and protect access to those attributes

**Preparation for Next Lesson:**
- Unit 04 will cover Magic Methods (dunder methods)
- Properties actually use magic methods `__get__`, `__set__`, `__delete__` behind the scenes
- Understanding encapsulation helps you appreciate why some magic methods exist

**Real-World Application:**
- Pydantic models (used in FastAPI) heavily use properties and validation
- Database ORMs use properties to sync with database fields
- Properties let you add validation without changing how code looks
- This is essential for building maintainable APIs
