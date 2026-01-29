# Complete your task here (refer to task.md)

# Goal 1: Ask for favorite food
user_input = input('What is your favorite food?')
# Goal 2: Open food.txt and write answer to file
with open('food.txt', 'w') as f:
    f.write(user_input)
# Goal 3: Check file exists (manual)
with open('food.txt', 'r') as f:
    content = f.read()
    print(content)