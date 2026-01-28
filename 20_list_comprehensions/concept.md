# Unit 20: List Comprehensions

## 1. What is List Comprehension?
List comprehension is a **shortcut** to create lists using a single line of code. It's a more "Pythonic" way to transform data.

**Traditional Way (Unit 06):**
```python
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(doubled)  # [2, 4, 6, 8, 10]
```

**List Comprehension Way:**
```python
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
```

**Syntax:**
```python
new_list = [expression for item in iterable]
```

---

## 2. Adding Conditions
You can filter items using `if` inside the comprehension.

**Example - Only Even Numbers:**
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # [2, 4, 6]
```

**Example - Transform and Filter:**
```python
words = ["hello", "world", "python"]
uppercase_long = [word.upper() for word in words if len(word) > 5]
print(uppercase_long)  # ["PYTHON"]
```

---

## Spiral Learning Note
List comprehensions are powerful shortcuts for creating lists. They combine loops (Unit 06), conditions (Unit 04), and list operations (Unit 05) into one elegant line!
