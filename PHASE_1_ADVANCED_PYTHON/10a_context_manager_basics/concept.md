# Unit 10a: Context Manager Basics

## YouTube Recommendations
- "Python context managers"
- "Python with statement"

---

## 1. The with Statement

The `with` statement ensures resources are properly cleaned up, even if errors occur.

**Problem:**
```python
file = open('data.txt', 'r')
content = file.read()
file.close()  # Easy to forget!
```

**Solution:**
```python
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed!
```

---

## 2. How It Works

`with` calls `__enter__()` and `__exit__()` methods:

```python
# What happens internally:
file = open('data.txt', 'r')
file.__enter__()
try:
    content = file.read()
finally:
    file.__exit__()
```

---

## Spiral Learning Note

- Unit 10b: Create custom context managers
- Unit 10c: @contextmanager decorator
- Essential for resource management
