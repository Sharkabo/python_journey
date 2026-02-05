# Unit 04: Magic Methods (Dunder Methods)

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python magic methods"
- "Python dunder methods"
- "Python __str__ __repr__"

---

## 1. What are Magic Methods?

Magic methods (also called **dunder methods** - double underscore) are special methods that Python calls automatically in certain situations. They allow you to customize how your objects behave with built-in Python operations.

**Common Pattern:**
- Start and end with double underscores: `__method__`
- You rarely call them directly
- Python calls them automatically

**Why are they useful?**
- Make your objects behave like built-in types
- Enable operator overloading
- Control object representation
- Essential for FastAPI response models

---

## 2. String Representation: `__str__` and `__repr__`

**`__str__`**: User-friendly string representation
**`__repr__`**: Developer-friendly, unambiguous representation

**Example:**
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        # For end users - readable
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        # For developers - reproducible
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

book = Book("Clean Code", "Robert Martin", 2008)
print(str(book))     # Clean Code by Robert Martin
print(repr(book))    # Book(title='Clean Code', author='Robert Martin', year=2008)
print(book)          # Calls __str__ automatically
```

---

## 3. Comparison: `__eq__`, `__lt__`, `__gt__`

These methods let you compare objects using `==`, `<`, `>`, etc.

**Example:**
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        # Define equality: two students are equal if they have same grade
        return self.grade == other.grade
    
    def __lt__(self, other):
        # Define less than: for sorting
        return self.grade < other.grade
    
    def __gt__(self, other):
        # Define greater than
        return self.grade > other.grade

alice = Student("Alice", 85)
bob = Student("Bob", 92)
charlie = Student("Charlie", 85)

print(alice == charlie)  # True (same grade)
print(alice == bob)      # False
print(bob > alice)       # True
print(sorted([bob, alice, charlie], key=lambda s: s.grade))  # Works because of __lt__
```

---

## 4. Container Emulation: `__len__`, `__getitem__`

Make your objects behave like lists or dictionaries.

**Example:**
```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        # Enable len() function
        return len(self.songs)
    
    def __getitem__(self, index):
        # Enable indexing: playlist[0]
        return self.songs[index]
    
    def __contains__(self, song):
        # Enable 'in' operator
        return song in self.songs

playlist = Playlist("My Favorites")
playlist.add_song("Imagine")
playlist.add_song("Bohemian Rhapsody")

print(len(playlist))           # 2
print(playlist[0])             # Imagine
print("Imagine" in playlist)   # True

# Can even iterate!
for song in playlist:
    print(song)
```

---

## 5. Arithmetic Operators: `__add__`, `__sub__`, `__mul__`

Customize how `+`, `-`, `*` work with your objects.

**Example:**
```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)
    
    def __str__(self):
        return f"{self.amount} {self.currency}"

price1 = Money(100, "USD")
price2 = Money(50, "USD")

total = price1 + price2
print(total)  # 150 USD

difference = price1 - price2
print(difference)  # 50 USD
```

---

## 6. Common Magic Methods Reference

| Method | Operator/Function | Purpose |
|--------|------------------|---------|
| `__str__` | `str()`, `print()` | User-friendly string |
| `__repr__` | `repr()` | Developer string |
| `__len__` | `len()` | Length of object |
| `__getitem__` | `obj[key]` | Indexing |
| `__setitem__` | `obj[key] = val` | Assignment |
| `__contains__` | `in` | Membership test |
| `__eq__` | `==` | Equality |
| `__lt__` | `<` | Less than |
| `__gt__` | `>` | Greater than |
| `__add__` | `+` | Addition |
| `__sub__` | `-` | Subtraction |
| `__call__` | `obj()` | Call as function |

---

## Spiral Learning Note

**Connection to Previous Learning:**
- You learned about classes and `__init__` in Unit 01
- Magic methods extend that concept for customization
- They make your objects feel "Pythonic"

**Preparation for Next Lesson:**
- Unit 05 will teach `*args` and `**kwargs`
- Magic methods often use `**kwargs` for flexibility
- Understanding these basics helps you read FastAPI source code
