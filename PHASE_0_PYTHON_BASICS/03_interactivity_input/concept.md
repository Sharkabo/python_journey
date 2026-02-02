# Unit 03: Interactivity (Input)

## 1. Getting User Input
To make programs interactive, we use `input()`. This pauses the program and waits for the user to type something.

**Syntax:**
```python
variable = input("Prompt text: ")
```

**Example:**
```python
name = input("What is your name? ")
print("Hello " + name)
```

## 2. Converting Input Types
IMPORTANT: `input()` ALWAYS returns **Text (String)**, even if the user types a number.
To do math, you must convert it to a number using `int()`.

**Example:**
```python
age_text = input("Enter your age: ")
age = int(age_text) # Convert to integer
print(age + 1)
```

---

## Spiral Learning Note
We used `print` (Unit 01) and variables (Unit 01). Now we combine them with `input`. If we didn't convert `age` to an `int` (Unit 02), the math would fail!
