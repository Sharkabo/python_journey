# Unit 12a: Custom Exceptions

## YouTube Recommendations
- "Python custom exceptions"
- "Python exception handling"

---

## 1. Creating Custom Exceptions

```python
class ValidationError(Exception):
    pass

class User:
    def __init__(self, age):
        if age < 0:
            raise ValidationError("Age cannot be negative")
        self.age = age

try:
    user = User(-5)
except ValidationError as e:
    print(e)  # Age cannot be negative
```

---

## Spiral Learning Note

Custom exceptions make error handling more specific and clear.
