# Unit 05a: Basic Type Hints

## YouTube Recommendations
- "Python type hints tutorial"
- "Python type annotations basics"
- "Python 類型提示基礎"

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

## 3. Collection Type Hints - Lists

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

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01: You created classes with attributes and methods
- Units 02-03: You worked with inheritance and properties
- Unit 05a: Now you're adding type hints to make all of this clearer

**Preparation for Next Lesson:**
- Unit 05b: Advanced types (Optional, Union, Dict, Set)
- Unit 05c: Generics and Protocols
- Understanding basic type hints now makes those much easier

**Real-World Application:**
- FastAPI requires type hints for automatic validation
- Modern Python projects use type hints for maintainability
- Tools like mypy catch bugs before code runs
