# Drills - Unit 18: File Reading
# ------------------------------

# Drill 1: (Assume hello.txt exists) Open "hello.txt" with `with open("hello.txt", "r") as f:`, read content with f.read(), and print it
with open('hello.txt', 'r') as f:
    content = f.read()
    print(content) 
# Drill 2: Write a try block that tries to open a non-existent file, and an except block that prints "File not found"
try:
    with open('test.txt', 'r') as f:
        content = f.read()
        print(content)
except:
    print('Check the file path or the working directory')