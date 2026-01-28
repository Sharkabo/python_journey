# Unit 18: Function Return Values

## 1. What is Return?
In Unit 07, we learned to create functions that **do** things (like print). Now we learn to create functions that **give back** values.

Think of a function like a vending machine:
- You put in money (parameters)
- It **returns** a snack (return value)

**Syntax:**
```python
def function_name(parameter):
    result = parameter * 2
    return result
```

**Example:**
```python
def add_five(number):
    return number + 5

result = add_five(10)
print(result)  # 15
```

---

## 2. Using Return Values
The power of `return` is that we can **store** the result and use it later!

**Example:**
```python
def calculate_tax(price):
    return price * 0.1

item_price = 100
tax = calculate_tax(item_price)
total = item_price + tax
print(f"Total: ${total}")  # Total: $110.0
```

**Multiple Returns:**
```python
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

status = check_age(20)
print(status)  # "Adult"
```

---

## Spiral Learning Note
Functions from Unit 07 just performed actions. Now they can **produce values** that we can use in calculations, store in variables, or pass to other functions!
