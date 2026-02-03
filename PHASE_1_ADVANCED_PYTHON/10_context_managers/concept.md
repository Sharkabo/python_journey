# Unit 10: Context Managers

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python context managers tutorial"
- "Python with statement"
- "Python __enter__ __exit__"
- "Python contextlib module"
- "Python 上下文管理器"

Recommended Channels:
- Corey Schafer (Python)
- ArjanCodes (Advanced Python)
- mCoding (Python internals)
- Real Python (Written tutorials)

---

## 1. What are Context Managers?

Context managers are objects that manage resources (like files, network connections, locks) and ensure proper cleanup even if errors occur. They use the `with` statement for elegant resource management.

**Key Benefits:**
- Automatic resource cleanup (no need to manually close files)
- Guaranteed cleanup even if exceptions occur
- Makes code cleaner and more readable
- Prevents resource leaks

**Common Use Case - File Handling:**
```python
# Without context manager (BAD - risky)
file = open('data.txt', 'r')
data = file.read()
file.close()  # What if an error occurs before this?

# With context manager (GOOD - guaranteed cleanup)
with open('data.txt', 'r') as file:
    data = file.read()
# File is automatically closed here, even if error occurs
```

---

## 2. The with Statement

The `with` statement calls special methods on context manager objects:
- `__enter__()` - Called when entering the with block
- `__exit__()` - Called when exiting the with block (even if error occurs)

**How it Works:**
```python
with context_manager as variable:
    # Use the resource
    pass
# Resource is cleaned up here

# This is equivalent to:
variable = context_manager.__enter__()
try:
    # Use the resource
    pass
finally:
    context_manager.__exit__(exc_type, exc_value, traceback)
```

---

## 3. Creating Custom Context Managers (Class-Based)

Create a custom context manager by implementing `__enter__` and `__exit__` methods.

**Basic Example:**
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Opens file and returns file object"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Closes file, called even if exception occurs"""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        # Return True to suppress exceptions
        return False

# Using the context manager
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
# Output:
# Opening test.txt
# Closing test.txt
```

**Handling Exceptions:**
```python
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        print("Connecting to database...")
        # Simulating database connection
        self.connection = {"connected": True}
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection...")
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            # Log the error, rollback transaction, etc.
        self.connection = None
        return False  # Don't suppress the exception

# Using with exception handling
try:
    with DatabaseConnection("localhost") as db:
        print("Working with database...")
        raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"Caught: {e}")

# Output:
# Connecting to database...
# Working with database...
# Closing database connection...
# Exception occurred: ValueError: Something went wrong!
# Caught: Something went wrong!
```

---

## 4. Creating Context Managers with contextlib

The `contextlib` module provides tools for creating context managers more easily.

**Using @contextmanager Decorator:**
```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """Context manager using generator function"""
    # Setup (before yield)
    print(f"Opening {filename}")
    file = open(filename, mode)
    
    try:
        yield file  # Yield the resource
    finally:
        # Cleanup (after yield, always runs)
        print(f"Closing {filename}")
        file.close()

# Using the context manager
with file_manager('test.txt', 'w') as f:
    f.write('Hello from contextlib!')
```

**Timer Context Manager:**
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    """Context manager to measure execution time"""
    start = time.time()
    print(f"Starting {name}...")
    
    yield  # No resource to return
    
    end = time.time()
    print(f"{name} took {end - start:.4f} seconds")

# Using the timer
with timer("Data processing"):
    time.sleep(1)
    # Do some work
    print("Processing data...")

# Output:
# Starting Data processing...
# Processing data...
# Data processing took 1.0012 seconds
```

---

## 5. Practical Context Manager Examples

**Directory Changer:**
```python
import os
from contextlib import contextmanager

@contextmanager
def change_directory(path):
    """Temporarily change working directory"""
    original_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original_dir)

# Usage
print(f"Current dir: {os.getcwd()}")
with change_directory('/tmp'):
    print(f"Inside context: {os.getcwd()}")
print(f"After context: {os.getcwd()}")
```

**Temporary Attribute Setter:**
```python
from contextlib import contextmanager

class Config:
    debug = False
    verbose = False

@contextmanager
def temporary_config(**kwargs):
    """Temporarily modify config settings"""
    # Save original values
    original = {key: getattr(Config, key) for key in kwargs}
    
    # Set new values
    for key, value in kwargs.items():
        setattr(Config, key, value)
    
    try:
        yield Config
    finally:
        # Restore original values
        for key, value in original.items():
            setattr(Config, key, value)

# Usage
print(f"Debug: {Config.debug}")  # False

with temporary_config(debug=True, verbose=True):
    print(f"Inside: Debug={Config.debug}, Verbose={Config.verbose}")
    # Debug=True, Verbose=True

print(f"After: Debug={Config.debug}")  # False
```

**Resource Pool Manager:**
```python
class ConnectionPool:
    def __init__(self, size):
        self.pool = [f"Connection-{i}" for i in range(size)]
        self.in_use = set()
    
    def acquire(self):
        if not self.pool:
            raise Exception("No connections available")
        conn = self.pool.pop()
        self.in_use.add(conn)
        print(f"Acquired {conn}")
        return conn
    
    def release(self, conn):
        if conn in self.in_use:
            self.in_use.remove(conn)
            self.pool.append(conn)
            print(f"Released {conn}")
    
    def get_connection(self):
        """Returns a context manager for a connection"""
        class ConnectionContext:
            def __init__(self, pool):
                self.pool = pool
                self.conn = None
            
            def __enter__(self):
                self.conn = self.pool.acquire()
                return self.conn
            
            def __exit__(self, exc_type, exc_value, traceback):
                self.pool.release(self.conn)
                return False
        
        return ConnectionContext(self)

# Usage
pool = ConnectionPool(2)

with pool.get_connection() as conn1:
    print(f"Using {conn1}")
    with pool.get_connection() as conn2:
        print(f"Using {conn2}")
    print("conn2 released")
print("conn1 released")
```

---

## 6. Multiple Context Managers

You can use multiple context managers in a single with statement.

**Multiple Contexts:**
```python
# Open multiple files at once
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())
# Both files automatically closed

# Or stack them
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        content = infile.read()
        outfile.write(content.upper())
```

**Using contextlib.ExitStack:**
```python
from contextlib import ExitStack

def process_files(filenames):
    with ExitStack() as stack:
        # Open multiple files dynamically
        files = [stack.enter_context(open(fname)) for fname in filenames]
        
        # Process all files
        for f in files:
            print(f.read())
    # All files automatically closed
```

---

## 7. suppress() Context Manager

The `contextlib.suppress()` context manager suppresses specified exceptions.

**Example:**
```python
from contextlib import suppress
import os

# Without suppress (verbose)
try:
    os.remove('nonexistent_file.txt')
except FileNotFoundError:
    pass  # Ignore if file doesn't exist

# With suppress (cleaner)
with suppress(FileNotFoundError):
    os.remove('nonexistent_file.txt')

# Suppress multiple exceptions
with suppress(FileNotFoundError, PermissionError):
    os.remove('some_file.txt')
```

---

## 8. Context Managers in Real Applications

**Database Transactions:**
```python
@contextmanager
def database_transaction(connection):
    """Manage database transactions with automatic rollback"""
    try:
        yield connection
        connection.commit()  # Success: commit
        print("Transaction committed")
    except Exception as e:
        connection.rollback()  # Error: rollback
        print(f"Transaction rolled back: {e}")
        raise

# Usage
with database_transaction(db_connection) as conn:
    conn.execute("INSERT INTO users VALUES (...)")
    conn.execute("UPDATE accounts SET ...")
```

**Thread Locks:**
```python
import threading

lock = threading.Lock()

# Using lock as context manager
with lock:
    # Critical section
    # Only one thread can be here at a time
    shared_resource.modify()
# Lock automatically released
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 09: Generators use `yield`; context managers with @contextmanager also use `yield`
- Unit 07: Decorators are used with @contextmanager
- File handling from Phase 0 is improved with context managers

**Preparation for Next Lesson:**
- Unit 11: Abstract Base Classes will define interfaces for resources
- Context managers ensure resources are properly managed regardless of type
- Both concepts promote robust, maintainable code

**Real-World Application:**
- File operations in production code
- Database connections and transactions
- Network socket management
- FastAPI dependency injection uses context manager patterns
- Thread locks and synchronization
- Temporary environment changes (config, directories)
- This is essential for building reliable, production-ready applications
