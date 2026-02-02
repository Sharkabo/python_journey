# Drills - Unit 11: Function Return Values
# -----------------------------------------

# Drill 1: Define a function 'double' that takes a number and returns number * 2
def double(number):
    result = number * 2
    return result
# Drill 2: Call double(7) and store the result in a variable called result, then print result
result = double(7)
print(result)
# Drill 3: Define a function 'greet_user' that takes a name and returns "Hello " + name
def greet_user(name):
    return (f"\"Hello\" {name}")

# Drill 4: Call greet_user("Ian") and print the returned value directly
greeting_line = greet_user('Ian')
print(greeting_line)
# Drill 5: Define a function 'is_adult' that takes age, returns True if age >= 18, else returns False
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

user_age = int(input("Please input your age:"))
print(is_adult(user_age))