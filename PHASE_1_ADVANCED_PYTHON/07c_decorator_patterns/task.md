# Task: Implement Production-Ready Decorator Patterns

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Retry Decorator
Create a decorator that:
- Retries a function if it raises an exception
- Accepts `max_attempts` parameter
- Adds delay between retries

## Goal 2: Create a Caching/Memoization Decorator
Create a decorator that:
- Stores function results based on arguments
- Returns cached result for repeated calls
- Works with different argument types

## Goal 3: Combine Decorator Patterns
Demonstrate:
- Stacking retry + caching decorators
- Real-world use cases
- Performance improvements

---

**Expected Output:**
```text
Attempt 1 failed, retrying...
Attempt 2 succeeded
Cached result returned instantly
```
