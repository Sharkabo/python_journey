# Unit 13: Data Structures - Linked List

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Python linked list implementation"
- "Linked list data structure"
- "Singly linked list tutorial"
- "Python 鏈結串列"
- "資料結構 linked list"

Recommended Channels:
- CS Dojo (Data Structures)
- freeCodeCamp.org
- Abdul Bari (Algorithms)
- Tech With Tim (Python)

---

## 1. What is a Linked List?

A linked list is a linear data structure where elements (called nodes) are connected through pointers/references. Unlike arrays, linked list elements are not stored in contiguous memory locations.

**Key Concepts:**
- **Node**: Contains data and reference to the next node
- **Head**: First node in the list
- **Tail**: Last node in the list (points to None)
- **Dynamic Size**: Can grow or shrink at runtime

**Linked List vs Array:**
```python
# Array (List in Python)
- Fixed or resized with copying
- Fast random access: O(1)
- Slow insertion/deletion at beginning: O(n)
- Contiguous memory

# Linked List
- Dynamic size, no resizing needed
- Slow random access: O(n)
- Fast insertion/deletion at beginning: O(1)
- Non-contiguous memory
```

**Visual Representation:**
```
Head -> [Data|Next] -> [Data|Next] -> [Data|None]
        Node 1         Node 2         Node 3 (Tail)
```

---

## 2. Node Implementation

A node is the building block of a linked list.

**Node Class:**
```python
class Node:
    def __init__(self, data):
        self.data = data  # Store the value
        self.next = None  # Reference to next node (initially None)

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes manually
node1.next = node2
node2.next = node3

# Traversing the linked list
current = node1
while current:
    print(current.data)  # 10, 20, 30
    current = current.next
```

---

## 3. Linked List Implementation

**Basic LinkedList Class:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # Start with empty list
    
    def is_empty(self):
        """Check if list is empty"""
        return self.head is None
    
    def print_list(self):
        """Print all elements"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Using the linked list
ll = LinkedList()
print(ll.is_empty())  # True

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link them
ll.head = node1
node1.next = node2
node2.next = node3

ll.print_list()  # 1 -> 2 -> 3 -> None
```

---

## 4. Insertion Operations

**Insert at Beginning (Prepend):**
```python
def insert_at_beginning(self, data):
    """Insert node at the start - O(1)"""
    new_node = Node(data)
    new_node.next = self.head  # Point to current head
    self.head = new_node       # Update head

# Usage
ll = LinkedList()
ll.insert_at_beginning(3)  # 3 -> None
ll.insert_at_beginning(2)  # 2 -> 3 -> None
ll.insert_at_beginning(1)  # 1 -> 2 -> 3 -> None
```

**Insert at End (Append):**
```python
def insert_at_end(self, data):
    """Insert node at the end - O(n)"""
    new_node = Node(data)
    
    if self.head is None:  # Empty list
        self.head = new_node
        return
    
    # Traverse to the end
    current = self.head
    while current.next:
        current = current.next
    
    current.next = new_node

# Usage
ll = LinkedList()
ll.insert_at_end(1)    # 1 -> None
ll.insert_at_end(2)    # 1 -> 2 -> None
ll.insert_at_end(3)    # 1 -> 2 -> 3 -> None
```

**Insert at Position:**
```python
def insert_at_position(self, data, position):
    """Insert node at specific position - O(n)"""
    if position == 0:
        self.insert_at_beginning(data)
        return
    
    new_node = Node(data)
    current = self.head
    
    # Traverse to position - 1
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of range")
        current = current.next
    
    if current is None:
        raise IndexError("Position out of range")
    
    new_node.next = current.next
    current.next = new_node

# Usage
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(3)
ll.insert_at_position(2, 1)  # 1 -> 2 -> 3 -> None
```

---

## 5. Deletion Operations

**Delete from Beginning:**
```python
def delete_from_beginning(self):
    """Delete first node - O(1)"""
    if self.head is None:
        raise ValueError("Cannot delete from empty list")
    
    self.head = self.head.next

# Usage
ll.print_list()  # 1 -> 2 -> 3 -> None
ll.delete_from_beginning()
ll.print_list()  # 2 -> 3 -> None
```

**Delete by Value:**
```python
def delete_by_value(self, value):
    """Delete first node with given value - O(n)"""
    if self.head is None:
        raise ValueError("Cannot delete from empty list")
    
    # If head node contains the value
    if self.head.data == value:
        self.head = self.head.next
        return
    
    # Search for the value
    current = self.head
    while current.next:
        if current.next.data == value:
            current.next = current.next.next
            return
        current = current.next
    
    raise ValueError(f"Value {value} not found")

# Usage
ll.print_list()  # 1 -> 2 -> 3 -> None
ll.delete_by_value(2)
ll.print_list()  # 1 -> 3 -> None
```

---

## 6. Search and Traversal

**Search for Value:**
```python
def search(self, value):
    """Search for a value - O(n)"""
    current = self.head
    position = 0
    
    while current:
        if current.data == value:
            return position
        current = current.next
        position += 1
    
    return -1  # Not found

# Usage
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print(ll.search(20))  # 1
print(ll.search(40))  # -1 (not found)
```

**Get Length:**
```python
def get_length(self):
    """Count number of nodes - O(n)"""
    count = 0
    current = self.head
    
    while current:
        count += 1
        current = current.next
    
    return count

# Usage
print(ll.get_length())  # 3
```

---

## 7. Complete LinkedList Implementation

**Full Implementation with Type Hints:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def insert_at_beginning(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_by_value(self, value) -> bool:
        if self.head is None:
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        
        return False
    
    def search(self, value) -> bool:
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def print_list(self) -> None:
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# Complete usage example
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_beginning(0)
ll.print_list()  # 0 -> 1 -> 2 -> 3 -> None

ll.delete_by_value(2)
ll.print_list()  # 0 -> 1 -> 3 -> None

print(ll.search(1))  # True
print(ll.search(5))  # False
```

---

## 8. Time Complexity Analysis

**Common Operations:**
```python
Operation                 Time Complexity
-------------------------------------------
Access by index          O(n)
Search by value          O(n)
Insert at beginning      O(1)
Insert at end            O(n)  # Can be O(1) with tail pointer
Insert at position       O(n)
Delete from beginning    O(1)
Delete by value          O(n)
Get length               O(n)  # Can be O(1) by keeping count
```

**When to Use Linked Lists:**
- Frequent insertions/deletions at the beginning
- Unknown or changing size
- No need for random access
- Memory fragmentation is not a concern

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 01-04: OOP concepts used to create Node and LinkedList classes
- Unit 05: Type hints make linked list code clearer
- Phase 0: Lists and loops are foundation for understanding linked lists

**Preparation for Next Lesson:**
- Unit 14: Trees are recursive linked structures
- Understanding node references is crucial for trees
- Similar traversal patterns will be used

**Real-World Application:**
- Implementing undo/redo functionality
- Music playlist management
- Browser history (back/forward navigation)
- Memory allocation in operating systems
- Understanding how databases index data
- Foundation for more complex data structures
