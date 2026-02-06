# Task: Build Exception Patterns with Context

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Exceptions with Additional Data
Create exceptions that:
- Store error code and message
- Include timestamp
- Provide method to format error

## Goal 2: Create Exception Hierarchy
Build this structure:
- `AppError` (base)
  - `DatabaseError(AppError)`
  - `APIError(AppError)`
  - `NetworkError(AppError)`

## Goal 3: Implement Exception Handling Patterns
Demonstrate:
- Try/except with multiple exception types
- Finally blocks for cleanup
- Re-raising exceptions with additional context

---

**Expected Output:**
```text
[2026-02-06 15:30:00] DatabaseError (code: 500): Connection failed
Cleanup executed
Error logged and re-raised
```
