# Task: Build a Product Catalog with Read-Only Properties

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Product Class with Read-Only ID
Create a `Product` class with:
- Read-only `id` property (can only be set during initialization)
- Public `name` and `price` attributes that can be modified
- A computed `display_name` property showing formatted product info

## Goal 2: Add Child Class with Property Override
Create a `DiscountedProduct` subclass reference

that:
- Inherits from Product
- Overrides the `price` property to apply a discount
- Shows how properties work with inheritance

---

**Expected Output:**
```text
Product: #P001 - Laptop ($999.99)
Cannot change product ID
Discounted product: #P002 - Mouse ($15.99)
```
