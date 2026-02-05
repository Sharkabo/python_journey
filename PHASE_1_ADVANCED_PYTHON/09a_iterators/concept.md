# Unit 09a: Iterators

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python iterators tutorial"
- "Python __iter__ __next__"
- "Python iterator protocol"
- "Python 迭代器"

---

## 1. What are Iterators?

An iterator is an object that allows you to loop through a collection one item at a time. When you use a `for` loop, Python automatically uses iterators behind the scenes.

**Key Concepts:**
- An iterator is an object with `__iter__()` and `__next__()` methods
- `__iter__()` returns the iterator object itself
- `__next__()` returns the next item, raises `StopIteration` when done
- All iterables (lists, strings, dicts) use iterators internally

**Why Learn Iterators?**
- Understand how `for` loops actually work
- Create custom iteration logic
- More memory efficient than lists for large datasets
- Foundation for generators (Unit 09b)

---

## 2. How For Loops Actually Work

```python
# When you write this:
for item in [1, 2, 3]:
    print(item)

# Python does this internally:
iterator = iter([1, 2, 3])  # Calls __iter__()
while True:
    try:
        item = next(iterator)  # Calls __next__()
        print(item)
    except StopIteration:
        break
```

---

## 3. Creating a Custom Iterator

**Example: Counter Iterator**
```python
class Counter:
    def __init__(self, max_num):
        self.max_num = max_num
        self.num = 0
    
    def __iter__(self):
        # Return self because this object is the iterator
        return self
    
    def __next__(self):
        if self.num >= self.max_num:
            raise StopIteration
        self.num += 1
        return self.num

# Usage
counter = Counter(5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5
```

**Example: Reverse Iterator**
```python
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Usage
for char in Reverse("hello"):
    print(char)  # o, l, l, e, h
```

---

## 4. Built-in Iterator Functions

**iter() and next():**
```python
# Create iterator from any iterable
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # StopIteration error

# Use default value to avoid error
iterator = iter([1, 2, 3])
print(next(iterator, "Done"))  # 1
print(next(iterator, "Done"))  # 2
print(next(iterator, "Done"))  # 3
print(next(iterator, "Done"))  # "Done" (no error!)
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01: You used `for` loops without knowing how they work
- Unit 09a: Now you understand the iterator protocol behind them
- This explains why lists, strings, and dicts are "iterable"

**Preparation for Next Lesson:**
- Unit 09b: Generators (easier way to create iterators)
- Generators use `yield` instead of `__iter__` and `__next__`
- Same concept, simpler syntax

**Real-World Application:**
- Reading large files line by line (memory efficient)
- Processing database query results
- Custom data structures need custom iterators
- Understanding framework internals
