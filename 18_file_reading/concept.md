# Unit 18: File Reading

## 1. Opening a File
We can read text files (like `.txt`).
We use `with open(...)` because it automatically closes the file for us (safe!).

**Syntax:**
```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```
*Note: `"r"` means Read mode.*

## 2. Where is the file?
The file must exist in the same folder, or your program will crash (unless you use Try/Except from Unit 12!).

---

## Spiral Learning Note
Variables (Unit 01) disappear when the program ends. Files allow data to survive!
