# Binary Search


# 1. Basic Binary Search
"""
Task: Find the index of a target in a sorted array or return -1.
Example: [1, 2, 3, 4], target 3 → 2
Why: Core practice for Binary Search.
"""

# Solution
def binary_search(arr, target):
    """
    Finds the index of the target in a sorted array or returns -1.
    
    - Uses binary search to halve the search space each step.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach is more beginner-friendly than recursive.
    """
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
print(binary_search([1, 2, 3, 4], 3))  # Output: 2

# ----------------------------------------------------------------------------------
# 2. Find First Occurrence
"""
Task: Find the first occurrence of a target in a sorted array with duplicates.
Example: [1, 2, 2, 3], target 2 → 1
Why: Introduces binary search variations.
"""

# Solution
def find_first_occurrence(arr, target):
    """
    Finds the first occurrence of the target in a sorted array with duplicates.
    
    - Modifies binary search to continue left when target is found.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach keeps it simple.
    """
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
print(find_first_occurrence([1, 2, 2, 3], 2))  # Output: 1


# ----------------------------------------------------------------------------------
# 3. Find Last Occurrence
"""
Task: Find the last occurrence of a target in a sorted array with duplicates.
Example: [1, 2, 2, 3], target 2 → 2
Why: Reinforces boundary handling.
"""

# Solution
def find_last_occurrence(arr, target):
    """
    Finds the last occurrence of the target in a sorted array with duplicates.
    
    - Modifies binary search to continue right when target is found.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative for simplicity.
    """
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
print(find_last_occurrence([1, 2, 2, 3], 2))  # Output: 2

# ----------------------------------------------------------------------------------
# 4. Next Greater Element
"""
Task: Find the smallest element greater than the target.
Example: [1, 3, 5], target 2 → 3
Why: Prepares for real-world binary search tweaks.
"""

# Solution
def next_greater_element(arr, target):
    """
    Finds the smallest element greater than the target.
    
    - Uses binary search to find the insertion point.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative approach is clear and efficient.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1  # Move to right half
        else:
            right = mid     # Potential answer, but check left
    return arr[left] if left < len(arr) and arr[left] > target else None

# Test the function
print(next_greater_element([1, 3, 5], 2))  # Output: 3


# ----------------------------------------------------------------------------------
# 5. Square Root Estimation
"""
Task: Find the integer square root of a number using binary search.
Example: 16 → 4
Why: Applies binary search to a different domain."
"""

# Solution
def integer_square_root(n):
    """
    Finds the largest integer whose square is less than or equal to n.
    
    - Uses binary search to efficiently estimate square root.
    - Time Complexity: O(log n), Space Complexity: O(1).
    - Iterative method is beginner-friendly and avoids floating-point issues.
    """
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
print(integer_square_root(16))  # Output: 4


