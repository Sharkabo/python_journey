# Task: Unique Visitor Tracker

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Store Visitor Data
Create an empty set called `visitors` to track unique visitor names.

## Goal 2: Collect Visitor Names
Use a while loop to repeatedly ask for visitor names. 
- If the user types "done", break the loop
- Otherwise, add the name to the `visitors` set

## Goal 3: Display Results
After the loop ends:
- Print the total number of unique visitors using `len(visitors)`
- Print the list of unique visitors

## Goal 4: Check Specific Visitor
Ask the user for a name and check if that person visited (use `in` operator).

---
**Expected Output:**
```text
Enter visitor name (or 'done' to finish): Alice
Enter visitor name (or 'done' to finish): Bob
Enter visitor name (or 'done' to finish): Alice
Enter visitor name (or 'done' to finish): done

Total unique visitors: 2
Visitors: {'Alice', 'Bob'}

Check if someone visited: Alice
Alice visited today!
```
