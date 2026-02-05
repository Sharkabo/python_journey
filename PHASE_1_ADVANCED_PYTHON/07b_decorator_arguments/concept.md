# Unit 07b: Decorators with Arguments

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python decorator with arguments"
- "Python functools wraps"
- "Python *args **kwargs decorator"
- "Python 裝飾器參數"

---

## 1. Problem: Decorators and Function Arguments

In Unit 07a, our decorators only worked with functions that take no arguments. Real functions need parameters!

**This Breaks:**
```python
def log_decorator(func):
    def wrapper():  # No parameters!
        print(f"Calling {func.__name__}")
        result = func()
        return result
    return wrapper

@log_decorator
def greet(name):  # Takes a parameter
    return f"Hello, {name}"

# This will error!
greet("Alice")  # TypeError: wrapper() takes 0 positional arguments
```

---

## 2. Solution: Use *args and **kwargs

Make the wrapper accept any number of arguments:

**Syntax:**
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):  # Accept any arguments
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)  # Pass them through
        return result
    return wrapper

@log_decorator
def greet(name):
    return f"Hello, {name}"

@log_decorator
def add(a, b):
    return a + b

# Now both work!
print(greet("Alice"))  # Calling greet \n Hello, Alice
print(add(5, 3))       # Calling add \n 8
```

---

## 3. The functools.wraps Problem

Decorators have a problem: they hide the original function's metadata.

**The Problem:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello to someone"""
    return f"Hello, {name}"

print(greet.__name__)  # "wrapper" (should be "greet")
print(greet.__doc__)   # None (should be "Say hello to someone")
```

**The Solution: @functools.wraps:**
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello to someone"""
    return f"Hello, {name}"

print(greet.__name__)  # "greet" ✓
print(greet.__doc__)   # "Say hello to someone" ✓
```

**Always use `@wraps(func)` in your decorators!**

---

## 4. Complete Decorator Template

This is the standard pattern for any decorator:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before function call
        print(f"Before {func.__name__}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # After function call
        print(f"After {func.__name__}")
        
        # Return the result
        return result
    return wrapper
```

---

## 5. Practical Example: Validation Decorator

**Real-World Use Case:**
```python
from functools import wraps

def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check all numeric arguments are positive
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"All arguments must be positive")
        
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(width, height):
    """Calculate rectangle area"""
    return width * height

@validate_positive
def calculate_volume(length, width, height):
    """Calculate box volume"""
    return length * width * height

# Works fine
print(calculate_area(5, 10))  # 50

# Raises ValueError
try:
    print(calculate_area(-5, 10))
except ValueError as e:
    print(e)  # "All arguments must be positive"
```

---

## 6. Type Hints with Decorators

You can add type hints to decorators too:

```python
from functools import wraps
from typing import Any, Callable

def log_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 06: You learned *args and **kwargs for flexible parameters
- Unit 07a: You learned basic decorators
- Unit 07b: Now combining both to create professional decorators

**Preparation for Next Lesson:**
- Unit 07c: Common decorator patterns (timing, retry, caching)
- You now have the foundation to understand any decorator
- FastAPI decorators use this exact pattern

**Key Takeaway:**
- Always use `@wraps(func)` to preserve metadata
- Always use `*args, **kwargs` for flexible decorators
- This pattern works for 99% of decorators you'll write
