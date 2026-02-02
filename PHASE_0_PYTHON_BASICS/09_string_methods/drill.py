# Drills - Unit 09: String Methods
# ----------------------------------

# Drill 1: Create a variable text = "  python is fun  " and print text.strip()
text = " python is fun "
print(text.strip())
# Drill 2: Print text.upper() and text.lower()
print(text.upper())
print(text.lower())
# Drill 3: Create sentence = "I,love,coding" and split it by comma, store in a list called words
sentence = "I,love,coding"
words = sentence.split(',')
# Drill 4: Create a list items = ["apple", "banana"] and join them with " and " between them, then print
items = ["apple", "banana"]
glue = ' and '
items_line = glue.join(items)
print(items_line)
# Drill 5: Create variables name = "Ian" and score = 95, then use an f-string to print "Ian scored 95 points"
name = 'Ian'
score = 95
print(f'{name} scored {score}')
