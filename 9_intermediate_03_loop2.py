# Map an array to a new array with some computation performed on each item


# 1. Start with an array of numbers and create a new array with each number times 3.
#    For example, [1, 2, 3] becomes [3, 6, 9].

nums = [1, 2, 3]
result = []
i = 0

while i < len(nums):
    result.append(nums[i] * 3)
    i += 1
# print(result) 

# Alternative solution with a for loop
nums = [1, 2, 3]
result = []
for number in nums:
    result.append(number * 3)
# print(result)

# Alternative solution using a list comprehension
nums = [1, 2, 3]
result = [number * 3 for number in nums]
# print(result)


# 2. Start with an array of strings and create a new array with each string upcased.
#    For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

strings = ["hello", "goodbye"]
result = []
i = 0

while i < len(strings):
    string = strings[i]
    result.append(string.upper())
    i += 1
# print(result)

# Alternative solution with a for loop
strings = ["hello", "goodbye"]
result = []
for string in strings:
    result.append(string.upper())
# print(result)

# Alternative solution using a list comprehension
strings = ["hello", "goodbye"]
result = [string.upper() for string in strings]
# print(result)


# 3. Start with an array of hashes and create a new array of string values from each hash's :name key.
#    For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
#        ["Alice", "Blane"]
result = []
i = 0

while i < len(people):
    result.append(people[i]["name"])
    i += 1
# print(result)


# 4. Start with an array of numbers and create a new array with each number plus 7.
#    For example, [1, 2, 3] becomes [8, 9, 10].

nums = [1, 2, 3]
#      [8, 9, 10]
result = []
i = 0

while i < len(nums):
    result.append(nums[i] + 7)
    i += 1
# print(result)


# 5. Start with an array of strings and create a new array with each string's length.
#    For example, ["hello", "goodbye"] becomes [5, 7].

words = ["hello", "goodbye"]
#        [5, 7]
result = []
i = 0

while i < len(words):
    result.append(len(words[i]))
    i += 1
# print(result)


# 6. Start with an array of hashes and create a new array of number values from each hash's :age key.
#    For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
#         [27, 16]
result = []
i = 0

while i < len(people):
    person = people[i]
    result.append(person["age"])
    i += 1
# print(result)


# 7. Start with an array of numbers and create a new array with each number divided by 2.
#    For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].

prices = [1, 2, 3]
#        [0.5, 1.0, 1.5]
result = []
i = 0

while i < len(prices):
    result.append(prices[i] / 2.0)
    i += 1
# print(result)


# 8. Start with an array of strings and create a new array with each string's first letter only.
#    For example, ["hello", "goodbye"] becomes ["h", "g"].

words = ["hello", "goodbye"]
#       ["h", "g"]
result = []
i = 0

while i < len(words):
    result.append(words[i][0])
    i += 1
# print(result)


# 9. Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
#    For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

persons = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
#         [54, 32]
result = []
i = 0

while i < len(persons):
    person = persons[i]
    result.append(person["age"] * 2)
    i += 1
# print(result)


# 10. Start with an array of numbers and create a new array with each number converted into a string.
#     For example, [1, 2, 3] becomes ["1", "2", "3"].

nums = [1, 2, 3]
#         ["1", "2", "3"]
result = []
i = 0

while i < len(nums):
    number = nums[i]
    result.append(str(number))
    i += 1
# print(result)
