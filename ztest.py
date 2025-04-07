# ----------------------------------------------------------------------------------
# 4. Find Pair with Target Difference
"""
Task: Find two numbers in an array whose difference is a given target. The larger number minus the smaller should equal the target.
Example: [1, 3, 5, 8], target = 2 → [1, 3]
Why: Prepares for Two Sum by practicing pointer movement for a condition.
"""

def find_pair_with_difference(arr, target):
    arr.sort()  
    left, right = 0, 1
    while right < len(arr):
        difference = arr[right] - arr[left]
        if difference == target:
            return [arr[left], arr[right]]
        elif difference < target:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1
    return None


print(find_pair_with_difference([1, 3, 5, 8], 2))  # Output: [1, 3]
# print(find_pair_with_difference([8, 1, 3, 5], 3))  # Output: [5, 8]
# print(find_pair_with_difference([1, 2, 4], 5))  # Output: None
# print(find_pair_with_difference([1, 5, 6], 2))  # Output: None



# Sort array in ascending order to use two pointers effectively
# Set 'left' to 0 and 'right' to 1 (start with adjacent elements)
# Loop until 'right' reaches the end of the array
# Calculate difference between elements at right and left
# Check if the difference matches the target
# Return the pair if target is found
# If difference is too small
# Move 'right' forward to increase the difference
# If difference is too large
# Move 'left' forward to decrease the difference
# If pointers overlap after moving 'left'
# Move 'right' forward to keep them distinct
# Return None if no pair is found





