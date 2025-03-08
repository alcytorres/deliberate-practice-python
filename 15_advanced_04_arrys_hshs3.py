# Convert data from one data type into another


# 1. Convert an array of arrays into a hash.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.

nums = [[1, 3], [8, 9], [2, 16]]
#         {1 => 3, 8 => 9, 2 => 16}
result = {}

i = 0
while i < len(nums):
    key = nums[i][0]
    value = nums[i][1]
    result[key] = value
    i += 1

# print(result)


# Solution 




# 2. Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash.
#    For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.

items = [{ "id": 1, "color": "blue", "price": 32 }, { "id": 2, "color": "red", "price": 12 }]
#        {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}
result = {}

i = 0
while i < len(items):
    item = items[i]
    key = item["id"]
    result[key] = item
    i += 1

# print(result)



# Solution 






# 3. Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
#    For example, "bookkeeper" becomes {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}.

word = "bookkeeper"
#      {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}
result = {}

i = 0
while i < len(word):
    letter = word[i]
    if letter not in result:
        result[letter] = 0
    result[letter] += 1
    i += 1

# print(result)


# Solution 



# 4. Convert a hash into an array of arrays.
#    For example, {"chair" => 100, "book" => 14} becomes [["chair", 100], ["book", 14]].

items = { "chair": 100, "book": 14 }
#       [["chair", 100], ["book", 14]]
result = []

for name in items:
    result.append([name, items[name]])
# print(result)



# Solution
# items = {"chair": 100, "book": 14}    # Dictionary with items and prices
# #       [["chair", 100], ["book", 14]]
# result = []                           

# for name in items:                     # Loop over each key in the dictionary
#     result.append([name, items[name]]) # Add [key, value] pair to result
# print(result)                          # Print the final list of pairs


# IMPORTANT
# for name items: Grabs each key ("chair", then "book") directly from the dictionary. 
# In Python, looping over a dictionary gives you its keys.



# Solution
# items = {"chair": 100, "book": 14}
# result = []

# # Get all keys as a list to loop over
# keys = list(items.keys())
# i = 0

# while i < len(keys):
#     key = keys[i]               # Get the current key (e.g., "chair")
#     value = items[key]          # Get the matching value (e.g., 100)
#     result.append([key, value]) # Add them as a small list to result
#     i += 1

# print(result)  # Output: [["chair", 100], ["book", 14]]


# 5. Convert a hash into an array of hashes using the keys from each hash as the :id key in each of the array's hashes.
#    For example, {321 => {name: "Alice", age: 31}, 322 => {name: "Maria", age: 27}} becomes [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].

persons = { 321: { "name": "Alice", "age": 31 }, 322: { "name": "Maria", "age": 27 } }
#         [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}]
result = []

for id in persons:
    person = persons[id]
    person["id"] = id
    result.append(person)
    
# print(result)



# Solution
# persons = { 321: { "name": "Alice", "age": 31 }, 322: { "name": "Maria", "age": 27 } }  # Dictionary with IDs as keys, person info as values
# #         [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}]
# result = []                         # Empty list to store the new dictionaries

# for id in persons:             # Loop over each key (ID) in the dictionary
#     person = persons[id]       # Get the inner dictionary for the current ID
#     person["id"] = id          # Add the "id" key with the original key’s value
#     result.append(person)      # Add the updated dictionary to the result list

# print(result)                  # Print the final list of dictionaries



# 6. Convert an array of strings into a hash with keys for each string in the array and values for the number of times the string appears in the array.
#    For example, ["do", "or", "do", "not"] becomes {"do" => 2, "or" => 1, "not" => 1}.

strings = ["do", "or", "do", "not"]
#         {"do" => 2, "or" => 1, "not" => 1}
# strings_hash =


# p strings_hash



# Solution



# 7. Convert a hash into a flat array containing all the hash’s keys and values.
#    For example, {"a" => 1, "b" => 2, "c" => 3, "d" => 4} becomes ["a", 1, "b", 2, "c", 3, "d", 4].

hash = { "a": 1, "b": 2, "c": 3, "d": 4 }
#      ["a", 1, "b", 2, "c", 3, "d", 4]
# flattened_array =


# p flattened_array




# Solution




# 8. Combine data from a hash with names and prices and an array of hashes with names, colors, and weights to make a new hash.
#    For example, {"chair" => 75, "book" => 15} and [{name: "chair", color: "red", weight: 10}, {name: "book", color: "black", weight: 1}] becomes {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}.

price_hash = { "chair": 75, "book": 15 }
items = [{ "name": "chair", "color": "red", "weight": 10 }, { "name": "book", "color": "black", "weight": 1 }]
#        {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}
# combined_hash =


# p combined_hash





# Solution





# 9. Convert an array of hashes into a hash of arrays, using the author as keys and the titles as values.
#    For example, [{author: "Jeff Smith", title: "Bone"}, {author: "George Orwell", title: "1984"}, {author: "Jeff Smith", title: "RASL"}] becomes {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}.

books = [{ "author": "Jeff Smith", "title": "Bone" }, { "author": "George Orwell", "title": "1984" }, { "author": "Jeff Smith", "title": "RASL" }]
#       {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}
# books_hash =


# p books_hash





# Solution





# 10. Given a hash, create a new hash that has the keys and values switched.
#     For example, {"a" => 1, "b" => 2, "c" => 3} becomes {1 => "a", 2 => "b", 3 => "c"}.

original_hash = { "a": 1, "b": 2, "c": 3 }
#               {1 => "a", 2 => "b", 3 => "c"}
# flipped_hash =

# p flipped_hash






# Solution


