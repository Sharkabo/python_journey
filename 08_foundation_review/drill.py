# Drills - Unit 08: Foundation Review
# -------------------------------------

# Drill 1: Create a loop that runs 3 times
for i in range(3):
    print('Test')

# Drill 2: Ask for input "Guess:" and convert to int (write it just once, not in a loop)
guess_num = int(input('Please guess a number...'))

# Drill 3: Create a variable secret = 7. Write an if statement to check if guess == secret
secret = 7
if guess_num == secret:
    print('You got it!!')
else:
    print('Good luck with next time.')
# Drill 4: Create an empty list called user_guesses, then use .append() to add the numbers 5 and 10 to it
user_guesses = []
user_guesses.append(5)
user_guesses.append(10)

# Drill 5: Print "Game Over" followed by the user_guesses list
print(f'Game Over {user_guesses}')