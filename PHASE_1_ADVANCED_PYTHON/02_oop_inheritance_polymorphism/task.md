# Task: Create an Employee Management System

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Employee Base Class
Create an `Employee` class with the following:
- Attributes: `name`, `employee_id`, `base_salary`
- Method: `get_info()` - returns a formatted string with employee information
- Method: `calculate_salary()` - returns the base_salary (will be overridden by subclasses)

## Goal 2: Create Manager and Developer Subclasses
Create two child classes that inherit from Employee:

**Manager class:**
- Additional attribute: `team_size` (number of people managed)
- Override `calculate_salary()` to add a bonus: base_salary + (team_size * 1000)
- Add method: `manage_team()` - returns a message about managing the team

**Developer class:**
- Additional attribute: `programming_language` (primary language)
- Override `calculate_salary()` to add a skill bonus: base_salary + 5000
- Add method: `write_code()` - returns a message about writing code

## Goal 3: Demonstrate Polymorphism
Create a function called `print_employee_details(employee)` that:
- Accepts any Employee object (Employee, Manager, or Developer)
- Prints the employee's info using `get_info()`
- Prints the calculated salary using `calculate_salary()`

Test your function with instances of Employee, Manager, and Developer to demonstrate polymorphism.

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Employee: John Doe, ID: E001
Salary: $50000

Employee: Alice Smith, ID: M001
Salary: $65000
Alice Smith is managing a team of 15 people

Employee: Bob Johnson, ID: D001
Salary: $75000
Bob Johnson is writing code in Python
```
