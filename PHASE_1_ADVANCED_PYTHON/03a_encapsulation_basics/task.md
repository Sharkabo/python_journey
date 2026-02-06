# Task: Build an Encapsulated BankAccount System

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a BankAccount Class
Create a `BankAccount` class that demonstrates encapsulation:
- Use a private attribute `__balance` to store the account balance
- Add a private attribute `__account_number`
- Include a public attribute `holder` for the account holder's name
- Initialize the account with holder name, account number, and starting balance

## Goal 2: Implement Account Operations
Add methods to safely interact with the private balance:
- `deposit(amount)` - adds money to the account (validate amount > 0)
- `withdraw(amount)` - removes money if balance is sufficient
- `get_balance()` - returns the current balance
- `get_account_info()` - returns formatted account information

---
**Expected Output:**
When you run the code, the terminal should show:
```text
Account holder: Alice Johnson
Account number: 123-456-789
Initial balance: $1000.00
After deposit: $1500.00
After withdrawal: $1200.00
Final balance: $1200.00
```
