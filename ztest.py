# 1. Sum of First and Last Elements
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


print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)

# Test cases:
print(sum_first_last([5]))        # Output: 10 (5 + 5)
print(sum_first_last([]))         # Output: 0 (0 + 0)
print(sum_first_last([1, 2]))     # Output: 3 (1 + 2)





# 1. Sum of First and Last Elements
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

# print(sum_first_last([1, 2, 3]))  # Output: 4 (1 + 3)

# Test cases:
# print(sum_first_last([5]))        # Output: 10 (5 + 5)
# print(sum_first_last([]))         # Output: 0 (0 + 0)
# print(sum_first_last([1, 2]))     # Output: 3 (1 + 2)


