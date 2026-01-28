# Unit 09: String Methods & Formatting

## 1. Common String Methods
Strings (text) have built-in "tools" called **methods** that help us manipulate them.

**Common Methods:**
```python
text = "  Hello World  "
print(text.upper())      # "  HELLO WORLD  "
print(text.lower())      # "  hello world  "
print(text.strip())      # "Hello World" (removes spaces)
print(text.replace("World", "Python"))  # "  Hello Python  "
```

**Splitting & Joining:**
```python
sentence = "Apple,Banana,Cherry"
fruits = sentence.split(",")  # Creates a list: ["Apple", "Banana", "Cherry"]

words = ["I", "love", "Python"]
sentence = " ".join(words)    # "I love Python"
```

---

## 2. F-Strings (Modern Formatting)
F-strings let us insert variables directly into text using `f""` and `{}`.

**Syntax:**
```python
name = "Ian"
age = 20
print(f"My name is {name} and I am {age} years old")
```

**Example with Math:**
```python
price = 100
tax = 0.1
print(f"Total: ${price * (1 + tax)}")  # "Total: $110.0"
```

---

## Spiral Learning Note
We learned about strings in Unit 01, but now we can manipulate them! This is crucial for processing user input (Unit 03) and working with files (Units 13-14).
