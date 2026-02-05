# Unit 14a:  Tree Basics

## YouTube Recommendations
- "Binary tree Python"
- "Tree data structure"

---

## 1. Tree Structure

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

# Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

---

## Spiral Learning Note

Trees organize data hierarchically. Essential for algorithms.
