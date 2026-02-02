# Unit 06: Loops & Repetition

## 1. The For Loop
Loops allow us to repeat code without copying and pasting.
The `for` loop is great for going through a List (Unit 05).

**Syntax:**
```python
for item in list_name:
    # Do something with item
```

**Example:**
```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello " + name)
```
This prints 3 times!

## 2. Ranges
If you just want to repeat code 5 times, use `range()`.
`range(5)` creates a sequence: 0, 1, 2, 3, 4.

**Example:**
```python
for i in range(3):
    print("Repeat!")
```

---

## Spiral Learning Note
Loops let us process Lists (Unit 05) automatically. We can also use `if` (Unit 04) inside a loop to filter items!
