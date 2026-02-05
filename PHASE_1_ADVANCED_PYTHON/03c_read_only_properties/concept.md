# Unit 03c: Read-Only Properties and Inheritance

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python read-only properties"
- "Python property inheritance"
- "Python 唯讀屬性"

---

## 1. Read-Only Properties

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

## 2. Encapsulation with Inheritance

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

## 3. Overriding Properties in Child Classes

You can override properties in child classes to modify behavior.

**Example:**
```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self._base_salary = base_salary
    
    @property
    def salary(self):
        return self._base_salary
    
    @property
    def annual_bonus(self):
        """Base employees get 10% bonus"""
        return self._base_salary * 0.10

class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size
    
    @property
    def annual_bonus(self):
        """Managers get 20% bonus + team bonus"""
        base_bonus = self._base_salary * 0.20
        team_bonus = self.team_size * 1000
        return base_bonus + team_bonus

class Executive(Manager):
    @property
    def annual_bonus(self):
        """Executives get 30% bonus + team bonus"""
        base_bonus = self._base_salary * 0.30
        team_bonus = self.team_size * 2000
        return base_bonus + team_bonus

# Using the classes
emp = Employee("Alice", 50000)
print(emp.annual_bonus)  # 5000.0 (10%)

mgr = Manager("Bob", 80000, 5)
print(mgr.annual_bonus)  # 21000.0 (20% + 5 * 1000)

exec = Executive("Carol", 150000, 10)
print(exec.annual_bonus) # 65000.0 (30% + 10 * 2000)
```

---

## 4. Property Deleter

You can also define a deleter for properties using `@property_name.deleter`.

**Example:**
```python
class User:
    def __init__(self, username):
        self._username = username
        self._email = None
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value
    
    @email.deleter
    def email(self):
        print(f"Deleting email: {self._email}")
        self._email = None

# Using the deleter
user = User("alice")
user.email = "alice@example.com"
print(user.email)  # alice@example.com

del user.email     # Deleting email: alice@example.com
print(user.email)  # None
```

---

## 5. Complete Real-World Example

```python
class Product:
    def __init__(self, name, cost, markup_percent):
        self._name = name
        self._cost = cost
        self._markup_percent = markup_percent
        self._stock = 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def cost(self):
        return self._cost
    
    @cost.setter
    def cost(self, value):
        if value < 0:
            raise ValueError("Cost cannot be negative")
        self._cost = value
    
    @property
    def price(self):
        """Computed selling price"""
        return self._cost * (1 + self._markup_percent / 100)
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value
    
    @property
    def total_value(self):
        """Read-only: total inventory value"""
        return self.price * self._stock

# Using the Product class
laptop = Product("Gaming Laptop", 800, 25)
print(f"Cost: ${laptop.cost}")      # Cost: $800
print(f"Price: ${laptop.price}")    # Price: $1000.0

laptop.stock = 10
print(f"Stock: {laptop.stock}")           # Stock: 10
print(f"Total Value: ${laptop.total_value}")  # Total Value: $10000.0

laptop.cost = 750  # Update cost
print(f"New Price: ${laptop.price}")      # New Price: $937.5
print(f"New Total Value: ${laptop.total_value}")  # New Total Value: $9375.0
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01-02: You learned classes, inheritance, and polymorphism
- Unit 03a: You learned encapsulation fundamentals
- Unit 03b: You learned `@property` for elegant getters/setters
- Unit 03c: Now you understand read-only properties and inheritance patterns

**Preparation for Next Lesson:**
- Unit 04: Magic Methods (dunder methods)
- Properties actually use magic methods `__get__`, `__set__`, `__delete__` behind the scenes
- Understanding encapsulation helps you appreciate why magic methods exist

**Real-World Application:**
- FastAPI Pydantic models use properties and computed fields
- Database ORMs use read-only properties for relationships
- Properties enable clean APIs while maintaining data integrity
- This is professional-grade Python used in production systems
