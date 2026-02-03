# Task: Functional Programming Practice

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Lambda Basics
Create lambda functions for:
- Double a number
- Check if a number is even
- Calculate the area of a circle (given radius)

## Goal 2: Using map()
Given a list of prices [10, 25, 50, 100]:
- Use map() to add 20% tax to each price
- Use map() to convert to formatted strings like "$10.00"

## Goal 3: Using filter()
Given a list of products with 'name' and 'price':
```python
products = [
    {'name': 'Laptop', 'price': 999},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Keyboard', 'price': 75},
    {'name': 'Monitor', 'price': 300}
]
```
- Filter products under $100
- Filter products with names longer than 5 characters

## Goal 4: Custom Sorting
Sort the products list by:
- Price (ascending)
- Name length (descending)

## Goal 5: Using reduce()
- Calculate the total price of all products
- Find the most expensive product

---

**Expected Output:**
```text
Doubled: [20, 50, 100, 200]
With tax: [12.0, 30.0, 60.0, 120.0]
Cheap products: [Mouse, Keyboard]
Sorted by price: [Mouse ($25), Keyboard ($75), Monitor ($300), Laptop ($999)]
Total price: $1399
Most expensive: Laptop
```
