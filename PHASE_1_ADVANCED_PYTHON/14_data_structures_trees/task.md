# Task: Implement a Binary Search Tree

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Implement TreeNode and BST Classes
Create the basic structure:
- `TreeNode` class with `data`, `left`, and `right` attributes
- `BinarySearchTree` class with `root` attribute (initially None)
- Method: `is_empty()` - returns True if tree is empty
- Method: `insert(data)` - adds a new value maintaining BST property

## Goal 2: Implement Search and Traversal Methods
Add the following methods to BinarySearchTree:
- `search(data)` - returns True if value exists in tree
- `inorder_traversal()` - returns list of values in sorted order
- `preorder_traversal()` - returns list in preorder (Root-Left-Right)
- `postorder_traversal()` - returns list in postorder (Left-Right-Root)

## Goal 3: Implement Utility Methods
Add the following methods:
- `find_min()` - returns minimum value in tree
- `find_max()` - returns maximum value in tree
- `height()` - returns height of tree
- `size()` - returns total number of nodes

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Creating BST...
Inserting: 50, 30, 70, 20, 40, 60, 80

Inorder traversal (sorted): [20, 30, 40, 50, 60, 70, 80]
Preorder traversal: [50, 30, 20, 40, 70, 60, 80]
Postorder traversal: [20, 40, 30, 60, 80, 70, 50]

Search for 40: True
Search for 100: False

Minimum value: 20
Maximum value: 80
Tree height: 2
Tree size: 7 nodes
```
