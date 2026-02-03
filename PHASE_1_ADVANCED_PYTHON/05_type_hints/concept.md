# Unit 05: Type Hints

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python type hints tutorial"
- "Python type annotations"
- "Python mypy tutorial"
- "Python typing module"
- "Python 類型提示"

Recommended Channels:
- Corey Schafer (Python)
- Tech With Tim (Python)
- ArjanCodes (Advanced Python)
- mCoding (Python internals)

---

## 1. What are Type Hints?

Type hints (also called type annotations) allow you to specify what types of values variables, function parameters, and return values should have. They make code more readable and help catch bugs before runtime.

**Key Points:**
- Type hints are OPTIONAL in Python (Python remains dynamically typed)
- They don't affect runtime performance
- Tools like mypy, pyright, and IDEs use them for static type checking
- FastAPI relies heavily on type hints for automatic validation and documentation

**Why use Type Hints?**
- Better IDE autocomplete and IntelliSense
- Catch type errors before running code
- Self-documenting code (easier to understand)
- Required for FastAPI's automatic features
- Helps team collaboration on larger projects

**Basic Syntax:**
```python
# Variable annotation
name: str = "Alice"
age: int = 25
price: float = 19.99
is_active: bool = True

# Function annotation
def greet(name: str) -> str:
    return f"Hello, {name}"

# Type hints don't enforce types at runtime
age: int = "25"  # No error! Python doesn't enforce this
```

---

## 2. Basic Type Annotations

**Built-in Types:**
```python
# Common types
name: str = "Alice"
age: int = 30
height: float = 5.8
is_student: bool = True

# Function with type hints
def add_numbers(a: int, b: int) -> int:
    return a + b

def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

# Multiple return values (tuple)
def get_user_info() -> tuple[str, int]:
    return ("Alice", 25)

# No return value
def print_message(msg: str) -> None:
    print(msg)

# Example usage
result: int = add_numbers(5, 3)
greeting: str = get_greeting("Bob")
user_name, user_age = get_user_info()
```

---

## 3. Collection Type Hints

For collections like lists, dictionaries, sets, and tuples, you specify both the collection type and the type of elements inside.

**List Type Hints:**
```python
# List of integers
numbers: list[int] = [1, 2, 3, 4, 5]

# List of strings
names: list[str] = ["Alice", "Bob", "Charlie"]

# Function that takes and returns a list
def get_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

# Empty list with type hint
scores: list[float] = []
```

**Dictionary Type Hints:**
```python
# Dictionary with string keys and int values
ages: dict[str, int] = {"Alice": 25, "Bob": 30}

# Dictionary with int keys and string values
id_to_name: dict[int, str] = {1: "Alice", 2: "Bob"}

# Function with dict parameter
def count_items(items: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

# Nested dictionary
user_data: dict[str, dict[str, int]] = {
    "Alice": {"age": 25, "score": 100},
    "Bob": {"age": 30, "score": 95}
}
```

**Set and Tuple Type Hints:**
```python
# Set of strings
unique_names: set[str] = {"Alice", "Bob", "Charlie"}

# Tuple with specific types for each position
user: tuple[str, int, float] = ("Alice", 25, 5.8)

# Tuple with variable length (all same type)
coordinates: tuple[float, ...] = (1.5, 2.3, 4.1, 6.7)
```

---

## 4. Optional and Union Types

Sometimes a variable or parameter can be one of several types, or it can be None. Use `Optional` and `Union` from the typing module (or the `|` operator in Python 3.10+).

**Optional Type:**
```python
from typing import Optional

# Variable can be str or None
name: Optional[str] = "Alice"
name = None  # This is valid

# Or use the | operator (Python 3.10+)
name: str | None = "Alice"

# Function that might return None
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns None if not found

# Using the result
result = find_user(1)
if result is not None:
    print(f"Found: {result}")
```

**Union Type:**
```python
from typing import Union

# Variable can be int or str
user_id: Union[int, str] = 123
user_id = "ABC123"  # Both are valid

# Or use | operator (Python 3.10+)
user_id: int | str = 123

# Function that accepts multiple types
def process_id(id_value: int | str) -> str:
    return str(id_value)

# Multiple types including None
def get_value() -> int | str | None:
    return None
```

---

## 5. Type Hints for Classes

You can add type hints to class attributes and methods.

**Class Attributes and Methods:**
```python
class User:
    # Class variable type hint
    total_users: int = 0
    
    def __init__(self, name: str, age: int, email: str):
        self.name: str = name
        self.age: int = age
        self.email: str = email
        User.total_users += 1
    
    def get_info(self) -> str:
        return f"{self.name}, {self.age} years old"
    
    def is_adult(self) -> bool:
        return self.age >= 18
    
    @staticmethod
    def create_guest() -> 'User':  # Forward reference
        return User("Guest", 0, "guest@example.com")

# Using the class
user: User = User("Alice", 25, "alice@email.com")
info: str = user.get_info()
is_adult: bool = user.is_adult()
```

**Type Hints with Inheritance:**
```python
class Animal:
    def __init__(self, name: str):
        self.name: str = name
    
    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):
    def speak(self) -> str:  # Override with same return type
        return "Woof!"
    
    def fetch(self, item: str) -> None:
        print(f"{self.name} fetches {item}")

# Function that works with any Animal
def make_animal_speak(animal: Animal) -> str:
    return animal.speak()

dog: Dog = Dog("Buddy")
sound: str = make_animal_speak(dog)  # Works with Dog (subclass)
```

---

## 6. Type Hints in Practice

**Real-World Example:**
```python
from typing import Optional

class Product:
    def __init__(
        self, 
        name: str, 
        price: float, 
        stock: int,
        category: str
    ):
        self.name: str = name
        self.price: float = price
        self.stock: int = stock
        self.category: str = category
    
    def apply_discount(self, discount: float) -> float:
        """Apply discount and return new price"""
        if discount < 0 or discount > 1:
            raise ValueError("Discount must be between 0 and 1")
        return self.price * (1 - discount)
    
    def is_in_stock(self) -> bool:
        return self.stock > 0

class ShoppingCart:
    def __init__(self):
        self.items: list[Product] = []
    
    def add_item(self, product: Product) -> None:
        self.items.append(product)
    
    def get_total(self) -> float:
        total: float = 0
        for item in self.items:
            total += item.price
        return total
    
    def find_by_category(self, category: str) -> list[Product]:
        return [item for item in self.items if item.category == category]

# Using type hints helps IDE autocomplete
cart: ShoppingCart = ShoppingCart()
product: Product = Product("Laptop", 999.99, 5, "Electronics")
cart.add_item(product)
total: float = cart.get_total()
electronics: list[Product] = cart.find_by_category("Electronics")
```

---

## 7. Why Type Hints Matter for FastAPI

Type hints are not just good practice—they're essential for FastAPI:

**FastAPI Example (Preview):**
```python
# This is how FastAPI uses type hints
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

# FastAPI uses type hints to:
# 1. Validate incoming data
# 2. Generate automatic documentation
# 3. Provide IDE autocomplete
@app.post("/users/")
def create_user(user: User) -> dict[str, str]:
    return {"message": f"Created user {user.name}"}

# The type hints tell FastAPI:
# - user must be JSON matching User model
# - Response will be a dictionary with string keys and values
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01: You created classes with attributes and methods
- Units 02-03: You worked with inheritance and properties
- Unit 05: Now you're adding type hints to make all of this clearer
- Remember adding type hints to Unit 01's answer.py? This is why!

**Preparation for Next Lesson:**
- Unit 06 will teach `*args` and `**kwargs`
- Type hints become more complex with flexible parameters
- You'll learn: `def func(*args: int, **kwargs: str) -> None:`
- Understanding basic type hints now makes that much easier

**Real-World Application:**
- FastAPI requires type hints for automatic validation and docs
- Modern Python projects use type hints for maintainability
- Tools like mypy catch bugs before code runs
- Type hints make team collaboration much smoother
- This is not optional knowledge for backend development
