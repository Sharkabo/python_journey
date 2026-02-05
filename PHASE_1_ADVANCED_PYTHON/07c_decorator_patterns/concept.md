# Unit 07c: Common Decorator Patterns

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python timing decorator"
- "Python retry decorator"
- "Python decorator patterns"
- "Python 裝飾器模式"

---

## 1. Timing Decorator

Measure how long a function takes to execute. Very useful for performance optimization.

**Implementation:**
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done"

@timing_decorator
def fast_function():
    return sum(range(1000))

# Usage
slow_function()  # slow_function took 2.0021 seconds
fast_function()  # fast_function took 0.0001 seconds
```

---

## 2. Retry Decorator

Automatically retry a function if it fails. Common for network requests or unreliable operations.

**Implementation:**
```python
from functools import wraps
import time

def retry(max_attempts=3, delay=1):
    """Retry decorator with configurable attempts and delay"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        print(f"Failed after {max_attempts} attempts")
                        raise
                    print(f"Attempt {attempts} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_api_call():
    """Simulates an unreliable API that sometimes fails"""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("API is down")
    return {"status": "success"}

# Usage - will retry up to 3 times
result = unreliable_api_call()
```

---

## 3. Logging Decorator  

Log function calls with arguments and return values. Essential for debugging.

**Implementation:**
```python
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        logging.info(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def create_user(name, age, role="user"):
    return {"name": name, "age": age, "role": role}

# Usage
user = create_user("Alice", 25, role="admin")
# INFO:root:Calling create_user('Alice', 25, role='admin')
# INFO:root:create_user returned {'name': 'Alice', 'age': 25, 'role': 'admin'}
```

---

## 4. Cache/Memoization Decorator

Store results of expensive function calls. Python has built-in `@lru_cache` for this.

**Using Built-in Cache:**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    """Compute fibonacci number (expensive without cache)"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call: computed
print(fibonacci(100))  # Fast! Results are cached

# Second call: instant (from cache)
print(fibonacci(100))  # Instant!
```

**Custom Cache Decorator:**
```python
from functools import wraps

def simple_cache(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@simple_cache
def expensive_computation(x, y):
    print(f"Computing {x} + {y}...")
    time.sleep(2)  # Simulate expensive operation
    return x + y

print(expensive_computation(5, 3))  # Computing 5 + 3... \n 8 (takes 2s)
print(expensive_computation(5, 3))  # 8 (instant, from cache)
```

---

## 5. Authentication Decorator (FastAPI Pattern)

Check if user is authorized before running function. Common in web frameworks.

**Simple Example:**
```python
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # In real app, check session/token
        is_authenticated = kwargs.get('is_authenticated', False)
        
        if not is_authenticated:
            raise PermissionError("Authentication required")
        
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_profile(user_id, is_authenticated=False):
    return f"Profile for user {user_id}"

# Fails
try:
    view_profile(123)
except PermissionError as e:
    print(e)  # Authentication required

# Succeeds
print(view_profile(123, is_authenticated=True))
```

---

## 6. Combining Multiple Patterns

You can combine decorators for powerful effects:

```python
@timing_decorator
@log_calls
@retry(max_attempts=3)
def fetch_user_data(user_id):
    """Fetch user data from API"""
    # Simulated API call
    return {"id": user_id, "name": "Alice"}
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 07a: Basic decorator concept
- Unit 07b: Decorators with arguments and @wraps
- Unit 07c: Real-world patterns you'll use constantly

**Preparation for Next Lesson:**
- Unit 08: Lambda and functional programming
- These patterns appear in every Python framework
- FastAPI uses timing, authentication, and validation decorators

**Real-World Application:**
- `@app.route` (Flask) - routing decorator
- `@app.get` (FastAPI) - HTTP method decorator
- `@login_required` (Django) - authentication decorator
- `@pytest.fixture` (Testing) - setup decorator
- `@lru_cache` (stdlib) - performance optimization

**Pro Tips:**
- Start with timing and logging decorators for debugging
- Use `@lru_cache` for expensive computations
- Study framework decorators to understand their internals
- Most decorators follow the patterns you learned here
