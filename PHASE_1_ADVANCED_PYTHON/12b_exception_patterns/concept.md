# Unit 12b: Exception Patterns

## YouTube Recommendations
- "Python exception hierarchy"
- "Python exception best practices"

---

## 1. Exception with Data

```python
class APIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

try:
    raise APIError(404, "Not Found")
except APIError as e:
    print(f"{e.status_code}: {e.message}")
```

---

## Spiral Learning Note

Store extra data in exceptions for better debugging.
