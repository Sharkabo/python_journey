# Unit 10b: Custom Context Managers

## YouTube Recommendations
- "Python custom context manager"
- "Python __enter__ __exit__"

---

## 1. Creating Context Managers

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with FileManager('data.txt', 'w') as f:
    f.write("Hello!")
```

---

## 2. Timer Example

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        print(f"Took {time.time() - self.start:.2f}s")

with Timer():
    time.sleep(2)
# Prints: Took 2.00s
```

---

## Spiral Learning Note

Unit 10c: @contextmanager makes this easier
