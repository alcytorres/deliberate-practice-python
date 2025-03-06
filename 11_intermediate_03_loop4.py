# Reduce an array to a single value based on some computation


# 1. Start with an array of numbers and compute the sum of all the numbers.
#    For example, [5, 10, 8, 3] becomes 26.

nums =  [5, 10, 8, 3]
#          26
total = 0
i = 0

while i < len(nums):
    total += nums[i]
    i += 1
# print(total)


# 2. Start with an array of strings and combine them all into a single string.
#    For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

sports = ["volleyball", "basketball", "badminton"]
#         "volleyballbasketballbadminton"
combined_string = ""
i = 0

while i < len(sports):
    combined_string += sports[i]
    i += 1
# print(combined_string)


# 3. Start with an array of hashes and compute the sum of the prices (from the :price key).
#    For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
#       105
total = 0
i = 0

while i < len(items):
    item = items[i]
    total += item["price"]
    i += 1
# print(total)


# 4. Start with an array of numbers and compute the the minimum number.
#    For example, [5, 10, 8, 3, 9] becomes 3.

nums = [5, 10, 8, 3, 9]
#         3
min_num = nums[0]
i = 0

while i < len(nums):
    if nums[i] < min_num:
        min_num = nums[i]
    i += 1
# print(min_num)


# 5. Start with an array of strings and compute the total length of all the strings.
#    For example, ["volleyball", "basketball", "badminton"] becomes 29.

sports = ["volleyball", "basketball", "badminton"]
#        29
string_length = 0
i = 0

while i < len(sports):
    string_length += len(sports[i])
    i += 1
# print(string_length)


# 6. Start with an array of hashes and find the hash with the lowest price (from the :price key).
#    For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.
# (REDO)

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
#       {name: "pencil", price: 1}
cheapest_items = items[0]
i = 0

while i < len(items):
    item = items[i]
    if item["price"] < cheapest_items["price"]:
        cheapest_items = item
    i += 1
# print(cheapest_items)


# 7. Start with an array of numbers and compute product of all the numbers.
#    For example, [5, 10, 8, 3] becomes 1200.

nums = [5, 10, 8, 3]
#      1200
product = 1
i = 0

while i < len(nums):
    product *= nums[i]
    i += 1
# print(product)


#  8. Start with an array of strings and combine them all into a single string, separated by dashes.
#     For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

sports = ["volleyball", "basketball", "badminton"]
#        "-volleyball-basketball-badminton-"
string = "-"
i = 0

while i < len(sports):
    string += sports[i] + "-"
    i += 1
# print(string)


# Solution using f-string (short for "formatted string")
# sports = ["volleyball", "basketball", "badminton"]
# #        "-volleyball-basketball-badminton-"
# string = "-"
# i = 0

# while i < len(sports):
#     string += f"{sports[i]}-"
#     i += 1
# print(string)


# 9. Start with an array of hashes and find the hash with the shortest name (from the :name key).
#    For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
#       {name: "book", price: 4}
shortest_name = items[0]
i = 0

while i < len(items):
    item = items[i]
    if len(item["name"]) < len(shortest_name["name"]):
        shortest_name = item
    i += 1
# print(shortest_name)


# 10. Start with an array of numbers and compute the maximum number.
#     For example, [5, 10, 8, 3] becomes 10.

nums = [5, 10, 8, 3]
#         10
max_number = nums[0]
i = 0

while i < len(nums):
    if nums[i] > max_number:
        max_number = nums[i]
    i += 1
# print(max_number)
