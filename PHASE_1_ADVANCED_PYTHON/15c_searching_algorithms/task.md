# Task: Implement Searching Algorithms

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Implement Linear Search
Create `linear_search(arr, target)` that:
- Searches through array sequentially
- Returns index if found, -1 if not
- Works on unsorted arrays

## Goal 2: Implement Binary Search
Create `binary_search(arr, target)` that:
- Only works on sorted arrays
- Uses divide-and-conquer
- Returns index if found, -1 if not
- Much faster than linear search

## Goal 3: Compare Search Performance
Create benchmarks that:
- Test both algorithms on large arrays
- Measure execution time
- Demonstrate O(n) vs O(log n) difference

---

**Expected Output:**
```text
Array (sorted): [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

Linear search for 15: Found at index 7 (10 comparisons)
Binary search for 15: Found at index 7 (3 comparisons)

Linear search: O(n) - slow on large arrays
Binary search: O(log n) - fast but requires sorted array
```
