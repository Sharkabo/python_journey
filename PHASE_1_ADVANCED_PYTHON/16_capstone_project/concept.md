# Unit 16: Capstone Project - Task Management API

## Project Overview

This capstone project synthesizes all concepts from Phase 1 by building a complete Task Management System. You'll apply OOP, type hints, decorators, data structures, and algorithms to create a production-ready application.

**What You'll Build:**
A command-line task management system with advanced features including task prioritization, categorization, and deadline management.

---

## Learning Objectives

By completing this project, you will demonstrate mastery of:
- Object-Oriented Programming (inheritance, encapsulation, polymorphism)
- Type hints for robust code
- Decorators for logging and validation
- Context managers for file operations
- Data structures for efficient task organization
- Algorithms for sorting and searching tasks
- Exception handling for robust error management

---

## Project Requirements

### Core Features

**1. Task Management:**
- Create, update, delete, and list tasks
- Each task has: title, description, priority, category, deadline, status
- Support task status: TODO, IN_PROGRESS, COMPLETED
- Support priority levels: LOW, MEDIUM, HIGH

**2. Categories:**
- Organize tasks into categories (Work, Personal, Shopping, etc.)
- Filter tasks by category
- Count tasks per category

**3. Sorting and Filtering:**
- Sort tasks by priority, deadline, or creation date
- Filter by status, category, or priority
- Search tasks by keyword in title/description

**4. Persistence:**
- Save tasks to JSON file
- Load tasks from JSON file
- Auto-save on changes

**5. User Interface:**
- Interactive menu system
- Clear, formatted output
- Input validation

---

## Technical Requirements

**Must Use These Concepts:**

**1. OOP (Units 01-04):**
```python
# Base class for entities
class BaseEntity:
    # Encapsulation with properties
    # Abstract methods for subclasses

# Task class inheriting from BaseEntity
class Task(BaseEntity):
    # Proper use of __init__, __str__, __repr__
    # Properties with validation
    # Type hints on all methods

# Manager classes for business logic
class TaskManager:
    # Use composition and dependency injection
```

**2. Type Hints (Unit 05):**
```python
# All functions and methods must have type hints
from typing import Optional, List, Dict
from datetime import datetime

def create_task(
    title: str,
    description: str,
    priority: str,
    category: str,
    deadline: Optional[datetime] = None
) -> Task:
    pass
```

**3. Decorators (Unit 07):**
```python
# Create decorators for:
@log_operation  # Log method calls
@validate_input  # Validate parameters
@timing  # Measure performance
```

**4. Context Managers (Unit 10):**
```python
# Use for file operations
with FileManager('tasks.json', 'r') as file:
    data = file.read()
```

**5. Data Structures (Units 13-14):**
```python
# Organize tasks efficiently
# Use appropriate data structures for fast lookup
# Consider using priority queue for task prioritization
```

**6. Algorithms (Unit 15):**
```python
# Implement custom sorting
# Efficient search algorithms
# Optimize for O(n log n) or better when possible
```

---

## Suggested Architecture

```
capstone_project/
├── models/
│   ├── __init__.py
│   ├── base.py          # BaseEntity class
│   ├── task.py          # Task class
│   └── enums.py         # Status, Priority enums
├── managers/
│   ├── __init__.py
│   ├── task_manager.py  # Business logic
│   └── file_manager.py  # Persistence
├── utils/
│   ├── __init__.py
│   ├── decorators.py    # Custom decorators
│   ├── validators.py    # Input validation
│   └── formatters.py    # Output formatting
├── main.py              # Entry point with menu
└── tasks.json           # Data file
```

---

## Implementation Guidelines

**Phase 1: Core Models (30%):**
1. Create `BaseEntity` with common properties (id, created_at, updated_at)
2. Create `Task` class with all required fields
3. Create enums for Status and Priority
4. Add data validation using properties

**Phase 2: Manager Classes (30%):**
1. Implement `TaskManager` with CRUD operations
2. Implement file persistence with context managers
3. Add decorators for logging and validation
4. Handle exceptions gracefully

**Phase 3: Algorithms and Search (20%):**
1. Implement task sorting (by priority, deadline, etc.)
2. Implement task filtering
3. Implement keyword search
4. Optimize for performance

**Phase 4: User Interface (20%):**
1. Create interactive menu
2. Implement all menu options
3. Add input validation
4. Format output beautifully

---

## Evaluation Criteria

**Code Quality (40%):**
- Proper use of OOP principles
- Type hints on all functions/methods
- Clean, readable code with good naming
- Proper error handling

**Feature Completeness (30%):**
- All core features implemented
- Features work correctly
- Edge cases handled

**Technical Concepts (20%):**
- Decorators used appropriately
- Context managers for file ops
- Efficient algorithms
- Appropriate data structures

**User Experience (10%):**
- Clear instructions
- Intuitive menu system
- Helpful error messages
- Well-formatted output

---

## Bonus Challenges

If you finish early, try these advanced features:
- Task dependencies (task B depends on task A)
- Recurring tasks
- Task tags/labels
- Export to CSV
- Statistics dashboard
- Undo/redo functionality
- Multi-user support with authentication

---

## Getting Started

1. Create the project structure
2. Start with the models (Task, BaseEntity)
3. Implement basic CRUD in TaskManager
4. Add file persistence
5. Build the menu system
6. Implement advanced features
7. Test thoroughly
8. Refactor and optimize

---

## Spiral Learning Note

**This Project Integrates:**
- Unit 01-04: OOP fundamentals and design patterns
- Unit 05: Type hints for robust code
- Unit 07: Decorators for cross-cutting concerns
- Unit 10: Context managers for resource management
- Unit 11-12: Abstract classes and exception handling
- Unit 13-14: Data structures for efficiency
- Unit 15: Algorithms for sorting and searching

**Preparation for Phase 2:**
- This foundation prepares you for FastAPI
- Similar architecture to real web APIs
- TypeHints essential for FastAPI automatic features
- Understanding data flow and validation crucial

**Real-World Skills:**
- Project structure like production applications
- Design patterns used in industry
- Performance optimization techniques
- Code organization and modularity
- This is portfolio-worthy work that demonstrates professional-level Python skills
