# Drills - Unit 12: Loop Control
# --------------------------------

# Drill 1: Write a for loop from 0 to 9, but break when i equals 7
for i in range(10):
    print(i)
    if i == 7:
        break

# Drill 2: Write a for loop from 0 to 5, but continue (skip) when i equals 3
for i in range(7):
    if i == 3:
        continue
    print(i)
# Drill 3: Create a while True loop that asks for input and breaks if input is "stop"
while True:
    answer = input('Enter Stop to exit the loop')
    if answer == 'Stop':
        break

# Drill 4: Loop through [10, 15, 20, 25, 30] and skip printing numbers less than 20 using continue
collection = [10, 15, 20, 25, 30]
for i in collection:
    if i < 20:
        continue
    print(i)
# Drill 5: Loop through range(10) and only print even numbers (use continue to skip odd numbers)
for i in range(10):
    if i % 2 == 0:
        if i == 0:
            continue
        else:
            print(i)
    else: 
        continue
