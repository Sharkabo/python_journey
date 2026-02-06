# Task: Build Abstract Shape System

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Abstract Shape Class
Create an abstract `Shape` class that:
- Uses ABC (Abstract Base Class)
- Defines abstract method `area()`
- Defines abstract method `perimeter()`
- Cannot be instantiated directly

## Goal 2: Create Concrete Shape Classes
Implement these classes:
- `Rectangle(length, width)` - implements area() and perimeter()
- `Circle(radius)` - implements area() and perimeter()
- Both inherit from Shape

## Goal 3: Demonstrate Abstract Classes
Show that:
- Abstract Shape cannot be instantiated
- Concrete shapes work correctly
- All shapes follow the same interface

---

**Expected Output:**
```text
Error: Cannot instantiate abstract class Shape

Rectangle: area=20, perimeter=18
Circle: area=78.54, perimeter=31.42
```
