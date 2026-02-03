# Unit 14: Data Structures - Trees

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Binary tree Python implementation"
- "Binary search tree tutorial"
- "Tree traversal algorithms"
- "Python 二元樹"
- "資料結構 tree"

Recommended Channels:
- CS Dojo (Data Structures)
- Abdul Bari (Algorithms)
- freeCodeCamp.org
- Back To Back SWE

---

## 1. What is a Tree?

A tree is a hierarchical data structure consisting of nodes connected by edges. Unlike linked lists which are linear, trees are hierarchical.

**Key Terms:**
- **Node**: Contains data and references to child nodes
- **Root**: Top node (has no parent)
- **Parent**: Node with children
- **Child**: Node connected below another node
- **Leaf**: Node with no children
- **Height**: Longest path from root to any leaf
- **Depth**: Distance from root to a node

**Visual Representation:**
```
        10          Root
       /  \
      5    15       Level 1
     / \   / \
    3   7 12  20    Level 2 (Leaves)
```

---

## 2. Binary Tree

A binary tree is a tree where each node has at most two children (left and right).

**Binary Tree Node:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None   # Left child
        self.right = None  # Right child

# Creating a simple binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

# Tree structure:
#     10
#    /  \
#   5    15
#  / \
# 3   7
```

---

## 3. Binary Search Tree (BST)

A Binary Search Tree is a binary tree with a special property:
- Left subtree contains only nodes with values LESS than the parent
- Right subtree contains only nodes with values GREATER than the parent
- This property applies to ALL nodes

**BST Example:**
```
        10          Valid BST
       /  \
      5    15       5 < 10 < 15
     / \   / \
    3   7 12  20    3 < 5 < 7, 12 < 15 < 20
```

**Why BST is Useful:**
- Efficient searching: O(log n) average case
- Efficient insertion: O(log n) average case
- Efficient deletion: O(log n) average case
- In-order traversal gives sorted output

---

## 4. BST Implementation

**TreeNode and BST Classes:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode | None = None
    
    def is_empty(self) -> bool:
        return self.root is None
```

**Insert Operation:**
```python
def insert(self, data):
    """Insert a new value into BST"""
    if self.root is None:
        self.root = TreeNode(data)
    else:
        self._insert_recursive(self.root, data)

def _insert_recursive(self, node, data):
    """Helper method for recursive insertion"""
    if data < node.data:
        # Go left
        if node.left is None:
            node.left = TreeNode(data)
        else:
            self._insert_recursive(node.left, data)
    else:
        # Go right (including duplicates)
        if node.right is None:
            node.right = TreeNode(data)
        else:
            self._insert_recursive(node.right, data)

# Usage
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(20)
```

**Search Operation:**
```python
def search(self, data) -> bool:
    """Search for a value in BST"""
    return self._search_recursive(self.root, data)

def _search_recursive(self, node, data) -> bool:
    """Helper method for recursive search"""
    if node is None:
        return False
    
    if data == node.data:
        return True
    elif data < node.data:
        return self._search_recursive(node.left, data)
    else:
        return self._search_recursive(node.right, data)

# Usage
print(bst.search(7))   # True
print(bst.search(100)) # False
```

---

## 5. Tree Traversal Methods

Tree traversal means visiting all nodes in a specific order.

**Inorder Traversal (Left - Root - Right):**
```python
def inorder_traversal(self) -> list:
    """Returns sorted list of values"""
    result = []
    self._inorder_recursive(self.root, result)
    return result

def _inorder_recursive(self, node, result):
    if node is not None:
        self._inorder_recursive(node.left, result)   # Left
        result.append(node.data)                      # Root
        self._inorder_recursive(node.right, result)   # Right

# Usage
#     10
#    /  \
#   5    15
#  / \   / \
# 3   7 12  20

print(bst.inorder_traversal())  # [3, 5, 7, 10, 12, 15, 20] (sorted!)
```

**Preorder Traversal (Root - Left - Right):**
```python
def preorder_traversal(self) -> list:
    """Used for creating a copy of the tree"""
    result = []
    self._preorder_recursive(self.root, result)
    return result

def _preorder_recursive(self, node, result):
    if node is not None:
        result.append(node.data)                      # Root
        self._preorder_recursive(node.left, result)   # Left
        self._preorder_recursive(node.right, result)  # Right

# Usage
print(bst.preorder_traversal())  # [10, 5, 3, 7, 15, 12, 20]
```

**Postorder Traversal (Left - Right - Root):**
```python
def postorder_traversal(self) -> list:
    """Used for deleting the tree"""
    result = []
    self._postorder_recursive(self.root, result)
    return result

def _postorder_recursive(self, node, result):
    if node is not None:
        self._postorder_recursive(node.left, result)   # Left
        self._postorder_recursive(node.right, result)  # Right
        result.append(node.data)                       # Root

# Usage
print(bst.postorder_traversal())  # [3, 7, 5, 12, 20, 15, 10]
```

---

## 6. Finding Min and Max

**Minimum Value (Leftmost Node):**
```python
def find_min(self) -> int | None:
    """Find minimum value in BST"""
    if self.root is None:
        return None
    
    current = self.root
    while current.left is not None:
        current = current.left
    
    return current.data

# Usage
print(bst.find_min())  # 3
```

**Maximum Value (Rightmost Node):**
```python
def find_max(self) -> int | None:
    """Find maximum value in BST"""
    if self.root is None:
        return None
    
    current = self.root
    while current.right is not None:
        current = current.right
    
    return current.data

# Usage
print(bst.find_max())  # 20
```

---

## 7. Tree Height and Size

**Calculate Height:**
```python
def height(self) -> int:
    """Calculate height of tree"""
    return self._height_recursive(self.root)

def _height_recursive(self, node) -> int:
    if node is None:
        return -1  # Height of empty tree is -1
    
    left_height = self._height_recursive(node.left)
    right_height = self._height_recursive(node.right)
    
    return 1 + max(left_height, right_height)

# Usage
print(bst.height())  # 2
```

**Count Nodes:**
```python
def size(self) -> int:
    """Count total number of nodes"""
    return self._size_recursive(self.root)

def _size_recursive(self, node) -> int:
    if node is None:
        return 0
    
    return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

# Usage
print(bst.size())  # 7
```

---

## 8. Complete BST Implementation

**Full Implementation:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode | None = None
    
    def insert(self, data) -> None:
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data) -> bool:
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data) -> bool:
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def inorder_traversal(self) -> list:
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

# Complete usage
bst = BinarySearchTree()
values = [10, 5, 15, 3, 7, 12, 20]
for val in values:
    bst.insert(val)

print("Inorder (sorted):", bst.inorder_traversal())
print("Search 7:", bst.search(7))
print("Search 100:", bst.search(100))
```

---

## 9. Time Complexity

**BST Operations (Average Case):**
```
Operation          Average      Worst Case
------------------------------------------------
Search             O(log n)     O(n) - unbalanced
Insert             O(log n)     O(n) - unbalanced
Delete             O(log n)     O(n) - unbalanced
Traversal          O(n)         O(n)
Find Min/Max       O(log n)     O(n) - unbalanced
```

**Why Worst Case is O(n):**
If you insert sorted data, the BST becomes a linked list:
```
1
 \
  2
   \
    3  (This is O(n) for search!)
```

**Solution:** Use self-balancing trees (AVL, Red-Black) - beyond this course.

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 13: Trees are like linked lists but with TWO next pointers
- Unit 01-04: Recursion (important for tree operations) builds on OOP
- Understanding node references from linked lists is crucial

**Preparation for Next Lesson:**
- Unit 15: Algorithms (sorting, searching)
- Tree traversal is similar to sorting algorithms
- Understanding recursion helps with recursive algorithms

**Real-World Application:**
- File systems (directory structures)
- Database indexing (B-trees, B+ trees)
- Expression parsing (AST in compilers)
- Autocomplete systems
- Decision trees in machine learning
- Hierarchical data representation
