# Task: Add Type Hints to a Student Management System

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Student Class with Type Hints
Create a `Student` class with properly type-hinted attributes and methods:
- Attributes: `name` (str), `student_id` (int), `grades` (list[float]), `email` (str | None)
- Method: `add_grade(grade: float) -> None` - adds a grade to the list
- Method: `get_average() -> float` - returns average grade or 0.0 if no grades
- Method: `get_info() -> str` - returns formatted student information

## Goal 2: Create Classroom Class with Type Hints
Create a `Classroom` class with type-hinted collections:
- Attribute: `students` (list[Student]) - stores Student objects
- Attribute: `course_name` (str)
- Method: `add_student(student: Student) -> None` - adds a student
- Method: `get_top_students(count: int) -> list[Student]` - returns top N students by average
- Method: `find_student(student_id: int) -> Student | None` - finds student by ID or returns None
- Method: `get_class_average() -> float` - returns average of all students' averages

## Goal 3: Create Helper Functions with Type Hints
Create standalone functions with proper type annotations:
- `create_student_from_dict(data: dict[str, str | int]) -> Student` - creates Student from dictionary
- `generate_report(classroom: Classroom) -> dict[str, float | int]` - returns report with total_students, class_average, highest_average

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Student: Alice (ID: 1001)
Email: alice@school.com
Grades: [85.5, 92.0, 88.5]
Average: 88.67

Classroom: Python 101
Total Students: 3
Class Average: 87.33
Top Student: Bob with 90.50 average

Report:
{'total_students': 3, 'class_average': 87.33, 'highest_average': 90.5}
```
