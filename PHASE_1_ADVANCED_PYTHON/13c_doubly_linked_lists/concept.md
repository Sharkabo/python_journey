# Unit 13c: Doubly Linked Lists

## YouTube Recommendations
- "Doubly linked list Python"
- "Doubly linked list tutorial"

---

## 1. Doubly Linked Node

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
```

---

## Spiral Learning Note

Can traverse both directions. Used in browser history, undo/redo.
