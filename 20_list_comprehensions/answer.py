# Complete your task here (refer to task.md)

# 1. Temperature Converter
temp_C = [0, 10, 20, 30, 40]
temp_F = [C * 9/5 + 32 for C in temp_C]
print(temp_F)
# 2. Filter Passing Grades
scores = [45, 67, 89, 52, 78, 91, 34, 88]
passing_grade = [score for score in scores if score >= 60]
print(passing_grade)
# 3. Clean User Input
source_inputs = ["  hello  ", "  world  ", "  python  "]
cleaned_inputs = [input.strip() for input in source_inputs]
print(cleaned_inputs)
# 4. Display All Results
print(f'Fahrenheit: {temp_F}\nPassing Grades: {passing_grade}\nCleaned Input: {cleaned_inputs}')
