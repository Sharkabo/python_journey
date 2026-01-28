# Unit 20: Tuples & Sets

## 1. Tuples - Immutable Lists
Tuples are like lists (Unit 05), but they **cannot be changed** after creation. Use parentheses `()` instead of brackets.

**Syntax:**
```python
coordinates = (10, 20)
rgb_color = (255, 128, 0)
```

**Why Use Tuples?**
- Protect data from accidental changes
- Faster than lists
- Can be used as dictionary keys (lists cannot)

**Example:**
```python
point = (3, 4)
x, y = point  # Unpacking
print(f"X: {x}, Y: {y}")  # X: 3, Y: 4
```

---

## 2. Sets - Unique Collections
Sets store **unique** values only (no duplicates). Use curly braces `{}`.

**Syntax:**
```python
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3} - duplicates removed!
```

**Common Operations:**
```python
fruits = {"apple", "banana"}
fruits.add("cherry")
fruits.remove("banana")

# Check membership
if "apple" in fruits:
    print("We have apples!")
```

**Set Math:**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # {3} - intersection
print(set1 | set2)  # {1, 2, 3, 4, 5} - union
```

---

## Spiral Learning Note
Lists (Unit 05) are flexible. Tuples are for fixed data. Sets are for unique collections. Choose the right tool for the job!
