# Task: Build Advanced Decorators with Arguments

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Repeat Decorator
Create a decorator that:
- Accepts a parameter `times` for how many times to repeat
- Executes the decorated function `times` times
- Uses functools.wraps to preserve metadata

## Goal 2: Create a Validation Decorator
Create a decorator that:
- Accepts validation rules as parameters
- Validates function arguments before execution
- Raises ValueError for invalid inputs

## Goal 3: Test Your Decorators
Demonstrate:
- Decorator factory pattern
- Proper use of functools.wraps
- Handling decorator parameters

---

**Expected Output:**
```text
Hello, World!
Hello, World!
Hello, World!
(function repeated 3 times)

Error: Value must be positive
```
