# Unit 01: Classes and Objects (OOP Basics)

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python OOP tutorial"
- "Python classes and objects"
- "Python __init__ method"

Recommended Channels:
- Corey Schafer (Python)
- Tech With Tim (Python)
- freeCodeCamp.org

---

## 1. What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm that organizes data and the methods that operate on that data together into "objects".

**Core Concepts:**
- **Class**: A blueprint or template for objects
- **Object**: An instance created from a class
- **Attribute**: Data stored in an object
- **Method**: Functions that belong to an object

**Why do we need OOP?**
- Organizes code more clearly
- Reuses code efficiently
- Easier to maintain and extend

---

## 2. Creating a Class

**Syntax:**
```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
    
    def method_name(self):
        # Method content
        pass
```

**Explanation:**
- `class`: Keyword to define a class
- `__init__`: Constructor, automatically executes when creating an object
- `self`: Reference to the object itself
- `self.attribute`: Object's attribute

**Example:**
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

# Create objects (instantiation)
book1 = Book("Python Basics", "John Smith", 200)
book2 = Book("FastAPI Guide", "Jane Doe", 350)

# Use objects
print(book1.title)           # Python Basics
print(book1.get_info())      # Python Basics by John Smith, 200 pages
print(book2.get_info())      # FastAPI Guide by Jane Doe, 350 pages
```

---

## 3. Understanding `self`

`self` is one of the most important concepts in Python OOP.

**What `self` does:**
- Represents the object instance itself
- Allows methods to access the object's attributes
- Must be the first parameter of methods (but you don't pass it when calling)

**Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # self.name is the object's attribute
        self.age = age
    
    def introduce(self):
        # self lets us access the object's name and age
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

# Create two different people
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.introduce()  # Hi, I'm Alice and I'm 25 years old
person2.introduce()  # Hi, I'm Bob and I'm 30 years old

# self lets each object have its own data
print(person1.name)  # Alice
print(person2.name)  # Bob
```

---

## 4. Instance Variables vs Class Variables

**Instance Variables:**
- Each object has its own copy
- Defined using `self.variable`
- Different objects can have different values

**Class Variables:**
- All objects share the same value
- Defined directly in the class
- Used for shared data

**Example:**
```python
class Student:
    # Class variable (shared by all students)
    school_name = "Python Academy"
    total_students = 0
    
    def __init__(self, name, grade):
        # Instance variables (each student's own)
        self.name = name
        self.grade = grade
        Student.total_students += 1  # Update class variable

# Create students
student1 = Student("Alice", 85)
student2 = Student("Bob", 92)

# Instance variables are independent
print(student1.name)    # Alice
print(student2.name)    # Bob

# Class variables are shared
print(student1.school_name)     # Python Academy
print(student2.school_name)     # Python Academy
print(Student.total_students)   # 2
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- You already know how to use functions to encapsulate code (Unit 07)
- You already know how to use dictionaries to store related data (Unit 13)
- OOP combines these two concepts: data + functions = objects

**Preparation for Next Lesson:**
- Next you'll learn about Inheritance, which allows classes to be reused
- Understanding `self` and `__init__` is the foundation for learning inheritance
