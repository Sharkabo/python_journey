# Unit 03b: The @property Decorator

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python @property decorator"
- "Python getter setter"
- "Python property 裝飾器"

---

## 1. The @property Decorator

The `@property` decorator allows you to define methods that can be accessed like attributes. This gives you control over how attributes are accessed and modified while keeping a clean syntax.

**Why use @property?**
- Add validation when setting values
- Compute values on the fly
- Maintain backward compatibility when changing implementation
- Make read-only attributes
- Keep the clean attribute access syntax

**Basic Syntax:**
```python
class ClassName:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        """Getter method"""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Setter method"""
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value
```

**Example:**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit (computed)"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self._celsius = (value - 32) * 5/9

# Using the class
temp = Temperature(25)
print(temp.celsius)      # 25 (calls the getter)
print(temp.fahrenheit)   # 77.0 (computed from celsius)

temp.celsius = 30        # Calls the setter with validation
print(temp.celsius)      # 30
print(temp.fahrenheit)   # 86.0

temp.fahrenheit = 32     # Set using Fahrenheit
print(temp.celsius)      # 0.0 (automatically converted)

# temp.celsius = -300    # ValueError: Temperature below absolute zero!
```

---

## 2. Getter and Setter Methods (Old vs New Style)

Before `@property` was available, Python used explicit getter and setter methods. Understanding this helps you appreciate `@property` and recognize it in older code.

**Old Style (Explicit Methods):**
```python
class OldStylePerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0 or age > 150:
            raise ValueError("Invalid age")
        self._age = age

# Usage
person = OldStylePerson("Alice", 30)
print(person.get_name())  # Alice
person.set_age(31)
print(person.get_age())   # 31
```

**New Style (Using @property):**
```python
class ModernPerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value

# Usage (cleaner syntax)
person = ModernPerson("Alice", 30)
print(person.name)  # Alice (looks like attribute access)
person.age = 31     # Looks like assignment, but calls setter
print(person.age)   # 31
```

---

## 3. Practical Example: Rectangle Class

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        """Computed property - no setter needed"""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Another computed property"""
        return 2 * (self._width + self._height)

# Using the Rectangle class
rect = Rectangle(5, 10)
print(rect.width)      # 5
print(rect.height)     # 10
print(rect.area)       # 50 (computed on the fly)
print(rect.perimeter)  # 30 (computed on the fly)

rect.width = 7
print(rect.area)       # 70 (automatically updated)

# rect.area = 100      # AttributeError: can't set attribute
# rect.width = -5      # ValueError: Width must be positive
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 03a: You learned encapsulation with public/protected/private attributes
- Unit 03b: Now you're using `@property` for elegant, controlled access
- Properties provide the benefits of encapsulation without ugly `get_` and `set_` methods

**Preparation for Next Lesson:**
- Unit 03c: You'll learn about read-only properties and inheritance patterns
- Unit 04: Magic Methods (properties use `__get__` and `__set__` behind the scenes)

**Real-World Application:**
- Pydantic models (used in FastAPI) heavily use properties
- Database ORMs use properties to sync with database fields
- Properties let you add validation without changing how code looks
- Essential for building maintainable APIs
