# Complete your task here (refer to task.md)

# Goal 1: Open journal.txt in append mode
with open('journal.txt', 'a') as f:
    while True:
        user_input = input("Write entry (or type 'exit' to quit): ")
        if user_input == 'exit':
            break
        else:
            f.write(user_input + "\n")

# Goal 2: Start loop, ask for input, check exit, and write to file
