# Task: Use @contextmanager Decorator

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Context Managers with @contextmanager
Use the decorator to create:
- A file manager using yield
- Simpler syntax than __enter__/__exit__
- Proper try/finally for cleanup

## Goal 2: Create a Temporary Directory Manager
Create a context manager that:
- Creates a temp directory on enter
- Yields the directory path
- Cleans up on exit

## Goal 3: Stack Multiple Context Managers
Demonstrate:
- Using multiple @contextmanager decorators
- Nesting context managers
- Real-world patterns

---

**Expected Output:**
```text
Created temp directory: /tmp/xyz
Working in temp directory...
Cleaned up temp directory

All resources managed safely!
```
