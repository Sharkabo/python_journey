# Capstone Project: Task Management System

## Project Goal

Build a complete task management system that demonstrates all Phase 1 concepts. This is a significant project that will take time to complete properly.

---

## Minimum Requirements

### 1. Task Model
Create a `Task` class with:
- Properties: id, title, description, priority (LOW/MEDIUM/HIGH), status (TODO/IN_PROGRESS/COMPLETED), category, created_at, deadline
- Type hints on all methods and properties
- Validation using property setters
- `__str__` and `__repr__` methods

### 2. TaskManager Class
Create a `TaskManager` class that:
- Stores tasks in an appropriate data structure
- Implements CRUD operations (Create, Read, Update, Delete)
- Has methods to filter and sort tasks
- Uses decorators for logging operations
- Includes proper error handling

### 3. File Persistence
- Save tasks to `tasks.json`
- Load tasks from `tasks.json`
- Use context managers for file operations
- Handle file not found and JSON errors

### 4. User Interface
Create an interactive menu with options for:
- Add new task
- List all tasks
- Filter tasks (by status, priority, category)
- Sort tasks (by priority, deadline)
- Mark task as complete
- Delete task
- Search tasks by keyword
- Save and exit

### 5. Advanced Features
- At least one custom decorator (logging, validation, or timing)
- Proper use of type hints throughout
- Exception handling for all user inputs
- Sorted output using efficient algorithms

---

## Project Structure

Create your project in the `answer/` directory with this structure:

```
answer/
├── models.py         # Task class and enums
├── manager.py        # TaskManager class
├── decorators.py     # Custom decorators
├── utils.py          # Helper functions
├── main.py           # Entry point with menu
└── tasks.json        # Data file (created automatically)
```

---

## Getting Started

1. Create the `answer/` directory
2. Start with `models.py` - create Task class and enums
3. Build `manager.py` - implement TaskManager
4. Create `decorators.py` - implement at least one decorator
5. Build `main.py` - create the menu system
6. Test thoroughly with various scenarios

---

## Expected Functionality

When you run `python main.py`, the user should see:

```text
=== Task Management System ===

1. Add new task
2. List all tasks
3. Filter tasks
4. Sort tasks
5. Mark task complete
6. Delete task
7. Search tasks
8. Save and exit

Choose an option: 1

Enter task title: Complete Python Phase 1
Enter description: Finish all 16 units
Priority (LOW/MEDIUM/HIGH): HIGH
Category: Learning
Deadline (YYYY-MM-DD) or press Enter: 2026-02-15

Task created successfully!

Choose an option: 2

=== All Tasks ===
[1] Complete Python Phase 1 - HIGH - TODO
    Learning | Deadline: 2026-02-15
    Finish all 16 units
```

---

## Evaluation Checklist

Use this to verify your project is complete:

**Core Features:**
- [ ] Task creation with all required fields
- [ ] List all tasks with formatted output
- [ ] Filter by status, priority, and category
- [ ] Sort by priority and deadline
- [ ] Mark tasks as complete
- [ ] Delete tasks
- [ ] Search by keyword
- [ ] Save/load from JSON file

**Technical Requirements:**
- [ ] Type hints on all functions and methods
- [ ] At least one custom decorator used
- [ ] Context managers for file operations
- [ ] Proper exception handling
- [ ] OOP principles (inheritance, encapsulation)
- [ ] Efficient sorting algorithm
- [ ] Input validation

**Code Quality:**
- [ ] Clean, readable code
- [ ] Good variable and function names
- [ ] Proper code organization
- [ ] Comments for complex logic
- [ ] No code duplication

---

## Tips

- Start small, build incrementally
- Test each feature before moving to the next
- Use type hints from the beginning
- Handle edge cases (empty list, invalid input, file errors)
- Make the UI clear and user-friendly
- Commit your code frequently (if using git)

---

This is your chance to showcase everything you've learned in Phase 1. Take your time and build something you're proud of!
