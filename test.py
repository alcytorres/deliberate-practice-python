# a = [1, 2]
# a.extend([3, 4])  # Adds 3 and 4 individually
# print(a)  # Output: [1, 2, 3, 4]

# a.extend((5, 6))  # Works with tuples too
# print(a)  # Output: [1, 2, 3, 4, 5, 6]

# a = [1, 2]
# a.append([3, 4])  # Adds [3, 4] as a single item
# print(a)  # Output: [1, 2, [3, 4]]

# fruits = ["apple", "banana"]
# more_fruits = ["orange", "grape"]
# fruits.extend(more_fruits)
# print(fruits)  # Output: ["apple", "banana", "orange", "grape"]


# fruits = ["apple", "banana"]
# more_fruits = ["orange", "grape"]
# fruits.append(more_fruits)
# print(fruits)  # Output: ['apple', 'banana', ['orange', 'grape']]


# range(start, stop)
# What it does: Generates a sequence of numbers from 'start' to 'stop-1'.
# Why use it: Creating loops or sequences for iteration (common in algorithms).
# Syntax:
# range(start, stop)  # Returns a range object; 'start' is inclusive, 'stop' is exclusive
# Example:
print(list(range(1, 4)))  # Output: [1, 2, 3]








