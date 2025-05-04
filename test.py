# 1. Compute Prefix Sum Array
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

# ----------------------------------------------------------------------------------
# 1. Compute Prefix Sum Array
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
Why: Direct practice for Running Sum of 1d Array.
"""

def prefix_sum(arr):   # Define the function that takes an array 'arr' as input
    if not arr:         # Check if the array is empty
        return []       # Return an empty array if input is empty
    result = [arr[0]]   # Start the result with the first element of 'arr'
    for i in range(1, len(arr)):  # Loop from the second element to the end
        result.append(result[-1] + arr[i])  # Add the previous sum to the current element
    return result       # Return the prefix sum array

# Test the function
print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6)]  →  [1, 1+2=3, 1+2+3=6)]
print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10)]  →  [1, 1+2=3, 1+2+3=6 1+3+6=10)]


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
    """
# If array is shorter than 'k'
# Cannot form a subarray of size 'k'
# Compute prefix sum array    [1, 2, 3, 4] → [1, 3, 6, 10)] 
# Sum of the first k elements 
# Slide the window from k to the end
# Calculate sum of current window
# Update max_sum if current_sum is larger
# Return the maximum sum found

# Test the function
print(max_subarray_sum([1, 2, 30, 4], 2))  # Output: 7 (3 + 4)




"""
Walkthrough of print(max_subarray_sum([1, 2, 3, 4], 2))
Let’s go through exactly what happens with [1, 2, 3, 4] and k=2, step-by-step, like we’re doing it by hand.

Start:
arr = [1, 2, 3, 4], k = 2.
Check Length:
if len(arr) < k: → len([1, 2, 3, 4]) = 4, k = 2. Is 4 < 2? No.
Skip return None and keep going.
Get Prefix Sums:
prefix = prefix_sum(arr) → Assume prefix_sum gives [1, 3, 6, 10]:
prefix[0] = 1 (just 1).
prefix[1] = 1 + 2 = 3.
prefix[2] = 1 + 2 + 3 = 6.
prefix[3] = 1 + 2 + 3 + 4 = 10.
First Chunk Sum:
max_sum = prefix[k - 1] → k = 2, k - 1 = 1, so prefix[1] = 3.
max_sum = 3 (sum of first 2 numbers: [1, 2]).
Think: Our best sum so far is 1 + 2 = 3.
Loop Through Other Chunks:
for i in range(k, len(arr)): → k = 2, len(arr) = 4, so range(2, 4) gives i = 2, 3.
When i = 2:
current_sum = prefix[i] - prefix[i - k] → i = 2, i - k = 2 - 2 = 0.
prefix[2] = 6, prefix[0] = 1.
current_sum = 6 - 1 = 5 (sum of [2, 3]).
max_sum = max(max_sum, current_sum) → max(3, 5) = 5.
Now max_sum = 5.
Think: Checked 2 + 3 = 5. It’s bigger than 3, so 5 is our new best.
When i = 3:
current_sum = prefix[i] - prefix[i - k] → i = 3, i - k = 3 - 2 = 1.
prefix[3] = 10, prefix[1] = 3.
current_sum = 10 - 3 = 7 (sum of [3, 4]).
max_sum = max(max_sum, current_sum) → max(5, 7) = 7.
Now max_sum = 7.
Think: Checked 3 + 4 = 7. It’s bigger than 5, so 7 is our new best.
Finish:
Loop ends (no more i values).
return max_sum → max_sum = 7.
Output:
print(max_subarray_sum([1, 2, 3, 4], 2)) → 7.
Why: The chunk [3, 4] gives the biggest sum of 2 numbers in a row (3 + 4 = 7).
"""