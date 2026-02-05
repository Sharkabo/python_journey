# Unit 11b: ABC Patterns

## YouTube Recommendations
- "Python ABC patterns"
- "Python repository pattern"

---

## 1. Repository Pattern

```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(self, data):
        pass
    
    @abstractmethod
    def get(self, id):
        pass

class SQLRepository(Repository):
    def save(self, data):
        # Save to SQL
        pass
    
    def get(self, id):
        # Get from SQL
        pass
```

---

## Spiral Learning Note

Ensures consistency across implementations. Used in frameworks.
