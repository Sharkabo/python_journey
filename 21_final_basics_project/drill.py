# Drills - Unit 21: Final Basics Review
# ---------------------------------------

# Drill 1: Create a dictionary called 'person' with keys "name": "Ian" and "age": 20
person = {'name': 'Ian', 'age': 20}

# Drill 2: Open "notes.txt" in append mode with `with open("notes.txt", "a") as f:` and write "Hello World\n" to it
with open('notes.txt', 'a') as f:
    f.write('Hello World\n')
with open('notes.txt', 'r') as f:
    content = f.read()
    print(content)
# Drill 3: Create a while loop that asks for input and breaks if the user types "exit"
while True:
    user_input = input('Exit the loop with the word: exit')
    if user_input == 'exit':
        break
