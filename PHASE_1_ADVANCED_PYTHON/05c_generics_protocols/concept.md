# Unit 05c: Type Hints for Classes and FastAPI

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python class type hints"
- "Python self type annotation"
- "FastAPI type hints"
- "Pydantic BaseModel"

---

## 1. Type Hints for Classes

You can add type hints to class attributes and methods just like functions.

**Basic Class with Type Hints:**
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
```

**Using the Class:**
```python
# IDE will provide autocomplete for attributes and methods
user: User = User("Alice", 25, "alice@email.com")
info: str = user.get_info()
is_adult: bool = user.is_adult()
```

---

## 2. Type Hints with Inheritance

Type hints work with inheritance too. This helps ensure subclasses follow the parent class's contract.

**Example:**
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

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"
```

**Function Working with Any Animal:**
```python
def make_animal_speak(animal: Animal) -> str:
    return animal.speak()

# Works with any subclass
dog: Dog = Dog("Buddy")
cat: Cat = Cat("Whiskers")

print(make_animal_speak(dog))  # "Woof!"
print(make_animal_speak(cat))  # "Meow!"
```

---

## 3. Real-World Example

Here's a practical shopping cart system using type hints:

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

## 4. Why Type Hints Matter for FastAPI

Type hints aren't just good practice—they're **essential** for FastAPI. FastAPI uses type hints to automatically validate data and generate documentation.

**FastAPI Example (Preview):**
```python
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

# When someone sends wrong data type:
# {"name": "Alice", "age": "twenty", "email": "alice@email.com"}
# FastAPI automatically returns an error!
```

**What FastAPI Does Automatically:**
- Validates `age` is an integer
- Validates `email` is a string
- Generates API documentation showing required fields
- Provides helpful error messages when data is wrong
- All of this just from type hints!

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01: You created classes without type hints
- Units 05a-05b: You learned type hints for simple and complex types
- Unit 05c: Now you're applying type hints to classes

**Preparation for Next Lesson:**
- Unit 06: `*args` and `**kwargs` with type hints
- Understanding class type hints makes FastAPI's Pydantic models clear
- Type hints become second nature from here on

**Real-World Application:**
- FastAPI requires type hints for automatic validation
- Modern Python projects use them for maintainability
- Tools like mypy catch bugs before code runs
- Essential for professional backend development
