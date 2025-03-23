# Convert data from one data type into another


# 1. Convert an array of arrays into a hash.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.

nums = [[1, 3], [8, 9], [2, 16]]
#         {1 => 3, 8 => 9, 2 => 16}
result = {}



# print(result)


# Solution 
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



# 2. Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash.
#    For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.

items = [{ "id": 1, "color": "blue", "price": 32 }, { "id": 2, "color": "red", "price": 12 }]
#        {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}
result = {}


# print(result)



# Solution 
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



# 3. Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
#    For example, "bookkeeper" becomes {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}.

word = "bookkeeper"
#      {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}
result = {}


# print(result)


# Solution 
word = "bookkeeper"    # Input string to process
#      {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}
result = {}            # Empty dictionary to store letter counts

i = 0                   # Initialize index to 0 to start at the first character
while i < len(word):    # Loop until i reaches the length of "bookkeeper" (10)
    letter = word[i]    # Get the character at position i (e.g., "b" when i=0)
    if letter not in result:  # If letter isn’t in the dictionary yet
        result[letter] = 0    # Initialize its count to 0
    result[letter] += 1       # Increment the count for this letter
    i += 1                    # Move to the next index

# print(result)  # Output the final dictionary with letter counts



# 4. Convert a hash into an array of arrays.
#    For example, {"chair" => 100, "book" => 14} becomes [["chair", 100], ["book", 14]].

items = { "chair": 100, "book": 14 }
#       [["chair", 100], ["book", 14]]
result = []


# print(result)



# Solution
items = {"chair": 100, "book": 14}    # Dictionary with items and prices
#       [["chair", 100], ["book", 14]]
result = []                           

for key in items:                     # Loop over each key in the dictionary
    result.append([key, items[key]])  # Add [key, value] pair to result
# print(result)                        # Print the final list of pairs


# IMPORTANT
# for name items: Grabs each key ("chair", then "book") directly from the dictionary. 
# ****** In Python, looping over a dictionary gives you its keys. ******



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


# DO THIS PROBLEM

# 5. Convert a hash into an array of hashes using the keys from each hash as the :id key in each of the array's hashes.
#    For example, {321 => {name: "Alice", age: 31}, 322 => {name: "Maria", age: 27}} becomes [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].

persons = { 321: { "name": "Alice", "age": 31 }, 322: { "name": "Maria", "age": 27 } }
#         [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}]
result = []



# print(result)



# A for loop is best here because:
    # Direct Key Access: The loop iterates over the hash’s keys (e.g., 321, 322), providing immediate access to each key (id) without needing manual indexing or counters.
    # Simplicity: It’s concise and readable, naturally pairing each key with its value (persons[id]) for transformation into the desired hash format.

# Solution
persons = { 321: { "name": "Alice", "age": 31 }, 322: { "name": "Maria", "age": 27 } }  # Dictionary with IDs as keys, person info as values
#         [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}]
result = []                         # Empty list to store the new dictionaries

for id in persons:             # Loop over each key (ID) in the dictionary
    person = persons[id]       # Get the inner dictionary for the current ID
    person["id"] = id          # Add the "id" key with the original key’s value
    result.append(person)      # Add the updated dictionary to the result list

# print(result)                 # Print the final list of dictionaries



# 6. Convert an array of strings into a hash with keys for each string in the array and values for the number of times the string appears in the array.
#    For example, ["do", "or", "do", "not"] becomes {"do" => 2, "or" => 1, "not" => 1}.

words = ["do", "or", "do", "not"]
#       {"do" => 2, "or" => 1, "not" => 1}
result = {}



# print(result)


# Solution
words = ["do", "or", "do", "not"]         # List of words to count
#         {"do" => 2, "or" => 1, "not" => 1}
result = {}                               # Empty dictionary to store word counts

i = 0                                     # Index to track position in list
while i < len(words):                     # Loop through all words in the list
    key = words[i]                        # Get the current word
    if key not in result:                 # If word isn’t in dictionary yet
        result[key] = 0                   # Start its count at 0
    result[key] += 1                      # Add 1 to the word’s count
    i += 1                                # Move to the next word

# print(result)                             # Print the final word counts



# 7. Convert a hash into a flat array containing all the hash’s keys and values.
#    For example, {"a" => 1, "b" => 2, "c" => 3, "d" => 4} becomes ["a", 1, "b", 2, "c", 3, "d", 4].

hash = { "a": 1, "b": 2, "c": 3, "d": 4 }
#      ["a", 1, "b", 2, "c", 3, "d", 4]
result = []


# print(result)



# Solution
hash = { "a": 1, "b": 2, "c": 3, "d": 4 }
#      ["a", 1, "b", 2, "c", 3, "d", 4]
result = []

for key in hash:
    result.append(key)
    result.append(hash[key])

# print(result)



# 8. Combine data from a hash with names and prices and an array of hashes with names, colors, and weights to make a new hash.
#    For example, {"chair" => 75, "book" => 15} and [{name: "chair", color: "red", weight: 10}, {name: "book", color: "black", weight: 1}] becomes {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}.

price_hash = { "chair": 75, "book": 15 }
items = [{ "name": "chair", "color": "red", "weight": 10 }, { "name": "book", "color": "black", "weight": 1 }]
#        {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}
result = {}


# print(result)



# Solution
price_hash = { "chair": 75, "book": 15 }
items = [{ "name": "chair", "color": "red", "weight": 10 }, { "name": "book", "color": "black", "weight": 1 }]
#        {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}
result = {}

i = 0
while i < len(items):
    item = items[i]
    name = item["name"]
    color = item["color"]
    weight = item["weight"]
    price = price_hash[name]
    result[name] = {"price": price, "color": color, "weight": weight}
    i += 1

# print(result)



# 9. Convert an array of hashes into a hash of arrays, using the author as keys and the titles as values.
#    For example, [{author: "Jeff Smith", title: "Bone"}, {author: "George Orwell", title: "1984"}, {author: "Jeff Smith", title: "RASL"}] becomes {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}.

books = [{ "author": "Jeff Smith", "title": "Bone" }, { "author": "George Orwell", "title": "1984" }, { "author": "Jeff Smith", "title": "RASL" }]
#       {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}
result = {}



# print(result)



# Solution
# Goal: Turn an array of book hashes into a hash where authors are keys and titles are grouped in arrays
books = [{ "author": "Jeff Smith", "title": "Bone" }, { "author": "George Orwell", "title": "1984" }, { "author": "Jeff Smith", "title": "RASL" }]
#       {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}
result = {}                      # Empty dictionary to store authors and their title lists

i = 0                            # Start index at 0 to step through the books list
while i < len(books):            # Loop until we’ve checked every book (length = 3)
    book = books[i]              # Get the current book hash (e.g., {"author": "Jeff Smith", "title": "Bone"})
    author = book["author"]      # Extract the author’s name (e.g., "Jeff Smith")
    title = book["title"]        # Extract the book’s title (e.g., "Bone")
    if author not in result:     # If this author isn’t in the dictionary yet
        result[author] = []      # Create an empty list for their titles
    result[author].append(title) # Add the current title to the author’s list
    i += 1                       # Move to the next book in the list

# print(result)                    # Show the final hash with authors and their titles


# 10. Given a hash, create a new hash that has the keys and values switched.
#     For example, {"a" => 1, "b" => 2, "c" => 3} becomes {1 => "a", 2 => "b", 3 => "c"}.

hash = { "a": 1, "b": 2, "c": 3 }
#      {1 => "a", 2 => "b", 3 => "c"}
result = {}



# print(result)


# Solution
hash = { "a": 1, "b": 2, "c": 3 }
#               {1 => "a", 2 => "b", 3 => "c"}
result = {}

for key in hash:
    result[hash[key]] = key
# print(result)


# Solution
# hash = { "a": 1, "b": 2, "c": 3 }
# result = {}

# for key in hash:
#   value = hash[key]
#   result[value] = key
# print(result)


"""
# Quick Decision Rule: → Update this to be more simple to understand

Collection-Driven (Hash/List Keys) → for loop: “Iterate over items/keys directly.”
        Pattern: for item in collection or for key in hash.
        
        Key Insight: Use for when the problem says “for each [item/key] in [collection], do something” (e.g., “for each key, add it to the result”).


Position-Driven (List Indices) → while loop: “Iterate using an index.”
        Pattern: while i < len(sequence) with sequence[i].

        Key Insight: Use while when the problem involves “stepping through a list” or “processing items at specific positions” (e.g., “for each position i, use the item at i”)."
"""

