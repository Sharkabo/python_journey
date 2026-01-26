# Unit 12: Error Handling (Try/Except)

## 1. When Things Crash
If a user enters text when you asked for a number, your program crashes (ValueError).
We can catch these errors.

**Syntax:**
```python
try:
    # Dangerous code
    x = int(input("Enter number: "))
except ValueError:
    # Run this if it crashes
    print("That was not a number!")
```

## 2. Why Use It?
It makes your program "robust". It won't die unexpectedly.

---

## Spiral Learning Note
Remember Unit 03 (Input)? This basically fixes the biggest problem with `input()` — users typing the wrong thing.
