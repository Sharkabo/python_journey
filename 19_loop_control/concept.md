# Unit 19: Loop Control (Break & Continue)

## 1. Break - Stop the Loop
The `break` statement immediately exits a loop, even if the loop condition is still true.

**Example:**
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Prints: 0, 1, 2, 3, 4 (stops at 5)
```

**Real Use Case:**
```python
while True:
    answer = input("Type 'exit' to quit: ")
    if answer == "exit":
        break
    print("You typed:", answer)
```

---

## 2. Continue - Skip to Next Iteration
The `continue` statement skips the rest of the current iteration and moves to the next one.

**Example:**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
# Prints: 0, 1, 3, 4 (skips 2)
```

**Real Use Case:**
```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:  # If even
        continue
    print(num)  # Only prints odd numbers: 1, 3, 5
```

---

## Spiral Learning Note
We learned loops in Units 06 and 10. Now we can control them more precisely! `break` and `continue` are essential for handling user input and filtering data.
