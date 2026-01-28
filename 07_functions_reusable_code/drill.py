# Drills - Unit 07: Functions
# ---------------------------

# Drill 1: Define a function named 'say_hi' that prints "Hi!"
def say_hi():
    print('Hi!')

# Drill 2: Call the function 'say_hi'
say_hi()

# Drill 3: Define a function named 'greet' that takes a parameter 'name', prints "Hello " + name, then call greet("Ian")
def greet(name):
    print(f'Hello {name}')

name = input('Please input your name')
greet(name)

# Drill 4: Define a function 'add_five' that takes a number, adds 5, and prints result. Call it with 10.
def add_five(number):
    result = number + 5
    print(result)

add_five(10)
