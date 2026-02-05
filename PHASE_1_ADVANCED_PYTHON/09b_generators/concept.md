# Unit 09b: Generators

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python generators tutorial"
- "Python yield keyword"
- "Python generator vs iterator"
- "Python 生成器"

---

## 1. What are Generators?

Generators are a simpler way to create iterators. Instead of writing `__iter__` and `__next__`, you just use the `yield` keyword in a function.

**Key Points:**
- Generator functions use `yield` instead of `return`
- Each `yield` pauses the function and saves its state
- Next call resumes from where it paused
- Much simpler than writing iterator classes
- Memory efficient—values generated on-demand

---

## 2. Basic Generator Example

```python
def count_up_to(max_num):
    num = 1
    while num <= max_num:
        yield num  # Pause here and return num
        num += 1   # Resume here on next call

# Usage
for n in count_up_to(5):
    print(n)  # 1, 2, 3, 4, 5

# How it works:
gen = count_up_to(3)
print(next(gen))  # 1 (runs until first yield)
print(next(gen))  # 2 (resumes, runs until next yield)
print(next(gen))  # 3
print(next(gen))  # StopIteration
```

---

## 3. Generator vs Iterator Class

```python
# Using Generator Function - Simple!
def counter(max_num):
    num = 1
    while num <= max_num:
        yield num
        num += 1

# Much simpler than the Counter class from Unit 09a!
```

---

## 4. Practical Examples

**Reading Large Files:**
```python
def read_large_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()

# Only one line in memory at a time
for line in read_large_file('huge_file.txt'):
    print(line)
```

**Fibonacci Sequence:**
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
gen = fibonacci()
for _ in range(10):
    print(next(gen))
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

---

## 5. Generator Expressions

Even shorter syntax:

```python
# Generator expression (lazy)
squares_gen = (x**2 for x in range(10))

# List comprehension (eager)
squares_list = [x**2 for x in range(10)]

# Generators use much less memory!
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 09a: Learned iterator protocol (complex)
- Unit 09b: Generators make it simple with `yield`

**Preparation for Next Lesson:**
- Unit 10c: @contextmanager uses generators
- Generators are everywhere in Python

**Real-World Application:**
- Django ORM queries use generators
- FastAPI streaming responses
- Data processing pipelines
