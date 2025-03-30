# Top 'K' Elements
"""
Foundational Skills
   - Heap operations (min-heap, max-heap)
   - Sorting algorithms
Potential Knowledge Gaps
   - Unfamiliarity with heap data structures
   - Difficulty maintaining a heap of size k
"""

# ----------------------------------------------------------------------------------
# 1. K Largest Elements
"""
Task: Find the k largest elements in an array.
Example: [1, 3, 5, 2], k=2 → [5, 3]
Why: Introduces top-k selection."
"""

import heapq

def k_largest_elements(arr, k):
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
# print(k_largest_elements([1, 3, 5, 2], 2))  # Output: [3, 5] (order may vary)


# Solution
import heapq   # Import the heapq module for heap operations

def k_largest_elements(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the k largest elements in the array.
    
    - Uses a min-heap to maintain k largest elements.
    - Time Complexity: O(n log k), Space Complexity: O(k).
    - Heap is efficient and beginner-friendly with Python's heapq.
    """
    if k > len(arr):   # Check if 'k' is larger than the array length
        return None    # Return None since we can't find k elements
    heap = arr[:k]     # Take the first k elements from 'arr' to start our heap
    heapq.heapify(heap)  # Turn these k elements into a min-heap (smallest at the root)
    for num in arr[k:]:  # Loop through the rest of the array starting after the first k elements
        if num > heap[0]:  # If the current number is bigger than the smallest in the heap
            heapq.heappop(heap)  # Remove the smallest element from the heap
            heapq.heappush(heap, num)  # Add the current (larger) number to the heap
    return heap        # Return the heap, which now holds the k largest elements

# Test the function
# print(k_largest_elements([1, 3, 5, 2], 2))  # Output: [3, 5] (order may vary)


# ----------------------------------------------------------------------------------
# 2. Kth Largest Element
"""
Task: Find the kth largest element in an array.
Example: [3, 2, 1, 5], k=2 → 3
Why: Prepares for Top 'K' Frequent Elements.
"""

def kth_largest_element(arr, k):
    if k > len(arr):
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[-k]

# Test the function
# print(kth_largest_element([3, 2, 1, 5], 2))  # Output: 3


# Solution
def kth_largest_element(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the kth largest element in the array.
    
    - Sorts array and selects kth from end.
    - Time Complexity: O(n log n), Space Complexity: O(1).
    - Sorting is simpler for beginners; heap could be O(n log k) but is more complex.
    """
    if k > len(arr):   # Check if 'k' is larger than the array length
        return None    # Return None since there isn’t a kth element
    sorted_arr = sorted(arr)  # Sort the array in ascending order (smallest to largest)
    return sorted_arr[-k]     # Return the kth element from the end (kth largest)

# Test the function
# print(kth_largest_element([3, 2, 1, 5], 2))  # Output: 3


# ----------------------------------------------------------------------------------
# 3. Sort First K Elements
"""
Task: Sort the first k elements of an array in descending order.
Example: [1, 4, 3, 2], k=3 → [4, 3, 1, 2]
Why: Builds sorting intuition without heaps.
"""

def sort_first_k(arr, k):
    if k > len(arr):
        return arr
    arr[:k] = sorted(arr[:k], reverse=True)
    return arr

# Test the function
# print(sort_first_k([1, 4, 3, 2], 3))  # Output: [4, 3, 1, 2]


# Solution
def sort_first_k(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Sorts the first k elements of the array in descending order.
    
    - Sorts subarray in-place and reverses for descending order.
    - Time Complexity: O(k log k), Space Complexity: O(1).
    - Simple sorting is beginner-friendly.
    """
    if k > len(arr):   # Check if 'k' is larger than the array length
        return arr     # Return the array unchanged since we can’t sort beyond its length
    arr[:k] = sorted(arr[:k], reverse=True)  # Sort the first k elements in descending order
    return arr         # Return the modified array with first k elements sorted

# Test the function
# print(sort_first_k([1, 4, 3, 2], 3))  # Output: [4, 3, 1, 2]


# ----------------------------------------------------------------------------------
# 4. K Smallest Elements
"""
Task: Find the k smallest elements in an array.
Example: [5, 2, 1, 4], k=2 → [1, 2]
Why: Encourages heap-like thinking.
"""

import heapq   # Import the heapq module for heap operations

def k_smallest_elements(arr, k):
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
# print(k_smallest_elements([5, 2, 1, 4], 2))  # Output: [1, 2] (order may vary)


# Solution
import heapq   # Import the heapq module for heap operations

def k_smallest_elements(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the k smallest elements in the array.
    
    - Uses a max-heap (with negatives) to track smallest elements.
    - Time Complexity: O(n log k), Space Complexity: O(k).
    - Heap approach is efficient and teachable with heapq.
    """
    if k > len(arr):   # Check if 'k' is larger than the array length
        return None    # Return None since we can’t find k elements
    heap = [-num for num in arr[:k]]  # Take first k elements and negate them (to simulate a max-heap)
    heapq.heapify(heap)  # Turn these negated elements into a min-heap (largest negative at root)
    for num in arr[k:]:  # Loop through the rest of the array starting after the first k elements
        if -num > heap[0]:  # If the negated current number is bigger than the largest negative (smallest original)
            heapq.heappop(heap)  # Remove the largest negative (smallest original number)
            heapq.heappush(heap, -num)  # Add the negated current number to the heap
    return [-num for num in heap]  # Convert all negated numbers back to positive (k smallest elements)

# Test the function
# print(k_smallest_elements([5, 2, 1, 4], 2))  # Output: [1, 2] (order may vary)


# ----------------------------------------------------------------------------------
# 5. Merge K Sorted Lists (Simple)
"""
Task: Merge k sorted lists of size 2 into one sorted list.
Example: [[1, 3], [2, 4]] → [1, 2, 3, 4]
Why: Introduces multi-list handling."
"""

import heapq   # Import the heapq module for heap operations

def merge_k_sorted_lists(lists):
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
# print(merge_k_sorted_lists([[1, 3], [2, 4]]))  # Output: [1, 2, 3, 4]


# Solution
import heapq   # Import the heapq module for heap operations

def merge_k_sorted_lists(lists):   # Define the function that takes a list of sorted lists 'lists'
    """
    Merges k sorted lists into one sorted list.
    
    - Uses a min-heap to efficiently select the smallest element.
    - Time Complexity: O(N log k) where N is total elements, Space Complexity: O(k).
    - Heap-based merging is efficient and manageable for beginners.
    """
    heap = []   # Create an empty heap to store elements we’re merging
    for i, lst in enumerate(lists):  # Loop through each list in 'lists' with its index 'i'
        if lst:   # If the current list isn’t empty
            heapq.heappush(heap, (lst[0], i, 0))  # Add its first element, list index, and position (0) to the heap
    result = []   # Create an empty list to store the merged result
    while heap:   # While there are elements in the heap
        val, list_idx, elem_idx = heapq.heappop(heap)  # Pop the smallest element (value, list index, position)
        result.append(val)  # Add this smallest value to the result
        if elem_idx + 1 < len(lists[list_idx]):  # If there’s another element in the same list
            next_val = lists[list_idx][elem_idx + 1]  # Get the next element from that list
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))  # Add it to the heap with updated position
    return result   # Return the fully merged sorted list

# Test the function
# print(merge_k_sorted_lists([[1, 3], [2, 4]]))  # Output: [1, 2, 3, 4]


