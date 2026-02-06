# Task: Build Repository Pattern with ABC

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Abstract Repository
Create an abstract `Repository` class that:
- Defines abstract methods: `save()`, `get()`, `delete()`
- Uses @abstractmethod decorator
- Enforces interface for all repositories

## Goal 2: Implement Concrete Repositories
Create these implementations:
- `MemoryRepository` - stores data in a dictionary
- `FileRepository` - stores data in files (simulated)
- Both implement all abstract methods

## Goal 3: Use Polymorphism
Demonstrate:
- Swapping repositories without changing code
- Common interface benefits
- Real-world design pattern

---

**Expected Output:**
```text
Memory Repository:
Saved user: Alice
Retrieved: Alice
Deleted: Alice

File Repository:
Saved user: Bob
Retrieved: Bob
```
