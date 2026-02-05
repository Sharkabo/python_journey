# Unit 07a: Decorator Basics

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python decorators tutorial"
- "Python decorator basics"
- "Python @ symbol"
- "Python 裝飾器基礎"

---

## 1. What are Decorators?

A decorator is a function that **modifies or enhances** another function without changing its code. It's like wrapping a gift—the gift stays the same, but now it has decorative paper around it.

**Key Points:**
- Decorators are functions that take a function as input
- They return a new function that usually calls the original
- They use the `@` symbol as syntactic sugar
- Very common in Python frameworks (Flask, FastAPI, Django)

**Why Use Decorators?**
- Add functionality without modifying original code
- Reuse code across multiple functions
- Keep code DRY (Don't Repeat Yourself)
- Common uses: logging, timing, authentication, validation

---

## 2. Simple Decorator Example

**Basic Syntax:**
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# Without @ symbol (manual wrapping)
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)

# With @ symbol (decorator syntax)
@my_decorator
def say_goodbye():
    print("Goodbye!")

# Usage
say_hello()
# Output:
# Before function call
# Hello!
# After function call

say_goodbye()
# Output:
# Before function call
# Goodbye!
# After function call
```

**How It Works:**
1. `@my_decorator` is equivalent to `say_goodbye = my_decorator(say_goodbye)`
2. The decorator receives the function
3. Returns a new `wrapper` function
4. When you call `say_goodbye()`, you're actually calling `wrapper()` 5. The wrapper calls the original function inside

---

## 3. Practical Example: Logging Decorator

**Real-World Use Case:**
```python
def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        result = func()
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@log_decorator
def fetch_data():
    print("Fetching data from database...")
    return {"users": 100}

@log_decorator
def process_payment():
    print("Processing payment...")
    return True

# Usage
data = fetch_data()
# Output:
# Calling function: fetch_data
# Fetching data from database...
# Function fetch_data completed

payment = process_payment()
# Output:
# Calling function: process_payment
# Processing payment...
# Function process_payment completed
```

---

## 4. Multiple Decorators

You can stack multiple decorators on one function:

```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        result = func()
        return result + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet():
    return "hello world"

print(greet())  # "HELLO WORLD!!!"

# Order matters! It's like:
# greet = exclamation_decorator(uppercase_decorator(greet))
# First uppercase, then add exclamation
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 06: You learned functions can take functions as parameters
- Unit 07a: Now you're using that to modify functions with decorators
- This is a fundamental Python pattern you'll see everywhere

**Preparation for Next Lesson:**
- Unit 07b: Decorators with arguments (*args, **kwargs)
- Unit 07c: Common decorator patterns (timing, caching, validation)
- FastAPI uses decorators heavily (@app.get, @app.post)

**Real-World Application:**
- Flask: `@app.route("/home")`
- FastAPI: `@app.get("/users")`
- Django: `@login_required`
- Testing: `@pytest.fixture`
