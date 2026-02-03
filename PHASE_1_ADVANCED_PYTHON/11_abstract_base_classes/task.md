# Task: Build a Payment System with ABC

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create PaymentMethod ABC
Create an abstract base class `PaymentMethod` with:
- Abstract method: `process_payment(amount: float) -> bool`
- Abstract method: `get_transaction_fee(amount: float) -> float`
- Concrete method: `display_name() -> str` (return "Payment Method")

## Goal 2: Implement CreditCardPayment
Create a class `CreditCardPayment(PaymentMethod)` that:
- Implements `process_payment`: Print "Processing ${amount} via Credit Card" and return True
- Implements `get_transaction_fee`: Return 2.9% of amount
- Override `display_name`: Return "Credit Card"

## Goal 3: Implement PayPalPayment
Create a class `PayPalPayment(PaymentMethod)` that:
- Implements `process_payment`: Print "Processing ${amount} via PayPal" and return True
- Implements `get_transaction_fee`: Return 3.5% of amount  
- Override `display_name`: Return "PayPal"

## Goal 4: Create a checkout function
Create a function `checkout(payment_method: PaymentMethod, amount: float)` that:
- Calculates the fee using `get_transaction_fee`
- Processes the payment
- Prints the total (amount + fee)

## Goal 5: Test your implementation
Create instances and test the checkout function with both payment methods.

---

**Expected Output:**
```text
Payment method: Credit Card
Processing $100.00 via Credit Card
Transaction fee: $2.90
Total charge: $102.90

Payment method: PayPal
Processing $100.00 via PayPal
Transaction fee: $3.50
Total charge: $103.50
```
