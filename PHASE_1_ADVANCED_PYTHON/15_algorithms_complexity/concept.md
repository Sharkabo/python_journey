# Unit 15: Algorithms and Complexity

## YouTube Recommendations
If you find learning from text difficult, search for these keywords:
- "Big O notation explained"
- "Python sorting algorithms"
- "Algorithm complexity tutorial"
- "Python 演算法複雜度"
- "Big O 時間複雜度"

Recommended Channels:
- Abdul Bari (Algorithms)
- CS Dojo (Computer Science)
- Back To Back SWE
- freeCodeCamp.org

---

## 1. What is Algorithm Complexity?

Algorithm complexity describes how the runtime or memory usage of an algorithm grows as the input size increases. This is measured using Big O notation.

**Why It Matters:**
- Writing efficient code is crucial for scalability
- Helps choose the right algorithm for the problem
- Essential for technical interviews
- Important for backend performance optimization

**Big O Notation Basics:**
```
O(1)       - Constant time (best)
O(log n)   - Logarithmic time
O(n)       - Linear time
O(n log n) - Linearithmic time
O(n²)      - Quadratic time
O(2^n)     - Exponential time (worst)
```

---

## 2. Time Complexity Examples

**O(1) - Constant Time:**
```python
def get_first_element(items: list) -> any:
    """Always takes same time regardless of list size"""
    return items[0]  # O(1)

def get_value_from_dict(data: dict, key: str) -> any:
    """Dictionary lookup is O(1)"""
    return data[key]  # O(1)
```

**O(n) - Linear Time:**
```python
def find_max(numbers: list[int]) -> int:
    """Must check every element once"""
    max_val = numbers[0]
    for num in numbers:  # O(n)
        if num > max_val:
            max_val = num
    return max_val

def sum_list(numbers: list[int]) -> int:
    """Must visit each element"""
    total = 0
    for num in numbers:  # O(n)
        total += num
    return total
```

**O(n²) - Quadratic Time:**
```python
def bubble_sort(arr: list[int]) -> list[int]:
    """Nested loops over same data"""
    n = len(arr)
    for i in range(n):           # O(n)
        for j in range(n - i - 1):  # O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # Total: O(n²)

def find_duplicates_slow(items: list) -> list:
    """Check each pair of items"""
    duplicates = []
    for i in range(len(items)):        # O(n)
        for j in range(i + 1, len(items)):  # O(n)
            if items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates  # O(n²)
```

**O(log n) - Logarithmic Time:**
```python
def binary_search(arr: list[int], target: int) -> int:
    """Halves search space each iteration"""
    left, right = 0, len(arr) - 1
    
    while left <= right:  # O(log n)
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
```

---

## 3. Space Complexity

Space complexity measures memory usage as input grows.

**O(1) Space - Constant:**
```python
def sum_numbers(numbers: list[int]) -> int:
    """Only uses one variable regardless of input size"""
    total = 0  # O(1) space
    for num in numbers:
        total += num
    return total
```

**O(n) Space - Linear:**
```python
def create_copy(numbers: list[int]) -> list[int]:
    """Creates a new list same size as input"""
    return numbers[:]  # O(n) space

def fibonacci_list(n: int) -> list[int]:
    """Stores n fibonacci numbers"""
    fib = [0, 1]  # O(n) space
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
```

---

## 4. Sorting Algorithms

**Bubble Sort - O(n²):**
```python
def bubble_sort(arr: list[int]) -> list[int]:
    """Simple but slow sorting algorithm"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Optimization: already sorted
            break
    return arr

# Time: O(n²), Space: O(1)
```

**Selection Sort - O(n²):**
```python
def selection_sort(arr: list[int]) -> list[int]:
    """Find minimum and swap to front"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Time: O(n²), Space: O(1)
```

**Merge Sort - O(n log n):**
```python
def merge_sort(arr: list[int]) -> list[int]:
    """Divide and conquer sorting - efficient!"""
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Time: O(n log n), Space: O(n)
```

**Quick Sort - O(n log n) average:**
```python
def quick_sort(arr: list[int]) -> list[int]:
    """Fast in-place sorting algorithm"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Time: O(n log n) average, O(n²) worst
# Space: O(n)
```

---

## 5. Searching Algorithms

**Linear Search - O(n):**
```python
def linear_search(arr: list[int], target: int) -> int:
    """Check each element sequentially"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Time: O(n), Space: O(1)
# Works on unsorted arrays
```

**Binary Search - O(log n):**
```python
def binary_search(arr: list[int], target: int) -> int:
    """Efficient search on sorted arrays"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Time: O(log n), Space: O(1)
# Requires sorted array!
```

**Binary Search (Recursive):**
```python
def binary_search_recursive(
    arr: list[int], 
    target: int, 
    left: int = 0, 
    right: int | None = None
) -> int:
    """Recursive version of binary search"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Time: O(log n), Space: O(log n) due to recursion stack
```

---

## 6. Common Algorithm Patterns

**Two Pointers:**
```python
def is_palindrome(s: str) -> bool:
    """Check if string is palindrome using two pointers"""
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Time: O(n), Space: O(1)
```

**Sliding Window:**
```python
def max_sum_subarray(arr: list[int], k: int) -> int:
    """Find maximum sum of k consecutive elements"""
    if len(arr) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Time: O(n), Space: O(1)
```

**Hash Map for Fast Lookup:**
```python
def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Find two numbers that sum to target"""
    seen = {}  # O(n) space
    
    for i, num in enumerate(numbers):  # O(n) time
        complement = target - num
        if complement in seen:  # O(1) lookup
            return (seen[complement], i)
        seen[num] = i
    
    return None

# Time: O(n), Space: O(n)
# Without hash map would be O(n²)
```

---

## 7. Practical Complexity Analysis

**Comparing Algorithms:**
```python
# Problem: Find duplicates in a list

# Solution 1: Nested loops - O(n²)
def find_duplicates_slow(items: list) -> set:
    duplicates = set()
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                duplicates.add(items[i])
    return duplicates

# Solution 2: Using a set - O(n)
def find_duplicates_fast(items: list) -> set:
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return duplicates

# For n=1000 items:
# Slow: ~1,000,000 operations
# Fast: ~1,000 operations
# 1000x faster!
```

---

## 8. Algorithm Selection Guide

**When to Use Each:**
```python
# Sorting:
# - Small data (< 50 items): Any algorithm works
# - Large data: Merge sort or Quick sort O(n log n)
# - Nearly sorted: Bubble sort with optimization O(n)
# - In-place needed: Quick sort

# Searching:
# - Unsorted data: Linear search O(n)
# - Sorted data: Binary search O(log n)
# - Frequent lookups: Hash map O(1)

# Data structures:
# - Fast insertion/deletion at front: Linked List O(1)
# - Fast random access: Array/List O(1)
# - Fast lookup: Hash map/Dictionary O(1)
# - Sorted data: Binary Search Tree O(log n)
```

---

## Spiral Learning Note

**Connection to Previous Learning:**
- Unit 13-14: Data structures have different complexity for operations
- Linked lists: O(1) insert at front, O(n) access
- Trees: O(log n) for balanced BST operations
- Understanding complexity helps choose right data structure

**Preparation for Next Lesson:**
- Unit 16: Capstone project will combine all concepts
- You'll need to choose efficient algorithms for real problems
- Understanding complexity makes you a better developer

**Real-World Application:**
- Backend API performance optimization
- Database query optimization
- Choosing caching strategies
- Scalability planning
- Technical interview success
- This knowledge separates junior from senior developers
