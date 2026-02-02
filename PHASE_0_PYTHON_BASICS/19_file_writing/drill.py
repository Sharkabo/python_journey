# Drills - Unit 19: File Writing
# ------------------------------

# Drill 1: Open "log.txt" in write mode with `with open("log.txt", "w") as f:` and write "Log Entry 1" using f.write()
with open('log.txt', 'w') as f:
    f.write('You did modify the file.')
    
with open('log.txt', 'r') as f:
    content = f.read()
    print(content)

# Drill 2: Open "log.txt" in append mode with `with open("log.txt", "a") as f:` and write "Log Entry 2" to see it add to the end
with open('log.txt', 'a') as f:
    f.write('Log Entry 2')

with open('log.txt', 'r') as f:
    content = f.read()
    print(content)