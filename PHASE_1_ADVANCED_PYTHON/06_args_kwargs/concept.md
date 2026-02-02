# Unit 05: Args and Kwargs (*args, **kwargs)

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python args kwargs tutorial"
- "Python *args **kwargs explained"
- "Python function arguments"

Recommended Channels:
- Corey Schafer (Python)
- Tech With Tim (Python)
- Real Python

---

## 1. What are *args and **kwargs?

`*args` and `**kwargs` allow functions to accept a **variable number of arguments**. This is EVERYWHERE in FastAPI decorators and makes your functions incredibly flexible.

**Quick Summary:**
- `*args`: Accept any number of **positional** arguments (as a tuple)
- `**kwargs`: Accept any number of **keyword** arguments (as a dictionary)

**Why are they essential for FastAPI?**
- FastAPI decorators use them heavily
- Allows flexible function signatures
- Critical for understanding how FastAPI works under the hood

---

## 2. Understanding *args (Positional Arguments)

`*args` collects extra positional arguments into a tuple.

**Example:**
```python
def add_numbers(*args):
    print(f"Received args: {args}")
    print(f"Type: {type(args)}")
    return sum(args)

# Can pass any number of arguments
result1 = add_numbers(1, 2, 3)        # args = (1, 2, 3)
result2 = add_numbers(5, 10, 15, 20)  # args = (5, 10, 15, 20)
result3 = add_numbers(100)            # args = (100,)

print(result1)  # 6
print(result2)  # 50
print(result3)  # 100
```

**Iterating through *args:**
```python
def print_all(*args):
    for index, value in enumerate(args):
        print(f"Argument {index}: {value}")

print_all("apple", "banana", "cherry")
# Argument 0: apple
# Argument 1: banana
# Argument 2: cherry
```

---

## 3. Understanding **kwargs (Keyword Arguments)

`**kwargs` collects extra keyword arguments into a dictionary.

**Example:**
```python
def create_profile(**kwargs):
    print(f"Received kwargs: {kwargs}")
    print(f"Type: {type(kwargs)}")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Can pass any keyword arguments
create_profile(name="Alice", age=25, city="New York")
# kwargs = {'name': 'Alice', 'age': 25, 'city': 'New York'}

create_profile(username="bob123", email="bob@example.com")
# kwargs = {'username': 'bob123', 'email': 'bob@example.com'}
```

**Accessing specific kwargs:**
```python
def greet(**kwargs):
    name = kwargs.get('name', 'Guest')  # Default to 'Guest'
    age = kwargs.get('age')
    
    if age:
        print(f"Hello {name}, you are {age} years old")
    else:
        print(f"Hello {name}")

greet(name="Alice", age=25)  # Hello Alice, you are 25 years old
greet(name="Bob")            # Hello Bob
greet()                      # Hello Guest
```

---

## 4. Combining Regular Parameters, *args, and **kwargs

You can mix all three! Order matters:
1. Regular positional parameters
2. `*args`
3. Keyword-only parameters (optional)
4. `**kwargs`

**Example:**
```python
def complex_function(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function("must have", 1, 2, 3, default="custom", extra="info", debug=True)
# Required: must have
# Args: (1, 2, 3)
# Default: custom
# Kwargs: {'extra': 'info', 'debug': True}
```

**FastAPI-like example:**
```python
def api_endpoint(path, *middlewares, **options):
    print(f"Path: {path}")
    print(f"Middlewares: {middlewares}")
    print(f"Options: {options}")

api_endpoint("/users", "auth", "logging", method="GET", cache=True)
# Path: /users
# Middlewares: ('auth', 'logging')
# Options: {'method': 'GET', 'cache': True}
```

---

## 5. Unpacking with * and **

You can also use `*` and `**` to **unpack** iterables and dictionaries.

**Unpacking lists with *:**
```python
def calculate(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = calculate(*numbers)  # Same as calculate(1, 2, 3)
print(result)  # 6
```

**Unpacking dictionaries with **:**
```python
def create_user(name, email, age):
    return f"User: {name}, Email: {email}, Age: {age}"

user_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
}

result = create_user(**user_data)  # Unpacks dictionary to keyword args
print(result)  # User: Alice, Email: alice@example.com, Age: 25
```

**Combining lists:**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(combined)  # [1, 2, 3, 4, 5, 6]
```

**Combining dictionaries:**
```python
user = {"name": "Alice", "age": 25}
location = {"city": "NYC", "country": "USA"}
full_profile = {**user, **location}
print(full_profile)  # {'name': 'Alice', 'age': 25, 'city': 'NYC', 'country': 'USA'}
```

---

## 6. Real-World Use Cases

**Decorator pattern (FastAPI uses this):**
```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(5, 10)
# Calling add with args=(5, 10), kwargs={}
# Result: 15
```

**Flexible configuration:**
```python
def configure_app(name, *features, **settings):
    config = {
        "app_name": name,
        "features": list(features),
        "settings": settings
    }
    return config

app_config = configure_app(
    "MyApp",
    "authentication",
    "logging",
    "caching",
    debug=True,
    max_connections=100,
    timeout=30
)
print(app_config)
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- You know about functions (Unit 07 in Phase 0)
- You've seen magic methods that use flexible parameters (Unit 04)
- `*args` and `**kwargs` make functions super flexible

**Preparation for Next Lesson:**
- Unit 06 teaches Decorators
- Decorators HEAVILY use `*args` and `**kwargs`
- Understanding this unit is crucial for decorators and FastAPI
