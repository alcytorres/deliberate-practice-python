# Two Pointers


# 1. Sum of First and Last Elements
# Task: Given an array, return the sum of its first and last elements.
# Example: [1, 2, 3] → 4 (1 + 3)
# Why: Introduces using two pointers at opposite ends.

def sum_first_last(arr):
    if not arr:
        return 0
    first = arr[0]
    last = arr[-1]
    return first + last

# print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)

# Test cases:
# print(sum_first_last([5]))        # Output: 10 (5 + 5)
# print(sum_first_last([]))         # Output: 0 (0 + 0)
# print(sum_first_last([1, 2]))     # Output: 3 (1 + 2)


# Solution
def sum_first_last(arr):
    """
    Returns the sum of the first and last elements of the array.

    - Uses two pointers to access the start and end directly.
    - Time Complexity: O(1), Space Complexity: O(1).
    - Simple and beginner-friendly as it introduces pointer concepts without iteration.
    """
    if not arr:  # Handle empty array case
        return 0
    first = arr[0]          # Pointer to the first element
    last = arr[-1]          # Pointer to the last element (Python allows -1 indexing)
    return first + last

# Test the function
# print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)


# ----------------------------------------------------------------------------------
# 2. Check if Array is Sorted
# Task: Determine if an array is sorted in ascending order.
# Example: [1, 2, 3, 4] → True, [1, 3, 2] → False
# Why: Practices moving pointers to compare adjacent elements.


def is_sorted(arr):
    if len(arr) < 2:
        return True
    i, j = 0, 1  # i points to current, j to next element
    while j < len(arr):
         if arr[i] > arr[j]:  # If current element exceeds next, not sorted
            return False
         i += 1
         j += 1
    return True


# Test the function
print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))     # Output: False



# Solution
def is_sorted(arr):
    """
    Determines if the array is sorted in ascending order.
    
    - Uses two pointers to compare adjacent elements iteratively.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Iterative approach chosen for simplicity over recursive alternatives.
    """

    if len(arr) < 2:  # Arrays with 0 or 1 elements are sorted by definition
        return True
    i, j = 0, 1  # i points to current, j to next element
    while j < len(arr):
        if arr[i] > arr[j]:  # If current element exceeds next, not sorted
            return False
        i += 1  # Move both pointers forward
        j += 1
    return True

# Test the function
print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))     # Output: False


