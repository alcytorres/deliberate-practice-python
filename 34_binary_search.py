# Binary Search
"""
Foundational Skills
   - Understanding sorted arrays
   - Loop invariants (e.g., maintaining search bounds)
   - Conditional statements
Potential Knowledge Gaps
   - Misunderstanding loop invariants (e.g., when to include mid)
   - Handling edge cases (e.g., target not present, duplicates)
"""

# ----------------------------------------------------------------------------------
# 1. Basic Binary Search
"""
Task: Find the index of a target in a sorted array or return -1.
Example: [1, 2, 3, 4], target 3 → 2
Why: Core practice for Binary Search.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Integer division for midpoint
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1

# Test the function
# print(binary_search([1, 2, 3, 4], 3))  # Output: 2


# Solution
def binary_search(arr, target):   # Define the function that takes a sorted array 'arr' and a target value
    """
    Finds the index of the target in a sorted array or returns -1.
    
    - Uses binary search to halve the search space each step.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach is more beginner-friendly than recursive.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    while left <= right:            # Continue searching while the search space is valid (left doesn't pass right)
        mid = (left + right) // 2   # Calculate the middle index using integer division
        if arr[mid] == target:      # If the middle element is the target
            return mid              # Return its index immediately
        elif arr[mid] < target:     # If the middle element is less than the target
            left = mid + 1          # Move 'left' to mid + 1 to search the right half
        else:                       # If the middle element is greater than the target
            right = mid - 1         # Move 'right' to mid - 1 to search the left half
    return -1                       # Return -1 if the target isn’t found after the loop ends

# Test the function
# print(binary_search([1, 2, 3, 4], 3))  # Output: 2


# ----------------------------------------------------------------------------------
# 2. Find First Occurrence
"""
Task: Find the first occurrence of a target in a sorted array with duplicates.
Example: [1, 2, 2, 3], target 2 → 1
Why: Introduces binary search variations.
"""

def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid    # Record position but keep searching left
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Test the function
# print(find_first_occurrence([1, 2, 2, 3], 2))  # Output: 1


# Solution
def find_first_occurrence(arr, target):   # Define the function that takes a sorted array 'arr' with duplicates and a target
    """
    Finds the first occurrence of the target in a sorted array with duplicates.
    
    - Modifies binary search to continue left when target is found.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach keeps it simple.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    result = -1                     # Initialize 'result' to -1 (default if target isn’t found)
    while left <= right:            # Continue searching while the search space is valid
        mid = (left + right) // 2   # Calculate the middle index
        if arr[mid] == target:      # If the middle element is the target
            result = mid            # Store this index as a possible answer
            right = mid - 1         # Keep searching the left half for an earlier occurrence
        elif arr[mid] < target:     # If the middle element is less than the target
            left = mid + 1          # Move 'left' to mid + 1 to search the right half
        else:                       # If the middle element is greater than the target
            right = mid - 1         # Move 'right' to mid - 1 to search the left half
    return result                   # Return the earliest index found (or -1 if not found)

# Test the function
# print(find_first_occurrence([1, 2, 2, 3], 2))  # Output: 1


# ----------------------------------------------------------------------------------
# 3. Find Last Occurrence
"""
Task: Find the last occurrence of a target in a sorted array with duplicates.
Example: [1, 2, 2, 3], target 2 → 2
Why: Reinforces boundary handling.
"""

def find_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid   # Record position but keep searching right
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Test the function
# print(find_last_occurrence([1, 2, 2, 3], 2))  # Output: 2


# Solution
def find_last_occurrence(arr, target):   # Define the function that takes a sorted array 'arr' with duplicates and a target
    """
    Finds the last occurrence of the target in a sorted array with duplicates.
    
    - Modifies binary search to continue right when target is found.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative for simplicity.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    result = -1                     # Initialize 'result' to -1 (default if target isn’t found)
    while left <= right:            # Continue searching while the search space is valid
        mid = (left + right) // 2   # Calculate the middle index
        if arr[mid] == target:      # If the middle element is the target
            result = mid            # Store this index as a possible answer
            left = mid + 1          # Keep searching the right half for a later occurrence
        elif arr[mid] < target:     # If the middle element is less than the target
            left = mid + 1          # Move 'left' to mid + 1 to search the right half
        else:                       # If the middle element is greater than the target
            right = mid - 1         # Move 'right' to mid - 1 to search the left half
    return result                   # Return the latest index found (or -1 if not found)

# Test the function
# print(find_last_occurrence([1, 2, 2, 3], 2))  # Output: 2


# ----------------------------------------------------------------------------------
# 4. Next Greater Element
"""
Task: Find the smallest element greater than the target in a sorted array, or return None if no such element exists.
Example: [1, 3, 5], target 2 → 3
Why: Prepares for real-world binary search tweaks.
"""

def next_greater_element(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1  # Move to right half
        else:
            right = mid     # Potential answer, but check left
    return arr[left] if left < len(arr) and arr[left] > target else None

# Test the function
# print(next_greater_element([1, 3, 5], 2))  # Output: 3


# Solution
def next_greater_element(arr, target):   # Define the function that takes a sorted array 'arr' and a target
    """
    Finds the smallest element greater than the target.
    
    - Uses binary search to find the insertion point.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach is clear and efficient.
    """
    left, right = 0, len(arr) - 1   # Set 'left' to the start and 'right' to the end of the array
    while left < right:             # Continue until 'left' meets or exceeds 'right'
        mid = (left + right) // 2   # Calculate the middle index
        if arr[mid] <= target:      # If the middle element is less than or equal to the target
            left = mid + 1          # Move 'left' to mid + 1 to search the right half
        else:                       # If the middle element is greater than the target
            right = mid             # This could be the answer, but check the left half for a smaller option
    if left < len(arr) and arr[left] > target:  # Check if 'left' is in bounds and points to a value greater than target
        return arr[left]            # Return the smallest element greater than the target
    return None                     # Return None if no such element exists

# Test the function
# print(next_greater_element([1, 3, 5], 2))  # Output: 3


# ----------------------------------------------------------------------------------
# 5. Square Root Estimation
"""
Task: Find the largest integer whose square is less than or equal to a number using binary search.
Example: 16 → 4
Why: Applies binary search to a different domain."
"""

def integer_square_root(n):
    if n < 0:
        return None
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared == n:
            return mid
        elif mid_squared < n:
            left = mid + 1
        else:
            right = mid - 1
    return right  # Largest integer where square <= n

# Test the function
# print(integer_square_root(16))  # Output: 4


# Solution
def integer_square_root(n):   # Define the function that takes a non-negative integer 'n'
    """
    Finds the largest integer whose square is less than or equal to n.
    
    - Uses binary search to efficiently estimate square root.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative method is beginner-friendly and avoids floating-point issues.
    """
    if n < 0:                 # Check if the input 'n' is negative
        return None           # Return None since square root isn’t defined for negative numbers
    left, right = 0, n        # Set 'left' to 0 and 'right' to 'n' (range where the square root lies)
    while left <= right:      # Continue searching while the search space is valid
        mid = (left + right) // 2  # Calculate the middle value
        mid_squared = mid * mid    # Compute the square of 'mid'
        if mid_squared == n:       # If the square matches 'n' exactly
            return mid             # Return 'mid' as the exact square root
        elif mid_squared < n:      # If the square is less than 'n'
            left = mid + 1         # Move 'left' to mid + 1 to search larger values
        else:                      # If the square is greater than 'n'
            right = mid - 1        # Move 'right' to mid - 1 to search smaller values
    return right                  # Return 'right' as the largest integer whose square is <= 'n'

# Test the function
# print(integer_square_root(16))  # Output: 4

