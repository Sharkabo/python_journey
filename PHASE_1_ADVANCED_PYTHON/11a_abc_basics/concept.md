# Unit 11a: ABC Basics

## YouTube Recommendations
- "Python ABC tutorial"
- "Python abstract methods"

---

## 1. What are Abstract Base Classes?

ABCs define an interface that subclasses must implement.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h

rect = Rectangle(5, 3)
print(rect.area())  # 15
```

---

## Spiral Learning Note

Forces subclasses to implement required methods. Common in large projects.
