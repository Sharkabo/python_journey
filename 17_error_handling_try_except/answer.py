# Complete your task here (refer to task.md)

# Goal 1: Try block with input and doubling, Except block for ValueError with error message
try:
    user_input = int(input('Enter number:'))
    output = user_input * 2
    print(output)
except:
    print('Please enter digits only.')