# Unit 11: Abstract Base Classes (ABC)

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python abstract base class"  
- "Python ABC tutorial"
- "Python interfaces"

Recommended Channels:
- Corey Schafer (Python)
- ArjanCodes (Software Design)
- mCoding (Advanced Python)

---

## 1. What are Abstract Base Classes?

An **Abstract Base Class (ABC)** is a class that cannot be instantiated and is designed to be subclassed. It defines a "contract" that subclasses must follow.

**Key Concepts:**
- **Abstract methods**: Methods declared but not implemented
- **Concrete methods**: Regular methods with implementation
- **Subclasses MUST implement** all abstract methods

**Why use ABCs?**
- Enforce consistent interfaces across classes
- Catch errors at class definition time (not runtime)
- Design better APIs and frameworks
- Document expected behavior

---

## 2. Creating Abstract Base Classes

**Import required:**
```python
from abc import ABC, abstractmethod
```

**Example:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Inherit from ABC
    
    @abstractmethod
    def make_sound(self):
        # No implementation - subclasses MUST implement this
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def breathe(self):
        # Concrete method - shared by all animals
        print("Inhale... Exhale...")

# This will raise TypeError - can't instantiate ABC
# animal = Animal()  # Error!

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
    def move(self):
        print("Running on four legs")

class Bird(Animal):
    def make_sound(self):
        print("Tweet!")
    
    def move(self):
        print("Flying in the sky")

# Now we can create instances
dog = Dog()
dog.make_sound()  # Woof!
dog.move()        # Running on four legs
dog.breathe()     # Inhale... Exhale...

bird = Bird()
bird.make_sound()  # Tweet!
bird.move()        # Flying in the sky
```

---

## 3. Enforcing Implementation

If a subclass doesn't implement all abstract methods, you get an error **when creating an instance**:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Forgot to implement perimeter
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    # Missing perimeter() implementation!

# This will raise TypeError
# rect = Rectangle(5, 10)  # Error: Can't instantiate abstract class

# Correct implementation
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return self.side * 4

# This works
square = Square(5)
print(square.area())       # 25
print(square.perimeter())  # 20
```

---

## 4. Abstract Properties

You can also make properties abstract:

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @property
    @abstractmethod
    def connection_string(self):
        pass
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class PostgresDB(Database):
    def __init__(self, host, port, dbname):
        self.host = host
        self.port = port
        self.dbname = dbname
    
    @property
    def connection_string(self):
        return f"postgresql://{self.host}:{self.port}/{self.dbname}"
    
    def connect(self):
        print(f"Connecting to {self.connection_string}")
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL")

db = PostgresDB("localhost", 5432, "myapp")
print(db.connection_string)  # postgresql://localhost:5432/myapp
db.connect()
```

---

## 5. Real-World Use Case: FastAPI-like Repository Pattern

ABCs are perfect for defining repository interfaces:

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class UserRepository(ABC):
    """Abstract base class for user data access"""
    
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[dict]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[dict]:
        pass
    
    @abstractmethod
    def create(self, user_data: dict) -> dict:
        pass
    
    @abstractmethod
    def update(self, user_id: int, user_data: dict) -> dict:
        pass
    
    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass

class PostgresUserRepository(UserRepository):
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_by_id(self, user_id: int) -> Optional[dict]:
        # PostgreSQL implementation
        return {"id": user_id, "name": "Alice", "email": "alice@example.com"}
    
    def get_all(self) -> List[dict]:
        # PostgreSQL implementation
        return [{"id": 1, "name": "Alice"}]
    
    def create(self, user_data: dict) -> dict:
        # PostgreSQL implementation
        return {**user_data, "id": 123}
    
    def update(self, user_id: int, user_data: dict) -> dict:
        # PostgreSQL implementation
        return {"id": user_id, **user_data}
    
    def delete(self, user_id: int) -> bool:
        # PostgreSQL implementation
        return True

class MongoUserRepository(UserRepository):
    # Different database, same interface!
    def __init__(self, mongo_client):
        self.client = mongo_client
    
    def get_by_id(self, user_id: int) -> Optional[dict]:
        # MongoDB implementation
        pass
    
    def get_all(self) -> List[dict]:
        # MongoDB implementation
        pass
    
    def create(self, user_data: dict) -> dict:
        # MongoDB implementation
        pass
    
    def update(self, user_id: int, user_data: dict) -> dict:
        # MongoDB implementation
        pass
    
    def delete(self, user_id: int) -> bool:
        # MongoDB implementation
        pass

# Now your application code doesn't care which database you use!
def get_user_service(repo: UserRepository):
    user = repo.get_by_id(1)
    return user

# Can swap implementations easily
postgres_repo = PostgresUserRepository(db_connection=None)
user = get_user_service(postgres_repo)
```

---

## 6. ABC vs Regular Inheritance

**Regular Inheritance:**
```python
class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    pass

c = Child()
c.method()  # Works - inherits parent's method
```

**ABC Inheritance:**
```python
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def method(self):
        pass

class Child(Parent):
    pass

# c = Child()  # Error! Must implement method()

class GoodChild(Parent):
    def method(self):
        print("Implementation")

c = GoodChild()  # Works!
```

---

## 7. When to Use ABCs

**Use ABCs when:**
- Building a framework or library
- Defining plugin systems
- Multiple implementations of same interface
- You want to catch missing methods early
- Documenting expected subclass behavior

**Don't use ABCs when:**
- Simple inheritance is enough
- You're not sure about the interface yet
- Over-engineering simple code

---

## Spiral Learning Note

**Connection to Previous Learning:**
- You know inheritance (Unit 02)
- You've seen why interfaces matter
- ABCs enforce "contracts" for subclasses

**Preparation for Next Lesson:**
- Unit 12 teaches Advanced Exception Handling
- ABCs often raise TypeError for missing implementations
- Understanding abstract classes helps with API design
