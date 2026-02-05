# Unit 14c: Tree Traversal

## YouTube Recommendations
- "Tree traversal Python"
- "DFS BFS tree"

---

## 1. DFS Traversal

```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
```

---

## Spiral Learning Note

Different traversals for different use cases.
