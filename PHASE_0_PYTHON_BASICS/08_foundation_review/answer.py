# Complete your task here (refer to task.md)

# Goal 1: Define secret number
def start_game():
    secret_num = 7

# Goal 2: Loop 3 times to ask for guess and check match
    def validate(num):
        if num == secret_num:
            print('You Won!')
        else:
            print('Wrong!')

    guesses = []

    for i in range(3):
        input_num = int(input('Please try to guess a number...'))
        validate(input_num)
        guesses.append(input_num)

# Goal 3 (Bonus): Track guesses in a list
    print(guesses)

# Goal 4 (Bonus): Wrap in start_game function
start_game()