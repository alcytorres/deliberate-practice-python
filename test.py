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
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6)]  --> [1, 1+2=3, 1+2+3=6)]


# ----------------------------------------------------------------------------------
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
prefix = prefix_sum([1, 2, 3])  # Output: prefix = [1, 3, 6]
# print(range_sum(prefix, 0, 1))  # Output: 3  (1 + 2) 
# print (range_sum(prefix, 1, 2)) # Output: 5  (6 - 1)

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
# print(range_sum(prefix, 0, 1))  # Output: 3  (1 + 2)
# print (range_sum(prefix, 1, 2)) # Output: 5  (6 - 1)






# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero.
Example: [4, -4, 1] → True 
Why: Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)
    return False

# Test the function
print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)


# Solution
def has_zero_sum_subarray(arr):    # Define the function that takes an array 'arr' as input
    """
    Determines if there exists a subarray with sum zero.
    
    - Tracks prefix sums in a set; a repeat or zero indicates a zero-sum subarray.
    - Time Complexity: O(n), Space Complexity: O(n) for the set.
    - Set-based approach is intuitive for beginners and efficient.
    """
# Initialize prefix sum to zero
# Create an empty set to store seen prefix sums
# Iterate through each element in 'arr'
# Add the current number to the prefix sum
# If prefix sum is zero or seen before
# A subarray with sum zero exists
# Add the current prefix sum to the set
# No subarray with sum zero found

# Test the function
# print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

