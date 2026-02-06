# Task: Build Custom Exception System

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Custom Exceptions
Define these exception classes:
- `ValidationError(Exception)` - for validation failures
- `AgeValidationError(ValidationError)` - for invalid age
- `EmailValidationError(ValidationError)` - for invalid email

## Goal 2: Create a User Validator
Create a function that:
- Validates  user age (must be 0-150)
- Validates email format (must contain @)
- Raises appropriate custom exceptions

## Goal 3: Handle Custom Exceptions
Demonstrate:
- Catching specific exception types
- Exception hierarchies
- Proper error messages

---

**Expected Output:**
```text
Valid user created
Error: Age must be between 0 and 150
Error: Email must contain @
```
