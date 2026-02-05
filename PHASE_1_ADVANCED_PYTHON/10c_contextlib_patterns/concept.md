# Unit 10c: Contextlib Patterns

## YouTube Recommendations
- "Python contextlib"
- "Python contextmanager decorator"

---

## 1. @contextmanager Decorator

Simpler syntax using generators:

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_manager('data.txt', 'w') as f:
    f.write("Easy!")
```

---

## 2. How It Works

- Code before `yield` = `__enter__()`
- `yield` value = returned resource
- Code after `yield` = `__exit__()`

---

## Spiral Learning Note

Uses generators from Unit 09b. Preferred for simple cases.
