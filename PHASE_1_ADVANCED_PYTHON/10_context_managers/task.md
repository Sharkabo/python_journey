# Task: Build Resource Management System with Context Managers

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create TemporaryFile Context Manager
Create a class-based context manager called `TemporaryFile` that:
- Takes a filename in `__init__`
- Creates and opens a temporary file in `__enter__` (mode 'w+')
- Returns the file object from `__enter__`
- Closes and deletes the file in `__exit__`
- Handles exceptions properly (ensure file is deleted even if error occurs)
- Use `os.remove()` to delete the file

## Goal 2: Create Database Transaction Context Manager
Create a context manager using `@contextmanager` decorator called `transaction` that:
- Accepts a mock database connection object
- Prints "Starting transaction" when entering
- Yields the connection object
- If no exception: prints "Committing transaction" and calls connection.commit()
- If exception occurs: prints "Rolling back transaction" and calls connection.rollback(), then re-raises the exception
- Use try/except/finally structure  

Create a simple MockDB class with commit() and rollback() methods for testing.

## Goal 3: Create Resource Pool Context Manager
Create a context manager using `@contextmanager` called `acquire_resource` that:
- Accepts a resource pool (list of available resources)
- Gets a resource from the pool when entering
- Yields the resource
- Returns the resource to the pool when exiting
- Handles the case when pool is empty (raise Exception)

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Testing TemporaryFile:
File created: temp_test.txt
Writing to temporary file...
File deleted: temp_test.txt

Testing Database Transaction (Success):
Starting transaction
Executing query...
Committing transaction

Testing Database Transaction (Failure):
Starting transaction
Executing bad query...
Rolling back transaction
Exception handled: Database error!

Testing Resource Pool:
Acquired resource: Server-1
Using Server-1...
Released resource: Server-1
Available resources: ['Server-1', 'Server-2', 'Server-3']
```
