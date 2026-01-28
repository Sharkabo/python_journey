# Complete your task here (refer to task.md)

# 1. Clean User Input
source_name = input('Please input username...')
name = source_name.strip().replace(' ','').title()
# 2. Create a Username
username = name.lower().replace(' ',"_")

# 3. Display Result
print(f'Welcome, {name}! Your username is: {username}')
