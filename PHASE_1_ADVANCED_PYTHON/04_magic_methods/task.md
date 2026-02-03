# Task: Custom Product Class with Magic Methods

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Product Class
Create a `Product` class with:
- Attributes: `name`, `price`, `quantity`
- Implement `__init__` to initialize these attributes

## Goal 2: Implement String Representations
- Add `__str__`: Return "{name} - ${price}"
- Add `__repr__`: Return "Product(name='{name}', price={price}, quantity={quantity})"

## Goal 3: Implement Comparison Methods
- Add `__eq__`: Two products are equal if they have the same name
- Add `__lt__`: Compare products by price (for sorting)

## Goal 4: Implement Arithmetic
- Add `__add__`: Adding two products combines their quantities (same product only)
- Raise ValueError if trying to add different products

## Goal 5: Test Your Implementation
Create multiple products, test all magic methods.

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
str: Laptop - $999
repr: Product(name='Laptop', price=999, quantity=5)

Comparison:
laptop == phone: False
laptop < phone: False (laptop is more expensive)

Addition:
laptop1 + laptop2 = Product(name='Laptop', price=999, quantity=15)
```
