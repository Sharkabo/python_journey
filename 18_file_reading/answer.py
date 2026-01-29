# Complete your task here (refer to task.md)

# Goal 1: Open hello.txt in read mode, read content, and print it
with open('hello.txt', 'r') as f:
    content = f.read()
    print(content)