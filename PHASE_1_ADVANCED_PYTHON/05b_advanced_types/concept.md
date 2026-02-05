# Unit 05b: Advanced Types (Optional, Union, Collections)

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python Optional type hint"
- "Python Union types"
- "Python dict type hints"
- "Python typing module"

---

## 1. Dictionary Type Hints

Dictionaries require type hints for both keys and values. This helps catch bugs when you accidentally use wrong types.

**Syntax:**
```python
# Dictionary with string keys and int values
ages: dict[str, int] = {"Alice": 25, "Bob": 30}

# Dictionary with int keys and string values
id_to_name: dict[int, str] = {1: "Alice", 2: "Bob"}
```

**Example:**
```python
def count_items(items: list[str]) -> dict[str, int]:
    """Count how many times each item appears"""
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

# Usage
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
result = count_items(fruits)
print(result)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

**Nested Dictionaries:**
```python
# Dictionary containing dictionaries
user_data: dict[str, dict[str, int]] = {
    "Alice": {"age": 25, "score": 100},
    "Bob": {"age": 30, "score": 95}
}
```

---

## 2. Set and Tuple Type Hints

**Set Type Hints:**
```python
# Set of strings
unique_names: set[str] = {"Alice", "Bob", "Charlie"}

# Function that returns a set
def get_unique_values(items: list[int]) -> set[int]:
    return set(items)
```

**Tuple Type Hints:**
```python
# Tuple with specific types for each position
user: tuple[str, int, float] = ("Alice", 25, 5.8)

# Tuple with variable length (all same type)
coordinates: tuple[float, ...] = (1.5, 2.3, 4.1, 6.7)

# Function returning tuple
def get_user_info() -> tuple[str, int]:
    return ("Alice", 25)
```

---

## 3. Optional Types

`Optional` means a value can be either the specified type OR `None`. This is very common in Python.

**Syntax:**
```python
from typing import Optional

# Variable can be str or None
name: Optional[str] = "Alice"
name = None  # This is valid

# Or use | operator (Python 3.10+)
name: str | None = "Alice"
```

**Example:**
```python
def find_user(user_id: int) -> Optional[str]:
    """Find user by ID, return None if not found"""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)  # Returns None if not found

# Using the result
result = find_user(1)
if result is not None:
    print(f"Found: {result}")
else:
    print("User not found")
```

**Why Optional Matters:**
```python
# Without Optional, your IDE won't warn you about None
def get_name() -> str:
    return None  # IDE will complain!

# With Optional, it's clear None is allowed
def get_name() -> Optional[str]:
    return None  # This is fine
```

---

## 4. Union Types

`Union` means a value can be one of several types. Use when a function can accept or return multiple types.

**Syntax:**
```python
from typing import Union

# Variable can be int or str
user_id: Union[int, str] = 123
user_id = "ABC123"  # Both are valid

# Or use | operator (Python 3.10+)
user_id: int | str = 123
```

**Example:**
```python
def process_id(id_value: int | str) -> str:
    """Convert any ID to string format"""
    return str(id_value)

# Both work
print(process_id(123))      # "123"
print(process_id("ABC"))    # "ABC"
```

**Multiple Types Including None:**
```python
def get_value(key: str) -> int | str | None:
    """Return int, str, or None depending on key"""
    data = {"age": 25, "name": "Alice"}
    return data.get(key)

# Returns int
print(get_value("age"))    # 25
# Returns str
print(get_value("name"))   # "Alice"
# Returns None
print(get_value("city"))   # None
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 05a: You learned basic type hints for simple types
- Unit 05b: Now you can handle complex collections and optional values
- This prepares you for FastAPI which uses these extensively

**Preparation for Next Lesson:**
- Unit 05c: Class type hints and how FastAPI uses them
- Understanding Optional and Union makes FastAPI's automatic validation clearer
- You'll see how these types enable powerful features in web frameworks
