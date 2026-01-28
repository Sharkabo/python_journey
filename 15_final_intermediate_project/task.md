# Task Description

Build a "Tiny Journal" app.

## Goal 1
Open `journal.txt` in Append mode (`"a"`).

## Goal 2
Start a `while True` loop. Within the loop:
1. Ask input: "Write entry (or type 'exit' to quit): ".
2. Check if they typed "exit". If yes, use `break` to stop the loop.
3. If not exit, write the entry + a newline (`\n`) to the file.
*Important: Don't forget `f.write(entry + "\n")` so lines don't get stuck together!*

---
**Expected Output:**
```text
Write entry: Today I learned Python.
Write entry: It was fun.
Write entry: exit
```
*(Check journal.txt to see your two lines saved)*
