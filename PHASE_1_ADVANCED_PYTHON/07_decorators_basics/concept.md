# Unit 07: Decorators Basics

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python decorators tutorial"
- "Python decorators explained"
- "Python functools wraps"
- "Python 裝飾器教學"
- "Python decorator 詳解"

Recommended Channels:
- Corey Schafer (Python)
- ArjanCodes (Advanced Python)
- mCoding (Python internals)
- Tech With Tim (Python)

---

## 1. What are Decorators?

A decorator is a function that takes another function and extends its behavior without explicitly modifying it. Decorators allow you to "wrap" a function with additional functionality.

**Key Concept:**
- Decorators are functions that modify other functions
- They use the `@decorator_name` syntax
- They're essential for FastAPI routing and middleware
- They promote code reuse and separation of concerns

**Why use Decorators?**
- Add functionality to existing functions without changing their code
- Keep code DRY (Don't Repeat Yourself)
- Implement cross-cutting concerns (logging, timing, authentication)
- FastAPI uses decorators for routing, dependency injection, and more

**Simple Example:**
```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()

# Output:
# Before function runs
# Hello!
# After function runs
```

---

## 2. How Decorators Work

Decorators use Python's first-class functions feature—functions can be passed as arguments and returned from other functions.

**Understanding the Mechanics:**
```python
# This decorator syntax:
@my_decorator
def some_function():
    pass

# Is equivalent to:
def some_function():
    pass
some_function = my_decorator(some_function)
```

**Step-by-Step Example:**
```python
def uppercase_decorator(func):
    def wrapper():
        # Call the original function
        result = func()
        # Modify the result
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world"

# What happens:
# 1. greet() is passed to uppercase_decorator
# 2. uppercase_decorator returns the wrapper function
# 3. greet now refers to the wrapper function

print(greet())  # HELLO, WORLD
```

---

## 3. Decorators with Arguments

Most real-world functions have parameters. Your decorator needs to handle them.

**Using *args and **kwargs:**
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Using the decorated functions
result = add(3, 5)
# Output:
# Calling add with (3, 5) and {}
# add returned 8

message = greet("Alice", greeting="Hi")
# Output:
# Calling greet with ('Alice',) and {'greeting': 'Hi'}
# greet returned Hi, Alice!
```

---

## 4. Preserving Function Metadata with functools.wraps

Decorators replace the original function with the wrapper. This loses the original function's metadata (name, docstring, etc.). Use `functools.wraps` to fix this.

**Problem without @wraps:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def important_function():
    """This function does important work"""
    pass

print(important_function.__name__)  # wrapper (wrong!)
print(important_function.__doc__)   # None (lost docstring!)
```

**Solution with @wraps:**
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def important_function():
    """This function does important work"""
    pass

print(important_function.__name__)  # important_function (correct!)
print(important_function.__doc__)   # This function does important work
```

**Best Practice:**
Always use `@wraps(func)` when creating decorators. This is crucial for debugging and documentation.

---

## 5. Common Decorator Patterns

**Timing Decorator:**
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

result = slow_function()
# Output: slow_function took 1.0012 seconds
```

**Logging Decorator:**
```python
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        print(f"[LOG] Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Result: {result}")
        return result
    return wrapper

@log_decorator
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    return 0

result = calculate(5, 3, operation="multiply")
# Output:
# [LOG] Calling calculate
# [LOG] Arguments: (5, 3), {'operation': 'multiply'}
# [LOG] Result: 15
```

**Validation Decorator:**
```python
from functools import wraps

def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("All arguments must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(width, height):
    return width * height

area = calculate_area(5, 10)  # OK: 50
# area = calculate_area(-5, 10)  # ValueError: All arguments must be positive
```

**Retry Decorator:**
```python
from functools import wraps
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success"
```

---

## 6. Decorators with Parameters

Sometimes you want to configure your decorator. This requires an extra layer of function nesting.

**Parametrized Decorator:**
```python
from functools import wraps

def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")
    return name

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

**Structure Breakdown:**
```python
# 1. repeat(times) is called first, returns decorator
# 2. decorator(func) receives the function, returns wrapper
# 3. wrapper executes the actual logic

def repeat(times):           # Outer: receives parameters
    def decorator(func):     # Middle: receives function
        @wraps(func)
        def wrapper(*args, **kwargs):  # Inner: executes logic
            # Implementation here
            pass
        return wrapper
    return decorator
```

---

## 7. Multiple Decorators

You can stack multiple decorators on a single function. They're applied bottom-to-top.

**Example:**
```python
from functools import wraps

def bold_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def italic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

@bold_decorator
@italic_decorator
def greet(name):
    return f"Hello, {name}"

# Applied from bottom to top:
# 1. italic_decorator wraps greet
# 2. bold_decorator wraps the result
print(greet("Alice"))  # <b><i>Hello, Alice</i></b>
```

---

## 8. Why Decorators Matter for FastAPI

FastAPI heavily relies on decorators for routing and dependency injection.

**FastAPI Example (Preview):**
```python
from fastapi import FastAPI

app = FastAPI()

# The @app.get decorator does several things:
# 1. Registers this function as a handler for GET /
# 2. Uses type hints to validate inputs
# 3. Generates OpenAPI documentation
# 4. Handles serialization of the response
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}

# Multiple decorators in FastAPI:
from fastapi import Depends

@app.get("/users/me")
@require_authentication  # Custom decorator
def get_current_user():
    return {"user": "current_user"}
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 05: Type hints make decorators more powerful (help IDEs understand decorated functions)
- Unit 06: *args and **kwargs (next unit) are essential for writing flexible decorators
- Understanding functions as first-class objects is key

**Preparation for Next Lesson:**
- Unit 08 will cover Lambda functions and functional programming
- Decorators are a form of functional programming
- You'll see more advanced uses of functions as values

**Real-World Application:**
- FastAPI routes: `@app.get("/path")`
- Authentication: `@require_login`
- Caching: `@cache_result`
- Rate limiting: `@rate_limit(calls=10, period=60)`
- Logging and monitoring in production apps
- This knowledge is absolutely essential for backend development
