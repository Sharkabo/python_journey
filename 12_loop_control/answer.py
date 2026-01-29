# Complete your task here (refer to task.md)

# 1. Set Up the Game
secret_num = 42
flag = False
# 2. Create the Game Loop
# 3. Handle Invalid Input
for i in range(5):
    user_input = (input('Please try to guess the secret number:'))
    try:
        answer = int(user_input)
    except ValueError:
        print('Try again, your answer doesn\'t meet the requirements...')
        continue
    
    if answer == secret_num:
        print('Correct! You win!')
        flag = True
        break
    else:
        print('Wrong! Try again.')
# 4. Game Over
if flag == False:
    print(f'Game Over! The number was {secret_num}')
