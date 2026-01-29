# Complete your task here (refer to task.md)

# 1. Get User Information
user_age = int(input('Please input your age...'))
membership_ans = input('Do you have a membership card? (yes/no):').strip().lower()
if membership_ans == 'yes':
    have_membership = True
elif membership_ans == 'no':
    have_membership = False
else:
    print('Your answer doesn\'t meet the requirements. Try again...')
# 2. Check Access Rules
if user_age >= 18 and have_membership == True:
    print('Access Granted! Welcome!')
elif user_age >= 65 and have_membership == False:
    print('Senior citizens get free entry')
else:
    print('Access Denied. Requirements not met')
# 3. Display Result

