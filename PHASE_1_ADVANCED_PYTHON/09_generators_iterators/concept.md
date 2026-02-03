# Unit 09: Generators and Iterators

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python generators tutorial"
- "Python yield keyword"
- "Python iterators explained"
- "Python generator expressions"
- "Python 生成器教學"

Recommended Channels:
- Corey Schafer (Python)
- mCoding (Python internals)
- ArjanCodes (Advanced Python)
- Real Python (Written tutorials)

---

## 1. What are Iterators?

An iterator is an object that implements the iterator protocol: methods `__iter__()` and `__next__()`. Iterators allow you to tr

averse through a sequence of values one at a time.

**Key Concepts:**
- Iterable: Any object you can loop over (lists, strings, dictionaries)
- Iterator: Object that produces values one at a time when asked
- `__iter__()`: Returns the iterator object itself
- `__next__()`: Returns the next value or raises StopIteration when done

**Built-in Iterables:**
```python
# Lists, strings, tuples, sets are all iterable
my_list = [1, 2, 3]

# When you use a for loop, Python calls iter() on the iterable
for item in my_list:
    print(item)

# This is what happens behind the scenes:
iterator = iter(my_list)  # Calls my_list.__iter__()
print(next(iterator))     # 1 (calls iterator.__next__())
print(next(iterator))     # 2
print(next(iterator))     # 3
# print(next(iterator))   # StopIteration exception
```

**Creating a Custom Iterator:**
```python
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self  # Return the iterator object (itself)
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Using the iterator
countdown = CountDown(5)
for num in countdown:
    print(num)  # 5, 4, 3, 2, 1

# Or manually
countdown2 = CountDown(3)
print(next(countdown2))  # 3
print(next(countdown2))  # 2
print(next(countdown2))  # 1
# print(next(countdown2))  # StopIteration
```

---

## 2. What are Generators?

Generators are a simpler way to create iterators. They use the `yield` keyword instead of `return` and automatically implement the iterator protocol.

**Why Generators?**
- Easier to write than custom iterator classes
- Memory efficient (generate values on-the-fly)
- Can represent infinite sequences
- Pause and resume execution

**Generator Function Syntax:**
```python
def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration

# Or use in a for loop
for value in simple_generator():
    print(value)  # 1, 2, 3
```

**How Generators Work:**
```python
def countdown(start):
    current = start
    while current > 0:
        yield current  # Pause here and return current
        current -= 1   # Resume here on next() call

# Each yield pauses the function
gen = countdown(3)
print(next(gen))  # 3 (paused at first yield)
print(next(gen))  # 2 (resumed, paused at second yield)
print(next(gen))  # 1 (resumed, paused at third yield)
# print(next(gen))  # StopIteration (function finished)
```

---

## 3. Generators vs Regular Functions

**Regular Function:**
```python
def get_numbers():
    result = []
    for i in range(1000000):
        result.append(i * 2)
    return result

# Creates entire list in memory (uses lots of memory)
numbers = get_numbers()
```

**Generator Function:**
```python
def get_numbers_generator():
    for i in range(1000000):
        yield i * 2

# Creates values one at a time (memory efficient)
numbers_gen = get_numbers_generator()
```

**Memory Comparison:**
```python
import sys

# List: All values in memory
number_list = [x for x in range(100000)]
print(sys.getsizeof(number_list))  # Large memory usage

# Generator: Values created on demand
number_gen = (x for x in range(100000))
print(sys.getsizeof(number_gen))   # Tiny memory usage
```

---

## 4. Generator Expressions

Similar to list comprehensions, but create generators instead of lists.

**Syntax Comparison:**
```python
# List comprehension (creates full list in memory)
squares_list = [x**2 for x in range(10)]
print(squares_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expression (creates values on demand)
squares_gen = (x**2 for x in range(10))
print(squares_gen)   # <generator object>
print(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Practical Example:**
```python
# Reading large file - BAD (loads entire file)
with open('large_file.txt') as f:
    lines = [line.strip() for line in f]  # All in memory
    for line in lines:
        process(line)

# Reading large file - GOOD (one line at a time)
with open('large_file.txt') as f:
    lines = (line.strip() for line in f)  # Generator
    for line in lines:
        process(line)  # Process one line at a time
```

---

## 5. Practical Generator Examples

**Fibonacci Generator:**
```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Generate Fibonacci numbers up to 100
for num in fibonacci(100):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
```

**File Reader Generator:**
```python
def read_large_file(file_path):
    """Read file line by line without loading entire file"""
    with open(file_path) as file:
        for line in file:
            yield line.strip()

# Process huge file one line at a time
for line in read_large_file('huge_log.txt'):
    if 'ERROR' in line:
        print(line)
```

**Batch Generator:**
```python
def batch_data(data, batch_size):
    """Split data into batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Process data in batches
data = list(range(100))
for batch in batch_data(data, 10):
    print(f"Processing batch of {len(batch)} items")
    # Process batch...
```

**Infinite Sequence Generator:**
```python
def infinite_counter(start=0):
    """Generate infinite sequence of numbers"""
    count = start
    while True:
        yield count
        count += 1

# Use with caution! This never ends
counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
# Can continue forever...

# Combine with other functions
from itertools import islice
first_10 = list(islice(infinite_counter(), 10))
print(first_10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 6. Generator Methods

Generators have special methods for advanced control.

**send() method:**
```python
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")     # Received: Hello
gen.send("World")     # Received: World
```

**close() method:**
```python
def counter():
    count = 0
    try:
        while True:
            yield count
            count += 1
    finally:
        print("Generator closed")

gen = counter()
print(next(gen))  # 0
print(next(gen))  # 1
gen.close()       # Generator closed
```

---

## 7. Combining Generators

Generators can be chained together for data pipelines.

**Data Pipeline Example:**
```python
def read_numbers(numbers):
    """Generate numbers from list"""
    for num in numbers:
        yield num

def filter_even(numbers):
    """Filter even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square(numbers):
    """Square the numbers"""
    for num in numbers:
        yield num ** 2

# Chain generators together
data = range(10)
pipeline = square(filter_even(read_numbers(data)))

result = list(pipeline)
print(result)  # [0, 4, 16, 36, 64]

# More readable with separate variables
numbers = read_numbers(range(10))
even_numbers = filter_even(numbers)
squared = square(even_numbers)
print(list(squared))  # [0, 4, 16, 36, 64]
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 08: Lambda and functional programming work well with generators
- Generators are memory-efficient alternatives to list comprehensions
- Understanding functions and iteration from Phase 0 is essential

**Preparation for Next Lesson:**
- Unit 10: Context Managers also use iteration concepts
- Generators and context managers both manage resources efficiently
- File handling benefits from both concepts

**Real-World Application:**
- Processing large datasets without loading everything in memory
- Streaming data from APIs or databases
- FastAPI background tasks can use generators
- Data pipelines in production systems
- Reading log files, CSV files, database queries
- This is essential for building efficient, scalable applications
