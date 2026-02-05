# Unit 14b: Binary Search Tree

## YouTube Recommendations
- "BST Python tutorial"
- "Binary search tree insert"

---

## 1. BST Insert

```python
class BST:
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left:
                self._insert_recursive(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert_recursive(node.right, data)
            else:
                node.right = TreeNode(data)
```

---

## Spiral Learning Note

BST maintains sorted order. O(log n) search time.
