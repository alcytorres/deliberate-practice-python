"""
# Task: Given an array, return the sum of its first and last elements.
# Example: [1, 2, 3] → 4 (1 + 3)
# Why: Introduces using two pointers at opposite ends.
"""

def sum_first_last(arr):
    if not arr:
        return 0
    first = arr[0]
    last = arr[-1]
    return first + last

#test
print(sum_first_last([1, 2, 3]))


