# Select items from an array into a new array with items that match a certain condition


# 1. Start with an array of numbers and create a new array with only the numbers less than 20.
#    For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

nums = [2, 32, 80, 18, 12, 3]
#      [2, 18, 12, 3]
result = []
i = 0

while i < len(nums):
    number = nums[i]
    if number < 20:
        result.append(number)
    i += 1                      # WARNING --> Be careful with indentation 
# print(result)


# 2. Start with an array of strings and create a new array with only the strings that start with the letter "w".
#    For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

strings = ["winner", "winner", "chicken", "dinner"]
#         ["winner", "winner"]
result = []
i = 0

while i < len(strings):
    string = strings[i]
    if string[0] == "w":
        result.append(string)
    i += 1
# print(result)


# 3. Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key).
#    For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
#       [{name: "chair", price: 100}]
result = []
i = 0

while i < len(items):
    item = items[i]
    if item["price"] > 5:
        result.append(item)
    i += 1
# print(result)


# 4. Start with an array of numbers and create a new array with only the even numbers.
#    For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].

nums = [2, 4, 5, 1, 8, 9, 7]
#         [2, 4, 8]
result = []
i = 0

while i < len(nums):
    number = nums[i]
    if number % 2 == 0:
        result.append(number)
    i += 1 
# print(result)


# 5. Start with an array of strings and create a new array with only the strings shorter than 4 letters.
#    For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].

strings = ["a", "man", "a", "plan", "a", "canal", "panama"]
#         ["a", "man", "a", "a"]
result = []
i = 0

while i < len(strings):
    string = strings[i]
    if len(string) < 4:
        result.append(string)
    i += 1
# print(result)


# 6. Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
#    For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
#        [{name: "chair", price: 100}, {name: "book", price: 4}]
result = []
i = 0

while i < len(items):
    item = items[i]
    if len(item["name"]) < 6:
        result.append(item)
    i += 1
# print(result)


# 7. Start with an array of numbers and create a new array with only the numbers less than 10.
#    For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

nums = [8, 23, 0, 44, 1980, 3]
#         [8, 0, 3]
result = []
i = 0

while i < len(nums):
    number = nums[i]
    if number < 10:
        result.append(number)
    i += 1
# print(result)



# 8. Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
#    For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

strings = ["big", "little", "good", "bad"]
#         ["little", "good"]
result = []
i = 0

while i < len(strings):
    string = strings[i]
    if string[0] != "b":
        result.append(string)
    i += 1
# print(result)


# 9. Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key).
#    For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
#       [{name: "pencil", price: 1}, {name: "book", price: 4}]
result = []
i = 0

while i < len(items):
    item = items[i]
    if item["price"] < 10:
        result.append(item)
    i += 1
# print(result)


# 10. Start with an array of numbers and create a new array with only the odd numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

nums = [2, 4, 5, 1, 8, 9, 7]
#      [5, 1, 9, 7]
result = []
i = 0

while i < len(nums):
    number = nums[i]
    if number % 2 == 1:
        result.append(number)
    i += 1
# print(result)
