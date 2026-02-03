# Task: Implement and Compare Algorithms

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Implement Sorting Algorithms
Implement the following sorting algorithms:
- `bubble_sort(arr)` - O(n²) time, O(1) space
- `merge_sort(arr)` - O(n log n) time, O(n) space (include helper `merge` function)
- `quick_sort(arr)` - O(n log n) average time

Test each with: `[64, 34, 25, 12, 22, 11, 90]`

## Goal 2: Implement Searching Algorithms
Implement the following search algorithms:
- `linear_search(arr, target)` - returns index or -1
- `binary_search(sorted_arr, target)` - returns index or -1 (iterative)
- `binary_search_recursive(sorted_arr, target)` - recursive version

Test with sorted array and various targets.

## Goal 3: Solve Algorithm Problems
Implement the following optimization problems:
- `find_duplicates_fast(items)` - O(n) time using hash set
- `two_sum(numbers, target)` - O(n) time using hash map
- `max_sum_subarray(arr, k)` - O(n) time using sliding window

Each function should include a docstring explaining its time and space complexity.

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Testing Sorting Algorithms:
Original: [64, 34, 25, 12, 22, 11, 90]
Bubble Sort: [11, 12, 22, 25, 34, 64, 90]
Merge Sort: [11, 12, 22, 25, 34, 64, 90]
Quick Sort: [11, 12, 22, 25, 34, 64, 90]

Testing Search Algorithms:
Sorted array: [11, 12, 22, 25, 34, 64, 90]
Linear search for 25: index 3
Binary search for 25: index 3
Binary search (recursive) for 25: index 3
Search for 100: -1 (not found)

Testing Optimization Problems:
find_duplicates_fast([1, 2, 3, 2, 4, 3]): {2, 3}
two_sum([2, 7, 11, 15], target=9): (0, 1)
max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], k=4): 39
```
