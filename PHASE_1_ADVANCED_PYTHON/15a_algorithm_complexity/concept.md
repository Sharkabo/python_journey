# Unit 15a: Algorithm Complexity

## YouTube Recommendations
- "Big O notation Python"
- "Time complexity tutorial"

---

## 1. Big O Notation

```python
# O(1) - Constant
def get_first(arr):
    return arr[0]

# O(n) - Linear
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

---

## Spiral Learning Note

Understanding efficiency is crucial for optimization.
