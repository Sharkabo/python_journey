# Unit 03a: Encapsulation Basics

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python encapsulation tutorial"
- "Python public private protected"
- "Python 封裝概念"

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

## 2. Understanding Name Mangling

When you use double underscores `__`, Python applies **name mangling** to make the attribute harder (but not impossible) to access from outside.

**How Name Mangling Works:**
```python
class MyClass:
    def __init__(self):
        self.__private_var = 42

obj = MyClass()
# print(obj.__private_var)  # AttributeError

# But it's still accessible via name mangling:
print(obj._MyClass__private_var)  # 42 (not recommended!)
```

**When to Use Each:**
- **Public (`self.name`)**: For data that should be freely accessed
- **Protected (`self._name`)**: For internal use, but subclasses might need it
- **Private (`self.__name`)**: For truly internal implementation details

---

## 3. Practical Example: Product Class

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name                # Public: everyone can see product name
        self._supplier_code = "SUP123" # Protected: internal tracking
        self.__cost = price * 0.6      # Private: internal business logic
        self.__stock = stock           # Private: controlled access
    
    def get_price(self):
        """Public method to get selling price"""
        return self.__cost / 0.6
    
    def get_stock(self):
        """Public method to check stock"""
        return self.__stock
    
    def purchase(self, quantity):
        """Public method with validation"""
        if quantity <= 0:
            return False, "Quantity must be positive"
        if quantity > self.__stock:
            return False, "Insufficient stock"
        
        self.__stock -= quantity
        return True, f"Purchased {quantity} units"
    
    def restock(self, quantity):
        """Public method to add stock"""
        if quantity > 0:
            self.__stock += quantity
            return True
        return False

# Using the Product class
laptop = Product("Gaming Laptop", 1000, 50)
print(laptop.name)                # Gaming Laptop (public, OK)
print(laptop.get_price())         # 1000.0 (controlled access)
print(laptop.get_stock())         # 50

success, message = laptop.purchase(5)
print(message)                    # Purchased 5 units
print(laptop.get_stock())         # 45

# laptop.__stock = 1000           # Won't work (AttributeError)
# Can't cheat the system by directly modifying private attributes!
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01: You learned to create classes with attributes
- Unit 02: You learned inheritance, where child classes access parent attributes
- Unit 03a: Now you're learning to control access to those attributes

**Preparation for Next Lesson:**
- Unit 03b: You'll learn the `@property` decorator for elegant encapsulation
- Unit 03c: You'll learn about read-only properties and advanced patterns
- Properties build on the encapsulation concepts you learned here

**Real-World Application:**
- Encapsulation prevents bugs by controlling data access
- Banking systems use private attributes for account balances
- E-commerce platforms protect pricing and inventory data
- This is fundamental to writing secure, maintainable code
