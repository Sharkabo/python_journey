# Unit 13b: Linked List Operations

## YouTube Recommendations
- "Linked list insert delete"
- "Linked list operations"

---

## 1. Insert Operation

```python
def insert(self, position, data):
    new_node = Node(data)
    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return
    current = self.head
    for _ in range(position - 1):
        if not current:
            return
        current = current.next
    new_node.next = current.next
    current.next = new_node
```

---

## Spiral Learning Note

Insert, delete, search are core linked list operations.
