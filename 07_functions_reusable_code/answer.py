# Complete your task here (refer to task.md)

# Goal 1: Define check_password function with if/else logic
def check_password(input_pass):
    password = 'secret123'
    if input_pass == password:
        print('Access Granted')
    else:
        print('Access Denied')

# Goal 2: Call function twice to test
input_wrong = input('Please input the password, test 1')
check_password(input_wrong)

input_right = input('Please input the password, test 2')
check_password(input_right)