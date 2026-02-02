# Task: Data Processor

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Temperature Converter
You have a list of temperatures in Celsius: `[0, 10, 20, 30, 40]`

Use list comprehension to convert them all to Fahrenheit using the formula:
`F = C * 9/5 + 32`

## Goal 2: Filter Passing Grades
You have a list of test scores: `[45, 67, 89, 52, 78, 91, 34, 88]`

Use list comprehension to create a new list containing only scores >= 60 (passing grades).

## Goal 3: Clean User Input
You have a list of user inputs with extra spaces: `["  hello  ", "  world  ", "  python  "]`

Use list comprehension with `.strip()` to clean all the strings.

## Goal 4: Display All Results
Print all three processed lists with descriptive labels.

---
**Expected Output:**
```text
Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]
Passing Grades: [67, 89, 78, 91, 88]
Cleaned Input: ['hello', 'world', 'python']
```
