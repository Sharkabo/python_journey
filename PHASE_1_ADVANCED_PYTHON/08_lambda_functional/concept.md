# Unit 08: Lambda and Functional Programming

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python lambda tutorial"
- "Python map filter reduce"
- "Python functional programming"

Recommended Channels:
- Corey Schafer (Python)
- Tech With Tim (Python)
- mCoding (Advanced Python)

---

## 1. What is a Lambda Function?

A **lambda function** is a small anonymous function defined with the `lambda` keyword. It can have any number of arguments but only ONE expression.

**Syntax:**
```python
lambda arguments: expression
```

**Why use lambda?**
- Quick, one-line functions
- Used heavily with map, filter, sort
- Common in FastAPI route dependencies
- Cleaner code for simple operations

**Example:**
```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add(5, 3))         # 8
print(add_lambda(5, 3))  # 8
```

---

## 2. Lambda vs Regular Functions

**When to use Lambda:**
- Simple, one-line operations
- Used as argument to higher-order functions
- Throwaway functions (use once)

**When to use Regular Functions:**
- Complex logic
- Multiple statements
- Need documentation
- Reused multiple times

**Examples:**
```python
# Lambda - Good use case
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Lambda - Bad use case (too complex)
# Don't do this:
process = lambda x: x * 2 if x > 0 else x / 2 if x < 0 else 0

# Use regular function instead:
def process(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x / 2
    else:
        return 0
```

---

## 3. map() - Transform Each Element

`map()` applies a function to every item in an iterable.

**Syntax:**
```python
map(function, iterable)
```

**Examples:**
```python
# Convert to uppercase
names = ['alice', 'bob', 'charlie']
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Calculate squares
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Multiple iterables
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
added = list(map(lambda x, y: x + y, nums1, nums2))
print(added)  # [11, 22, 33]
```

---

## 4. filter() - Select Specific Elements

`filter()` returns only items that pass a test (return True).

**Syntax:**
```python
filter(function, iterable)
```

**Examples:**
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter long names
names = ['Alice', 'Bo', 'Charlie', 'Di', 'Eve']
long_names = list(filter(lambda name: len(name) > 3, names))
print(long_names)  # ['Alice', 'Charlie']

# Filter adults
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30}
]
adults = list(filter(lambda person: person['age'] >= 18, people))
print(adults)  # [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
```

---

## 5. sorted() with Lambda - Custom Sorting

Use lambda with `sorted()` or `.sort()` to define custom sort keys.

**Examples:**
```python
# Sort by string length
words = ['apple', 'banana', 'kiwi', 'cherry']
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # ['kiwi', 'apple', 'cherry', 'banana']

# Sort by last letter
sorted_last = sorted(words, key=lambda word: word[-1])
print(sorted_last)  # ['banana', 'apple', 'kiwi', 'cherry']

# Sort list of tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
by_grade = sorted(students, key=lambda student: student[1], reverse=True)
print(by_grade)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Sort list of dictionaries
products = [
    {'name': 'Laptop', 'price': 999},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Keyboard', 'price': 75}
]
by_price = sorted(products, key=lambda p: p['price'])
print(by_price)  # Sorted by price ascending
```

---

## 6. reduce() - Combine Elements

`reduce()` applies a function cumulatively to reduce a sequence to a single value.

**Import required:**
```python
from functools import reduce
```

**Examples:**
```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# Find maximum
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)  # 5

# Multiply all numbers
product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120

# Flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda acc, lst: acc + lst, nested, [])
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

---

## 7. List Comprehensions vs map/filter

List comprehensions are often more Pythonic than map/filter.

**Comparison:**
```python
numbers = [1, 2, 3, 4, 5]

# Using map
squares_map = list(map(lambda x: x ** 2, numbers))

# Using list comprehension (more Pythonic)
squares_comp = [x ** 2 for x in numbers]

# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (more Pythonic)
evens_comp = [x for x in numbers if x % 2 == 0]

# Complex: map + filter
# Old style
result_old = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# New style (more readable)
result_new = [x ** 2 for x in numbers if x % 2 == 0]
```

**When to use what:**
- **List comprehensions**: Most common, more Pythonic
- **map/filter**: When you already have the function defined
- **lambda with sorted**: Very common for custom sorting

---

## 8. Real-World FastAPI-like Examples

**Route sorting:**
```python
routes = [
    {'path': '/users', 'priority': 2},
    {'path': '/admin', 'priority': 1},
    {'path': '/posts', 'priority': 3}
]

# Sort by priority
sorted_routes = sorted(routes, key=lambda r: r['priority'])
```

**Filter active users:**
```python
users = [
    {'name': 'Alice', 'active': True},
    {'name': 'Bob', 'active': False},
    {'name': 'Charlie', 'active': True}
]

active_users = list(filter(lambda u: u['active'], users))
```

**Transform API responses:**
```python
db_users = [
    {'id': 1, 'name': 'Alice', 'password_hash': 'abc123'},
    {'id': 2, 'name': 'Bob', 'password_hash': 'def456'}
]

# Remove sensitive data
api_response = list(map(lambda u: {'id': u['id'], 'name': u['name']}, db_users))
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- You know list comprehensions (Phase 0, Unit 20)
- You've learned about functions (Phase 0, Unit 07)
- Lambda extends both concepts for functional style

**Preparation for Next Lesson:**
- Unit 09 teaches Generators and Iterators
- Generators are even more memory-efficient than map/filter
- Understanding functional programming helps with generators
