# Drills - Unit 17: Try/Except
# ----------------------------

# Drill 1: Write a try/except to catch a conversion error
#   - In the try: attempt to convert text to a number with int("Hello") - this will fail!
#   - In the except ValueError: print "Cannot convert text to number"
try:
    int('Hello')
except ValueError:
    print('Cannot convert text to number')

# Drill 2: Write a try/except to catch a division by zero error
#   - In the try: attempt 10 / 0 - this will cause an error!
#   - In the except ZeroDivisionError: print "Cannot divide by zero"
try:
    num = 10 / 0
    print(num)
except:
    print('Cannot divide by zero')
# Drill 3: Write a try/except that catches ANY type of error
#   - In the try: write code that causes an error (int("abc") or 1/0 or anything that breaks)
#   - In the except Exception: print "Oops, something went wrong!"
try:
    int("abc")
except:
    print('Oops, something went wrong!')