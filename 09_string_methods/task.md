# Task: Username Formatter

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Clean User Input
Ask the user to input their name. Use `.strip()` to remove extra spaces, then use `.title()` to capitalize the first letter of each word.

## Goal 2: Create a Username
Take the cleaned name and create a username by:
- Converting to lowercase
- Replacing spaces with underscores using `.replace()`

## Goal 3: Display Result
Use an f-string to print: `"Welcome, [Name]! Your username is: [username]"`

---
**Expected Output:**
If the user inputs `"  john doe  "`, the terminal should show:
```text
Enter your name:   john doe  
Welcome, John Doe! Your username is: john_doe
```
