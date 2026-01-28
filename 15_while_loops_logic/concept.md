# Unit 15: While Loops

## 1. The While Loop
`for` loops (Unit 06) run a set number of times.
`while` loops run **as long as** a condition is True.

**Syntax:**
```python
count = 0
while count < 3:
    print("Run")
    count = count + 1
```

## 2. Infinite Loops (Warning!)
If the condition NEVER becomes False, the loop runs forever (until you crash).
Always ensure something changes inside the loop!

---

## Spiral Learning Note
This is perfect for "Game Loops" (like Unit 08) where we don't know how many guesses the user needs. Use `while` instead of `for` for uncertain repetitions.
