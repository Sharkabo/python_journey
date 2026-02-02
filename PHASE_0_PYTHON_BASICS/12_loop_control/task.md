# Task: Number Guesser with Limits

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Set Up the Game
Create a secret number (e.g., 42) and a maximum of 5 attempts.

## Goal 2: Create the Game Loop
Use a for loop with `range(5)` to give the user 5 chances.
- Ask the user to guess the number
- If they guess correctly, print "Correct! You win!" and **break** out of the loop
- If they guess wrong, print "Wrong! Try again."

## Goal 3: Handle Invalid Input
If the user types something that's not a number, use `continue` to skip that attempt and ask again (you'll need a try/except block from Unit 12).

## Goal 4: Game Over
After the loop, if they didn't guess correctly, print "Game Over! The number was [secret]"

---
**Expected Output:**
```text
Guess the number (1-100): 30
Wrong! Try again.
Guess the number (1-100): 42
Correct! You win!
```
