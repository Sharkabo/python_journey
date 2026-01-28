# Task Description: Number Guessing Game

Build a simple "Guess the Number" game.

## Goal 1
Define a secret number variable (e.g., `secret_number = 7`).

## Goal 2
Use a loop (you can use `for i in range(3)` to give them 3 tries). Inside the loop:
1. Ask the user to "Guess a number:".
2. Convert it to an integer.
3. Check if it matches `secret_number`.
   - If yes: Print "You Won!" and calculate score (maybe?). **IMPORTANT**: Since we haven't learned `break` yet, just print "You Won!"
   - If no: Print "Wrong!".

## Goal 3 (Spiral Bonus)
Create an empty list called `guesses` before the loop.
Every time the user guesses, `append` their number to the list.
After the game ends, print: "Your guesses were: [list]"

## Goal 4 (Spiral Bonus)
Wrap all your code inside a function called `start_game()`, and then call it at the bottom.

---
**Expected Output (Example):**
```text
Guess a number: 2
Wrong!
Guess a number: 7
You Won!
Your guesses were: [2, 7]
```
