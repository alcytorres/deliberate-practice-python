# 1. Compute Prefix Sum Array
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]  # First element is the same
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum
    return result

# Test the function
# print(prefix_sum([1, 2, 3]))  # Output: [1, 1+2=3, 1+2+3=6)]


# Solution
def prefix_sum(arr):   # Define the function that takes an array 'arr' as input
    """
    Computes the prefix sum array where each element is the sum of all prior elements.
    
    - Builds array iteratively, adding each element to the previous sum.
    - Time Complexity: O(n), Space Complexity: O(n) for the result.
    - Simple iteration is beginner-friendly and efficient.
    """
    if not arr:         # Check if the array is empty
        return []       # Return an empty array if input is empty
    result = [arr[0]]   # Start the result with the first element of 'arr'
    for i in range(1, len(arr)):  # Loop from the second element to the end
        result.append(result[-1] + arr[i])  # Add the previous sum to the current element
    return result       # Return the prefix sum array

# Test the function
# print(prefix_sum([1, 2, 3]))  # Output: [1, 1+2=3, 1+2+3=6)]


# result = [1],  range(1, 3)  i = 1   result = (1 + 2 = 3)  --> result = [1, 3]
# result = [1, 3],  range(2, 3)  i = 2  result = (3 + 3 = 6) --> result = [1, 3, 6]
# return [1, 3, 6]






# 2. Range Sum Query
"""
Task: Find the sum of elements between two indices (inclusive) using prefix sums.
Example: [1, 2, 3], indices 0 to 1 → 3 (1 + 2)
Why: Teaches efficient range sum calculation.
"""

def range_sum(prefix, start, end):
    if start == 0:
        return prefix[end]  # Sum from start of array
    return prefix[end] - prefix[start - 1]  # Difference gives range sum

# Test the function
prefix = prefix_sum([1, 2, 3])
# print(range_sum(prefix, 0, 1))  # Output: 3 (1 + 2) 
# print (range_sum(prefix, 1, 2)) # Output: 5 (6 - 1)


# Solution
def range_sum(prefix, start, end):   # Define the function that takes a prefix sum array and two indices
    """
    Computes the sum of elements between start and end indices using prefix sums.
    
    - Uses subtraction of prefix sums for efficiency.
    - Time Complexity: O(1) per query, Space Complexity: O(1).
    - Direct calculation is simple and showcases prefix sum utility.
    """
    if start == 0:      # If starting from the beginning
        return prefix[end]  # Directly return the prefix sum at 'end'
    return prefix[end] - prefix[start - 1]  # Subtract prefix sum before 'start' from prefix sum at 'end'

# Test the function
prefix = prefix_sum([1, 2, 3])  # Output: [1, 3, 6]
print(range_sum(prefix, 0, 1))  # Output: 3 (1 + 2)
print (range_sum(prefix, 1, 2)) # Output: 5 (6 - 1)

