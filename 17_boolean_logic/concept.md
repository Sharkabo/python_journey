# Unit 17: Boolean Logic & Operators

## 1. Boolean Values
In Python, `True` and `False` are special values that represent yes/no, on/off.

**Comparison Operators:**
```python
age = 20
print(age > 18)      # True
print(age < 18)      # False
print(age == 20)     # True (equal to)
print(age != 25)     # True (not equal to)
```

---

## 2. Logical Operators
We can combine multiple conditions using `and`, `or`, and `not`.

**AND - Both must be True:**
```python
age = 20
has_license = True
if age >= 18 and has_license:
    print("You can drive!")
```

**OR - At least one must be True:**
```python
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today!")
```

**NOT - Reverses the value:**
```python
is_raining = False
if not is_raining:
    print("Let's go outside!")
```

---

## Spiral Learning Note
We used `if` statements in Unit 04, but now we can create more complex conditions! This is essential for real-world decision-making in programs.
