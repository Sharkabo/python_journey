# Task: Create a Smart Bank Account System

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create BankAccount Class with Encapsulation
Create a `BankAccount` class with the following:
- Protected attribute: `_balance` (initialized in `__init__` with owner name and initial balance)
- Public attribute: `owner`
- Public attribute: `account_number` (auto-generated, could be a simple incrementing number)
- Method: `deposit(amount)` - adds to balance if amount is positive
- Method: `withdraw(amount)` - subtracts from balance if sufficient funds and amount is positive
- Method: `get_balance()` - returns the current balance

## Goal 2: Add Property for Balance with Validation
Convert the balance access to use properties:
- Add `@property` for `balance` that returns `_balance`
- Add `@balance.setter` that validates:
  - Balance cannot be set to negative values
  - Raise `ValueError` with appropriate message if validation fails

## Goal 3: Create SavingsAccount with Interest
Create a `SavingsAccount` class that inherits from `BankAccount`:
- Additional protected attribute: `_interest_rate` (e.g., 0.05 for 5%)
- Override `__init__` to accept owner, initial_balance, and interest_rate
- Add property `interest_rate` with getter and setter (validate rate is between 0 and 1)
- Add method: `apply_interest()` - adds interest to balance (balance * interest_rate)
- Add read-only property: `projected_balance` - returns balance after one year of monthly compound interest

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Account: Alice (ACC001)
Initial Balance: $1000
After deposit: $1500
After withdrawal: $1300

Savings Account: Bob (ACC002)
Initial Balance: $5000
Interest Rate: 5.0%
After applying interest: $5250.0
Projected balance after 1 year: $5511.62
```
