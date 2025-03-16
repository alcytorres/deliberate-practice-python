# Modified Binary Search


# 1. Search in Rotated Sorted Array (Simple)
"""
Task: Find a target in a rotated sorted array.
Example: [4, 5, 1, 2, 3], target 2 → 3
Why: Introduces rotation concepts.
"""


# Solution
def search_rotated_array(arr, target):
    """
    Finds the target in a rotated sorted array.
    
    - Adapts binary search by checking which half is sorted.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach simplifies understanding of rotation logic.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Test the function
print(search_rotated_array([4, 5, 1, 2, 3], 2))  # Output: 3


# ----------------------------------------------------------------------------------
# 2. Find Minimum in Rotated Array
"""
Task: Find the smallest element in a rotated sorted array.
Example: [3, 4, 5, 1, 2] → 1
Why: Practices finding pivot points.
"""

# Solution
def find_min_in_rotated(arr):
    """
    Finds the smallest element in a rotated sorted array.
    
    - Uses binary search to find the pivot (minimum) point.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative for clarity in finding the unsorted transition.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum is in right half
        else:
            right = mid     # Minimum is in left half or at mid
    return arr[left]

# Test the function
print(find_min_in_rotated([3, 4, 5, 1, 2]))  # Output: 1

# ----------------------------------------------------------------------------------
# 3. Find Peak Element
"""
Task: Find an element larger than its neighbors.
Example: [1, 3, 2] → 3
Why: Applies binary search to unsorted data.
"""


# Solution
def find_peak_element(arr):
    """
    Finds an element greater than its neighbors.
    
    - Uses binary search to find a peak by comparing adjacent elements.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach is straightforward.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Peak is on the right
        else:
            right = mid     # Peak is on the left or at mid
    return arr[left]

# Test the function
print(find_peak_element([1, 3, 2]))  # Output: 3

# ----------------------------------------------------------------------------------
# 4. Count Rotations
"""
Task: Determine how many times a sorted array was rotated.
Example: [3, 4, 5, 1, 2] → 3
Why: Builds intuition for modified conditions.
"""


# Solution
def count_rotations(arr):
    """
    Determines how many times a sorted array was rotated.
    
    - Finds the index of the minimum element using binary search.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative method is clear for beginners.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum (rotation point) is right
        else:
            right = mid     # Minimum is left or at mid
    return left

# Test the function
print(count_rotations([3, 4, 5, 1, 2]))  # Output: 3

# ----------------------------------------------------------------------------------
# 5. Binary Search on Reverse Sorted Array
"""
Task: Adapt binary search for a descending sorted array.
Example: [5, 4, 3, 2, 1], target 3 → 2
Why: Encourages flexibility in binary search logic.
"""


# Solution
def binary_search_reverse_sorted(arr, target):
    """
    Finds the target in a descending sorted array.
    
    - Reverses binary search logic for descending order.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach keeps it simple.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid + 1  # Target is smaller, go right
        else:
            right = mid - 1  # Target is larger, go left
    return -1

# Test the function
print(binary_search_reverse_sorted([5, 4, 3, 2, 1], 3))  # Output: 2


