# Top 'K' Elements


# 1. K Largest Elements
"""
Task: Find the k largest elements in an array.
Example: [1, 3, 5, 2], k=2 → [5, 3]
Why: Introduces top-k selection."
"""

# Solution
import heapq

def k_largest_elements(arr, k):
    """
    Finds the k largest elements in the array.
    
    - Uses a min-heap to maintain k largest elements.
    - Time Complexity: O(n log k), Space Complexity: O(k).
    - Heap is efficient and beginner-friendly with Python's heapq.
    """
    if k > len(arr):
        return None
    heap = arr[:k]  # Take first k elements
    heapq.heapify(heap)  # Create min-heap
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heappop(heap)  # Remove smallest
            heapq.heappush(heap, num)  # Add larger element
    return heap

# Test the function
print(k_largest_elements([1, 3, 5, 2], 2))  # Output: [3, 5] (order may vary)


# ----------------------------------------------------------------------------------
# 2. Kth Largest Element
"""
Task: Find the kth largest element in an array.
Example: [3, 2, 1, 5], k=2 → 3
Why: Prepares for Top 'K' Frequent Elements.
"""

# Solution
def kth_largest_element(arr, k):
    """
    Finds the kth largest element in the array.
    
    - Sorts array and selects kth from end.
    - Time Complexity: O(n log n), Space Complexity: O(1).
    - Sorting is simpler for beginners; heap could be O(n log k) but is more complex.
    """
    if k > len(arr):
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[-k]

# Test the function
print(kth_largest_element([3, 2, 1, 5], 2))  # Output: 3


# ----------------------------------------------------------------------------------
# 3. Sort First K Elements
"""
Task: Sort the first k elements of an array in descending order.
Example: [1, 4, 3, 2], k=3 → [4, 3, 1, 2]
Why: Builds sorting intuition without heaps.
"""

# Solution
def sort_first_k(arr, k):
    """
    Sorts the first k elements of the array in descending order.
    
    - Sorts subarray in-place and reverses for descending order.
    - Time Complexity: O(k log k), Space Complexity: O(1).
    - Simple sorting is beginner-friendly.
    """
    if k > len(arr):
        return arr
    arr[:k] = sorted(arr[:k], reverse=True)
    return arr

# Test the function
print(sort_first_k([1, 4, 3, 2], 3))  # Output: [4, 3, 1, 2]


# ----------------------------------------------------------------------------------
# 4. K Smallest Elements
"""
Task: Find the k smallest elements in an array.
Example: [5, 2, 1, 4], k=2 → [1, 2]
Why: Encourages heap-like thinking.
"""

# Solution
def k_smallest_elements(arr, k):
    """
    Finds the k smallest elements in the array.
    
    - Uses a max-heap (with negatives) to track smallest elements.
    - Time Complexity: O(n log k), Space Complexity: O(k).
    - Heap approach is efficient and teachable with heapq.
    """
    if k > len(arr):
        return None
    heap = [-num for num in arr[:k]]  # Negate for max-heap behavior
    heapq.heapify(heap)
    for num in arr[k:]:
        if -num > heap[0]:  # Compare with largest negative
            heapq.heappop(heap)
            heapq.heappush(heap, -num)
    return [-num for num in heap]  # Convert back to positive

# Test the function
print(k_smallest_elements([5, 2, 1, 4], 2))  # Output: [1, 2] (order may vary)


# ----------------------------------------------------------------------------------
# 5. Merge K Sorted Lists (Simple)
"""
Task: Merge k sorted lists of size 2 into one sorted list.
Example: [[1, 3], [2, 4]] → [1, 2, 3, 4]
Why: Introduces multi-list handling."
"""

# Solution
def merge_k_sorted_lists(lists):
    """
    Merges k sorted lists into one sorted list.
    
    - Uses a min-heap to efficiently select the smallest element.
    - Time Complexity: O(N log k) where N is total elements, Space Complexity: O(k).
    - Heap-based merging is efficient and manageable for beginners.
    """
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list index, element index)
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    return result

# Test the function
print(merge_k_sorted_lists([[1, 3], [2, 4]]))  # Output: [1, 2, 3, 4]


