# Prefix Sum
"""
Foundational Skills
   - Array manipulation
   - Understanding cumulative sums
   - Basic loop structures
Potential Knowledge Gaps
   - Inefficient computation of running sums (e.g., recalculating sums repeatedly)
   - Difficulty applying prefix sums to subarray problems
"""

# ----------------------------------------------------------------------------------
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
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6)]  →  [1, 1+2=3, 1+2+3=6)]


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
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6)]  →  [1, 1+2=3, 1+2+3=6)]


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
prefix = prefix_sum([1, 2, 3])
# print(range_sum(prefix, 0, 1))  # Output: 3 (1 + 2)
# print (range_sum(prefix, 1, 2)) # Output: 5 (6 - 1)


# ----------------------------------------------------------------------------------
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
        prefix_sum += num  # Update running sum
        if prefix_sum == 0 or prefix_sum in seen:
            return True  # Zero sum found
        seen.add(prefix_sum)
    return False

# Test the function
# print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

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
    prefix_sum = 0      # Initialize prefix sum to zero
    seen = set()        # Create an empty set to store seen prefix sums
    for num in arr:     # Iterate through each element in 'arr'
        prefix_sum += num  # Add the current number to the prefix sum
        if prefix_sum == 0 or prefix_sum in seen:  # If prefix sum is zero or seen before
            return True   # A subarray with sum zero exists
        seen.add(prefix_sum)  # Add the current prefix sum to the set
    return False        # No subarray with sum zero found

# Test the function
# print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

"""
Explnation: 
Imagine you’re adding numbers in a list, step-by-step, and you’re looking for a trick: if at any point your total either hits 0 or matches a total you’ve seen before, you’ve found a chunk of numbers that adds up to 0. That’s what this code does.

The code checks if there’s a piece of the list [4, -4, 1] that adds to 0 (like 4 + -4 = 0). It keeps a running total and uses a “memory box” to remember totals it’s seen. If the total ever becomes 0 or repeats a number from the box, it says “Yes!” (True). If not, it says “No!” (False).
"""


# ----------------------------------------------------------------------------------
# 4. Maximum Subarray Sum of Size K
"""
Task: Find the maximum sum of any subarray of size k.
Example: [1, 2, 3, 4], k=2 → 7 (3 + 4)
Why: Bridges to more complex subarray problems.
"""

def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None
    prefix = prefix_sum(arr)
    max_sum = prefix[k - 1]  # First window sum
    for i in range(k, len(arr)):
        current_sum = prefix[i] - prefix[i - k]  # Sum of current window
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test the function
# print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# Solution
def max_subarray_sum(arr, k):  # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any subarray of size k.
    
    - Uses prefix sums to compute subarray sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(n) for prefix array.
    - Prefix sum approach is simpler than sliding window for beginners here.
    """
    if len(arr) < k:      # If array is shorter than 'k'
        return None       # Cannot form a subarray of size 'k'
    prefix = prefix_sum(arr)      # Compute prefix sum array   [1, 2, 3, 4] → [1, 3, 6, 10)] 
    max_sum = prefix[k - 1]       # Sum of the first k elements
    for i in range(k, len(arr)):  # Slide the window from k to the end
        current_sum = prefix[i] - prefix[i - k]  # Calculate sum of current window
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is larger
    return max_sum      # Return the maximum sum found

# Test the function
# print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)



# ----------------------------------------------------------------------------------
# 5. Partition Array into Equal Sums
"""
Task: Check if an array can be split into two non-empty contiguous parts with equal sums.
Example: [1, 5, 6] → True (1 + 5 = 6)
Why: Reinforces cumulative sum usage.
"""

def can_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False  # Odd sum can't be split evenly
    target = total_sum // 2
    prefix_sum = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum == target:
            return True  # Found a split point
    return False

# Test the function
print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)


# Solution
def can_partition(arr):    # Define the function that takes an array 'arr' as input
    """
    Checks if the array can be split into two parts with equal sums.
    
    - Uses prefix sum to find a point where left sum equals remaining sum.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Iterative check is straightforward and beginner-friendly.
    """
    total_sum = sum(arr)     # Calculate the total sum of the array
    if total_sum % 2 != 0:   # If total sum is odd
        return False         # Cannot split into two equal integer sums
    target = total_sum // 2  # Each part should sum to half of total_sum
    prefix_sum = 0      # Initialize prefix sum to zero
    for num in arr:     # Iterate through each element in 'arr'
        prefix_sum += num  # Add the current number to the prefix sum
        if prefix_sum == target:  # If prefix sum equals the target
            return True   # A split point is found
    return False          # No split point found

# Test the function
# print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)


