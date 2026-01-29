# Complete your task here (refer to task.md)

# 1. Store Visitor Data
visitors = set()

# 2. Collect Visitor Names
while True:
    user_input = input("Enter visitor name (or 'done' to finish):")
    if user_input == 'done':
        break
    else:
        visitors.add(user_input)
        print(f"Current visitors: {visitors}")

# 3. Display Results
print(len(visitors))
print(f'Visitors:{visitors}')
# 4. Check Specific Visitor
lookup_name = input('Check if someone visited:')

if lookup_name in visitors:
    print(f'{lookup_name} visited today!')
else:
    print(f'Sorry, {lookup_name} didn\'t show up')