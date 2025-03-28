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
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]


# Solution
def prefix_sum(arr):
    """
    Computes the prefix sum array where each element is the sum of all prior elements.
    
    - Builds array iteratively, adding each element to the previous sum.
    - Time Complexity: O(n), Space Complexity: O(n) for the result.
    - Simple iteration is beginner-friendly and efficient.
    """
    if not arr:
        return []
    result = [arr[0]]  # First element is the same
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum
    return result

# Test the function
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]


# ----------------------------------------------------------------------------------
# 2. Range Sum Query
"""
Task: Find the sum of elements between two indices using prefix sums.
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


# Solution
def range_sum(prefix, start, end):
    """
    Computes the sum of elements between start and end indices using prefix sums.
    
    - Uses subtraction of prefix sums for efficiency.
    - Time Complexity: O(1) per query, Space Complexity: O(1).
    - Direct calculation is simple and showcases prefix sum utility.
    """
    if start == 0:
        return prefix[end]  # Sum from start of array
    return prefix[end] - prefix[start - 1]  # Difference gives range sum

# Test the function
prefix = prefix_sum([1, 2, 3])
# print(range_sum(prefix, 0, 1))  # Output: 3 (1 + 2)


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


# Solution
def has_zero_sum_subarray(arr):
    """
    Determines if there exists a subarray with sum zero.
    
    - Tracks prefix sums in a set; a repeat or zero indicates a zero-sum subarray.
    - Time Complexity: O(n), Space Complexity: O(n) for the set.
    - Set-based approach is intuitive for beginners and efficient.
    """
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
def max_subarray_sum(arr, k):
    """
    Finds the maximum sum of any subarray of size k.
    
    - Uses prefix sums to compute subarray sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(n) for prefix array.
    - Prefix sum approach is simpler than sliding window for beginners here.
    """
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



# ----------------------------------------------------------------------------------
# 5. Partition Array into Equal Sums
"""
Task: Check if an array can be split into two parts with equal sums.
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
# print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)


# Solution
def can_partition(arr):
    """
    Checks if the array can be split into two parts with equal sums.
    
    - Uses prefix sum to find a point where left sum equals remaining sum.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Iterative check is straightforward and beginner-friendly.
    """
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
# print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)
