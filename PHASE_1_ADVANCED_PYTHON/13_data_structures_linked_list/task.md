# Task: Implement a Complete Linked List

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Implement Node and LinkedList Classes
Create the basic structure:
- `Node` class with `data` and `next` attributes
- `LinkedList` class with `head` attribute (initially None)
- Method: `is_empty()` - returns True if list is empty
- Method: `print_list()` - prints all elements in format: data1 -> data2 -> None

## Goal 2: Implement Insertion Methods
Add the following methods to LinkedList:
- `insert_at_beginning(data)` - insert node at start (O(1))
- `insert_at_end(data)` - insert node at end (O(n))
- `insert_at_position(data, position)` - insert at specific position
- `get_length()` - return number of nodes

## Goal 3: Implement Deletion and Search Methods
Add the following methods:
- `delete_by_value(value)` - delete first occurrence of value, return True if found
- `delete_at_position(position)` - delete node at position
- `search(value)` - return True if value exists in list
- `reverse()` - reverse the linked list in-place

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Creating linked list...
10 -> 20 -> 30 -> None
Length: 3

Inserting at beginning (5):
5 -> 10 -> 20 -> 30 -> None

Inserting at position 2 (15):
5 -> 10 -> 15 -> 20 -> 30 -> None

Deleting value 20:
5 -> 10 -> 15 -> 30 -> None

Search for 15: True
Search for 99: False

Reversing list:
30 -> 15 -> 10 -> 5 -> None
```
