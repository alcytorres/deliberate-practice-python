# Modified Binary Search
"""
Foundational Skills
   - Standard binary search
   - Understanding array rotations or non-standard conditions
Potential Knowledge Gaps
   - Adapting binary search to rotated or unsorted-like arrays
   - Identifying when a modified approach is needed
"""

# ----------------------------------------------------------------------------------
# 1. Search in Rotated Sorted Array (Simple)
"""
Task: Find a target in a rotated sorted array (e.g., a sorted array shifted circularly).
Example: [4, 5, 1, 2, 3], target 2 → 3
Why: Introduces rotation concepts.
"""

def search_rotated_array(arr, target):
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
# print(search_rotated_array([4, 5, 1, 2, 3], 2))  # Output: 3


# Solution
def search_rotated_array(arr, target):   # Define the function that takes a rotated sorted array 'arr' and a target
    """
    Finds the target in a rotated sorted array.
    
    - Adapts binary search by checking which half is sorted.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach simplifies understanding of rotation logic.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    while left <= right:            # Continue searching while the search space is valid (left doesn’t cross right)
        mid = (left + right) // 2   # Calculate the middle index using integer division
        if arr[mid] == target:      # If the middle element is the target we’re looking for
            return mid              # Return its index right away
        if arr[left] <= arr[mid]:   # Check if the left half (from left to mid) is sorted
            if arr[left] <= target < arr[mid]:  # If target lies within the sorted left half’s range
                right = mid - 1     # Narrow the search to the left half by moving 'right'
            else:                   # If target isn’t in the left half
                left = mid + 1      # Move 'left' to search the right half
        else:                       # If the left half isn’t sorted, the right half (mid to right) must be
            if arr[mid] < target <= arr[right]:  # If target lies within the sorted right half’s range
                left = mid + 1      # Narrow the search to the right half by moving 'left'
            else:                   # If target isn’t in the right half
                right = mid - 1     # Move 'right' to search the left half
    return -1                       # If the loop ends, target isn’t in the array, so return -1

# Test the function
# print(search_rotated_array([4, 5, 1, 2, 3], 2))  # Output: 3


# ----------------------------------------------------------------------------------
# 2. Find Minimum in Rotated Array
"""
Task: Find the smallest element in a rotated sorted array.
Example: [3, 4, 5, 1, 2] → 1
Why: Practices finding pivot points.
"""

def find_min_in_rotated(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum is in right half
        else:
            right = mid     # Minimum is in left half or at mid
    return arr[left]

# Test the function
# print(find_min_in_rotated([3, 4, 5, 1, 2]))  # Output: 1


# Solution
def find_min_in_rotated(arr):   # Define the function that takes a rotated sorted array 'arr'
    """
    Finds the smallest element in a rotated sorted array.
    
    - Uses binary search to find the pivot (minimum) point.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative for clarity in finding the unsorted transition.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    while left < right:             # Continue until 'left' and 'right' meet (no need for = since we want the min)
        mid = (left + right) // 2   # Calculate the middle index
        if arr[mid] > arr[right]:   # If middle element is greater than the rightmost element
            left = mid + 1          # Minimum must be in the right half (after mid), so move 'left'
        else:                       # If middle element is less than or equal to the rightmost
            right = mid             # Minimum is in the left half or at mid, so move 'right' to mid
    return arr[left]                # When 'left' equals 'right', it points to the smallest element

# Test the function
# print(find_min_in_rotated([3, 4, 5, 1, 2]))  # Output: 1


# ----------------------------------------------------------------------------------
# 3. Find Peak Element
"""
Task: Find an element larger than its neighbors.
Example: [1, 3, 2] → 3
Why: Applies binary search to unsorted data.
"""

def find_peak_element(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Peak is on the right
        else:
            right = mid     # Peak is on the left or at mid
    return arr[left]

# Test the function
# print(find_peak_element([1, 3, 2]))  # Output: 3


# Solution
def find_peak_element(arr):   # Define the function that takes an array 'arr'
    """
    Finds an element greater than its neighbors.
    
    - Uses binary search to find a peak by comparing adjacent elements.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach is straightforward.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    while left < right:             # Continue until 'left' and 'right' meet (peak will be found)
        mid = (left + right) // 2   # Calculate the middle index
        if arr[mid] < arr[mid + 1]: # If the next element is greater than the middle element
            left = mid + 1          # Peak must be on the right side, so move 'left'
        else:                       # If the middle element is greater than or equal to the next
            right = mid             # Peak is on the left side or at mid, so move 'right'
    return arr[left]                # When 'left' equals 'right', it’s a peak element

# Test the function
# print(find_peak_element([1, 3, 2]))  # Output: 3


# ----------------------------------------------------------------------------------
# 4. Count Rotations
"""
Task: Find how many positions the smallest element of a sorted array has shifted from the start due to rotation.
Example: [3, 4, 5, 1, 2] → 3
Why: Builds intuition for modified conditions.
"""

def count_rotations(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum (rotation point) is right
        else:
            right = mid     # Minimum is left or at mid
    return left

# Test the function
# print(count_rotations([3, 4, 5, 1, 2]))  # Output: 3


# Solution
def count_rotations(arr):   # Define the function that takes a rotated sorted array 'arr'
    """
    Determines how many times a sorted array was rotated.
    
    - Finds the index of the minimum element using binary search.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative method is clear for beginners.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    while left < right:             # Continue until 'left' and 'right' meet
        mid = (left + right) // 2   # Calculate the middle index
        if arr[mid] > arr[right]:   # If middle element is greater than the rightmost element
            left = mid + 1          # Rotation point (minimum) is in the right half, so move 'left'
        else:                       # If middle element is less than or equal to the rightmost
            right = mid             # Rotation point is in the left half or at mid, so move 'right'
    return left                     # The index of the minimum element is the number of rotations

# Test the function
# print(count_rotations([3, 4, 5, 1, 2]))  # Output: 3


# ----------------------------------------------------------------------------------
# 5. Binary Search on Reverse Sorted Array
"""
Task: Modify binary search to find a target in a descending sorted array.
Example: [5, 4, 3, 2, 1], target 3 → 2
Why: Encourages flexibility in binary search logic.
"""

def binary_search_reverse_sorted(arr, target):
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
# print(binary_search_reverse_sorted([5, 4, 3, 2, 1], 3))  # Output: 2


# Solution
def binary_search_reverse_sorted(arr, target):   # Define the function that takes a reverse sorted array 'arr' and a target
    """
    Finds the target in a descending sorted array.
    
    - Reverses binary search logic for descending order.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach keeps it simple.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    while left <= right:            # Continue searching while the search space is valid
        mid = (left + right) // 2   # Calculate the middle index
        if arr[mid] == target:      # If the middle element is the target
            return mid              # Return its index immediately
        elif arr[mid] > target:     # If middle element is greater than the target (in descending order)
            left = mid + 1          # Target is smaller, so move 'left' to search the right half
        else:                       # If middle element is less than the target
            right = mid - 1         # Target is larger, so move 'right' to search the left half
    return -1                       # Return -1 if the target isn’t found in the array

# Test the function
# print(binary_search_reverse_sorted([5, 4, 3, 2, 1], 3))  # Output: 2

