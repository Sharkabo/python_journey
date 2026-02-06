# Task: Build Custom Context Managers

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Timer Context Manager
Create a class that:
- Implements `__enter__` and `__exit__`
- Measures code execution time
- Prints elapsed time on exit

## Goal 2: Create a Database Connection Manager
Create a class that:
- Simulates database connection
- Auto-commits on success
- Auto-rollbacks on exceptions

## Goal 3: Handle Exceptions Properly
Demonstrate:
- Catching exceptions in `__exit__`
- Proper cleanup even on errors
- Returning True/False from `__exit__`

---

**Expected Output:**
```text
Connecting to database...
Operation succeeded - committed
Connection closed

Exception occurred - rolled back
Connection closed safely
```
