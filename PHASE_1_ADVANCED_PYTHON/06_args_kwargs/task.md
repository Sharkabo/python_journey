# Task: Build Flexible Functions with *args and **kwargs

Open `my_answer.py` in this folder and complete the following objectives:

## Goal 1: Create a sum_all function
Create a function `sum_all(*args)` that:
- Accepts any number of numbers
- Returns the sum of all numbers
- Returns 0 if no arguments are provided

## Goal 2: Create a describe_person function
Create a function `describe_person(**kwargs)` that:
- Accepts any keyword arguments
- Prints each key-value pair
- Must handle at minimum: name, age, city, occupation

## Goal 3: Create a create_user function
Create a function `create_user(username, *roles, **permissions)` that:
- `username` is required
- `*roles` collects role names
- `**permissions` collects permission settings
- Returns a dictionary with all this information

## Goal 4: Create a decorator-style wrapper
Create a function `call_logger(func, *args, **kwargs)` that:
- Calls the provided function with the given args and kwargs
- Prints what function was called and with what arguments
- Returns the result

## Goal 5: Practice unpacking
- Create a list of 5 numbers and unpack it to print each number separately
- Create a dictionary of user info and unpack it to call a function

---

**Expected Output:**
```text
sum_all(1, 2, 3, 4, 5) = 15
sum_all() = 0

Person info:
name: Alice
age: 30
city: New York

create_user result:
{'username': 'alice123', 'roles': ['admin', 'editor'], 'permissions': {'can_delete': True, 'can_edit': True}}

Calling add with (5, 3) and {}
Result: 8
```
