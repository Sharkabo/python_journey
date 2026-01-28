# Unit 19: File Writing

## 1. Writing to a File
To save data, we use Write mode (`"w"`).
**WARNING:** `"w"` overwrites the whole file!

**Syntax:**
```python
with open("output.txt", "w") as f:
    f.write("This is saved forever.")
```

## 2. Appending
If you want to add to the end without deleting, use Append mode (`"a"`).

---

## Spiral Learning Note
Now we can save our "ToDo List" (Unit 05) or "Game High Score" (Unit 08) so it is still there tomorrow.
