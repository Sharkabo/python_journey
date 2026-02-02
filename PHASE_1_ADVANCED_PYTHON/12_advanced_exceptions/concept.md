# Unit 12: Advanced Exception Handling

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python custom exceptions"
- "Python exception hierarchy"
- "Python try except best practices"

Recommended Channels:
- Corey Schafer (Python)
- ArjanCodes (Software Design)
- mCoding (Advanced Python)

---

## 1. Review: Basic Exception Handling

You learned basic try/except in Phase 0. Let's review and expand:

**Basic Pattern:**
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero!")
except Exception as e:
    # Catch all other exceptions
    print(f"An error occurred: {e}")
finally:
    # Always executes (cleanup code)
    print("Cleanup complete")
```

---

## 2. Creating Custom Exceptions

Custom exceptions make your code more expressive and easier to debug.

**Basic Custom Exception:**
```python
class ValidationError(Exception):
    """Raised when input validation fails"""
    pass

def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative")
    if age > 150:
        raise ValidationError("Age is unrealistic")
    return age

try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation failed: {e}")
```

**Custom Exception with Attributes:**
```python
class AuthenticationError(Exception):
    """Raised when authentication fails"""
    def __init__(self, username, message="Authentication failed"):
        self.username = username
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} for user: {self.username}"

try:
    raise AuthenticationError("alice123", "Invalid password")
except AuthenticationError as e:
    print(e)  # Authentication failed for user: alice123
    print(f"Username: {e.username}")
```

---

## 3. Exception Hierarchy

Creating a hierarchy of exceptions for better organization:

```python
class AppError(Exception):
    """Base exception for all application errors"""
    pass

class DatabaseError(AppError):
    """Database-related errors"""
    pass

class ConnectionError(DatabaseError):
    """Database connection errors"""
    pass

class QueryError(DatabaseError):
    """SQL query errors"""
    pass

class ValidationError(AppError):
    """Input validation errors"""
    pass

class UserNotFoundError(AppError):
    """User not found in system"""
    pass

# Usage
def get_user_from_db(user_id):
    try:
        # Simulate database query
        if user_id < 0:
            raise ValidationError("User ID must be positive")
        if user_id > 1000:
            raise UserNotFoundError(f"User {user_id} not found")
        # Simulate connection error
        raise ConnectionError("Could not connect to database")
    except DatabaseError as e:
        # Catches both ConnectionError and QueryError
        print(f"Database error: {e}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except AppError as e:
        # Catches all app errors
        print(f"Application error: {e}")
```

---

## 4. FastAPI-Style HTTP Exceptions

This prepares you for FastAPI's exception handling:

```python
class HTTPException(Exception):
    """Base HTTP exception"""
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)

class NotFoundException(HTTPException):
    def __init__(self, detail="Resource not found"):
        super().__init__(status_code=404, detail=detail)

class UnauthorizedException(HTTPException):
    def __init__(self, detail="Unauthorized"):
        super().__init__(status_code=401, detail=detail)

class BadRequestException(HTTPException):
    def __init__(self, detail="Bad request"):
        super().__init__(status_code=400, detail=detail)

# Usage (similar to FastAPI)
def get_user(user_id):
    if user_id < 0:
        raise BadRequestException("User ID must be positive")
    if user_id > 1000:
        raise NotFoundException(f"User {user_id} not found")
    return {"id": user_id, "name": "Alice"}

try:
    user = get_user(9999)
except HTTPException as e:
    print(f"HTTP {e.status_code}: {e.detail}")
```

---

## 5. Context Managers for Exception Safety

Using context managers to ensure cleanup even when exceptions occur:

```python
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to {self.connection_string}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnecting from database")
        self.connected = False
        
        # Return False to propagate exceptions
        # Return True to suppress exceptions
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        return False  # Don't suppress exceptions

# Usage
try:
    with DatabaseConnection("postgres://localhost") as db:
        print("Performing database operations...")
        raise ValueError("Simulated error")
        print("This won't execute")
except ValueError as e:
    print(f"Caught exception: {e}")
# Output:
# Connecting to postgres://localhost
# Performing database operations...
# Exception occurred: ValueError: Simulated error
# Disconnecting from database
# Caught exception: Simulated error
```

---

## 6. Exception Chaining

Preserve the original exception while raising a new one:

```python
class DataProcessingError(Exception):
    pass

def process_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
            # Simulate processing error
            result = int(data)  # May raise ValueError
            return result
    except FileNotFoundError as e:
        # Chain the exception
        raise DataProcessingError(f"Cannot process {filename}") from e
    except ValueError as e:
        raise DataProcessingError(f"Invalid data in {filename}") from e

try:
    process_file("nonexistent.txt")
except DataProcessingError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")
```

---

## 7. Best Practices for Exception Handling

**DO:**
- Create specific exception types for different error conditions
- Catch only exceptions you can handle
- Log exceptions with context
- Use exception hierarchy for organization
- Clean up resources in `finally` or context managers

**DON'T:**
- Use bare `except:` (catches everything including KeyboardInterrupt)
- Silence exceptions without logging
- Use exceptions for control flow
- Catch `Exception` unless you re-raise it

**Good Example:**
```python
class UserService:
    def create_user(self, user_data):
        try:
            # Validate
            if not user_data.get('email'):
                raise ValidationError("Email is required")
            
            # Save to database
            self.db.save(user_data)
            
        except ValidationError:
            # Let it propagate - caller should handle
            raise
        except DatabaseError as e:
            # Log and re-raise with context
            print(f"Failed to create user: {e}")
            raise
        except Exception as e:
            # Unexpected error - log and wrap
            print(f"Unexpected error creating user: {e}")
            raise AppError("User creation failed") from e
```

---

## 8. Real-World FastAPI Example

This is how you'll handle exceptions in FastAPI:

```python
# Custom exceptions for your API
class ItemNotFoundException(HTTPException):
    def __init__(self, item_id):
        super().__init__(
            status_code=404,
            detail=f"Item {item_id} not found"
        )

class InvalidItemDataException(HTTPException):
    def __init__(self, errors):
        super().__init__(
            status_code=422,
            detail={"message": "Invalid item data", "errors": errors}
        )

# Service layer
def get_item(item_id):
    if item_id < 0:
        raise InvalidItemDataException(["Item ID must be positive"])
    
    # Simulate database lookup
    item = None  # Not found
    
    if item is None:
        raise ItemNotFoundException(item_id)
    
    return item

# API endpoint (simplified)
def api_get_item(item_id):
    try:
        return get_item(item_id)
    except HTTPException:
        # FastAPI will handle this automatically
        raise
    except Exception as e:
        # Log unexpected errors
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- You know basic try/except (Phase 0, Unit 17)
- You've learned ABCs which raise TypeErrors (Unit 11)
- Custom exceptions make your code more professional

**Preparation for Next Lesson:**
- Unit 13 starts Data Structures (Linked Lists)
- Good exception handling is crucial for robust data structures
- You'll use custom exceptions in your implementations
