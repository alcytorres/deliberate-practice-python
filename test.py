# a = [1, 2]
# a.extend([3, 4])  # Adds 3 and 4 individually
# print(a)  # Output: [1, 2, 3, 4]

# a.extend((5, 6))  # Works with tuples too
# print(a)  # Output: [1, 2, 3, 4, 5, 6]

# a = [1, 2]
# a.append([3, 4])  # Adds [3, 4] as a single item
# print(a)  # Output: [1, 2, [3, 4]]



fruits = ["apple", "banana"]
more_fruits = ["orange", "grape"]
fruits.extend(more_fruits)
print(fruits)  # Output: ["apple", "banana", "orange", "grape"]



fruits = ["apple", "banana"]
more_fruits = ["orange", "grape"]
fruits.append(more_fruits)
print(fruits)  # Output: ["apple", "banana", "orange", "grape"]