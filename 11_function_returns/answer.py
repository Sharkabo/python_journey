# Complete your task here (refer to task.md)

# 1. Create Math Functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b 

# 2. Get User Input
a = int(input('Please input first number:'))
b = int(input('Please input second number:'))
# 3. Perform Calculations
sum = add(a, b)
difference = subtract(a, b)
product = multiply(a, b)
quotient = divide(a, b)

print(f'{a} + {b} = {sum}\n{a} - {b} = {difference}\n{a} * {b} = {product}\n{a} / {b} = {quotient}')
