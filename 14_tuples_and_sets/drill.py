# Drills - Unit 14: Tuples & Sets
# ---------------------------------

# Drill 1: Create a tuple called point with values (5, 10) and print it
point = (5, 10)
print(point)
# Drill 2: Unpack the tuple: x, y = point, then print x and y separately
x, y = point
print(x)
print(y)
# Drill 3: Create a set called numbers with values {1, 2, 2, 3, 3, 3} and print it (notice duplicates removed)
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)
# Drill 4: Add the number 4 to the numbers set using .add(), then print the set
numbers.add(4)
print(numbers)
# Drill 5: Create two sets: a = {1, 2, 3} and b = {3, 4, 5}, then print their intersection using a & b
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)