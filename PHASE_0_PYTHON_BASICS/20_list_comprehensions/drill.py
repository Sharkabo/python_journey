# Drills - Unit 20: List Comprehensions
# ---------------------------------------

# Drill 1: Create a list of squares from 1 to 5 using list comprehension: [1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print(squares)
# Drill 2: Create a list of numbers from 0 to 9, but only include even numbers using list comprehension
nums = []
for i in range(10):
    if i % 2 == 0:
        nums.append(i)
print(nums)

# Drill 3: Given names = ["alice", "bob", "charlie"], create a new list with all names in uppercase
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
# Drill 4: Given numbers = [1, 2, 3, 4, 5, 6], create a list of numbers greater than 3
numbers = [1, 2, 3, 4, 5, 6]
big_num = [num for num in numbers if num > 3]
print(big_num)
# Drill 5: Create a list of the lengths of words in ["cat", "dog", "elephant"] using list comprehension
animals = ["cat", "dog", "elephant"]
len_animals = [len(name) for name in animals]
print(len_animals)