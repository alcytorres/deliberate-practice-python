# Write nested loops with methods


# 1. Use a nested loop to convert an array of number pairs into a single flattened array.
#    For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].

num_pairs = [[1, 3], [8, 9], [2, 16]]
#              [1, 3, 8, 9, 2, 16]
result = []

i1 = 0


# print(result)


# Solution
num_pairs = [[1, 3], [8, 9], [2, 16]]
#              [1, 3, 8, 9, 2, 16]
result = []
i1 = 0
while i1 < len(num_pairs):
    pair = num_pairs[i1]
    i2 = 0
    while i2 < len(pair):
        result.append(pair[i2])
        i2 += 1
    i1 += 1

# print(result)


# 2. Use a nested loop with two arrays of strings to create a new array of strings with each string combined.
#    For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].

letters1 = ["a", "b", "c"]
letters2 = ["d", "e", "f", "g"]
#          ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]
result = []

i1 = 0


# print(result)



# Solution
letters1 = ["a", "b", "c"]
letters2 = ["d", "e", "f", "g"]
#          ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]
result = []

i1 = 0
while i1 < len(letters1):
    i2 = 0
    while i2 < len(letters2):
        result.append(letters1[i1] + letters2[i2])
        i2 += 1
    i1 += 1

# print(result)



# 3. Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
#    For example, ["a", "b", "c", "d"] becomes ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].

letters = ["a", "b", "c", "d"]
#         ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]
result = []

i1 = 0


# print(result)



# Solution
letters = ["a", "b", "c", "d"]
#         ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]
result = []

i1 = 0
while i1 < len(letters):
    i2 = 0
    while i2 < len(letters):
        if i1 != i2:
            result.append(letters[i1] + letters[i2])
        i2 += 1
    i1 += 1

# print(result)



# 4. Use a nested loop to find the largest product of any two different numbers within a given array.
#    For example, [5, -2, 1, -9, -7, 2, 6] becomes 63.

nums = [5, -2, 1, -9, -7, 2, 6]
#         63
max_product = nums[0] * nums[1]

i1 = 0


# print(max_product)



# Solution
nums = [5, -2, 1, -9, -7, 2, 6]
#         63
max_product = nums[0] * nums[1]

i1 = 0
while i1 < len(nums):
    i2 = 0
    while i2 < len(nums):
        if i1 != i2:
            current_product = nums[i1] * nums[i2]
            if current_product > max_product:
                max_product = current_product
        i2 += 1
    i1 +=1

# print(max_product)


# 5. Use a nested loop to compute the sum of all the numbers in an array of number pairs.
#    For example, [[1, 3], [8, 9], [2, 16]] becomes 39.

nums = [[1, 3], [8, 9], [2, 16]]
#         39
total = 0

i1 = 0

    
# print(total)



# Solution
nums = [[1, 3], [8, 9], [2, 16]]
#         39
total = 0

i1 = 0
while i1 < len(nums):
    pair = nums[i1]
    i2 = 0
    while i2 < len(pair):
        num = pair[i2]
        total += num
        i2 += 1
    i1 += 1
    
# print(total)


# 6. Use a nested loop with two arrays of numbers to create a new array of the sums of each combination of numbers.
#    For example, [1, 2] and [6, 7, 8] becomes [7, 8, 9, 8, 9, 10].

nums1 = [1, 2]
nums2 = [6, 7, 8]
#          [7, 8, 9, 8, 9, 10]
result = []

i1 = 0


# print(result)



# Solution
nums1 = [1, 2]
nums2 = [6, 7, 8]
#          [7, 8, 9, 8, 9, 10]
result = []

i1 = 0
while i1 < len(nums1):
    i2 = 0
    while i2 < len(nums2):
        result.append(nums1[i1] + nums2[i2])
        i2 += 1
    i1 += 1

# print(result)



# 7. Use a nested loop with an array of numbers to compute an array with every combination of products from each number.
#    For example, [2, 8, 3] becomes [4, 16, 6, 16, 64, 24, 6, 24, 9].

nums = [2, 8, 3]
#         [4, 16, 6, 16, 64, 24, 6, 24, 9]
result = []

i1 = 0


# print(result)



# Solution
nums = [2, 8, 3]
#         [4, 16, 6, 16, 64, 24, 6, 24, 9]
result = []

i1 = 0
while i1 < len(nums):
    i2 = 0
    while i2 < len(nums):
        result.append(nums[i1] * nums[i2])
        i2 += 1
    i1 += 1

# print(result)


# 8. Use a nested loop to find the largest sum of any two different numbers within an array.
#    For example, [1, 8, 3, 10] becomes 18.

nums = [1, 8, 3, 10]
#         18
max_sum = nums[0] + nums[1]

i1 = 0


# print(max_sum)



# Solution
nums = [1, 8, 3, 10]
#         18
max_sum = nums[0] + nums[1]

i1 = 0
while i1 < len(nums):
    i2 = 0
    while i2 < len(nums):
        if i1 != i2:
            current_sum = nums[i1] + nums[i2]
            if current_sum > max_sum:
                max_sum = current_sum
        i2 += 1
    i1 += 1

# print(max_sum)


# DO THIS PROBLEM

# 9. Use nested loops with an array of numbers to compute a new array containing the first two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.
#    For example, [2, 5, 3, 1, 0, 7, 11] becomes [3, 7].

nums = [2, 5, 3, 1, 0, 7, 11]
#         [3, 7]
result = False

i1 = 0


# print(result)  



# Solution
nums = [2, 5, 3, 1, 0, 7, 11] 
#         [3, 7]                
result = False                  # Start with False; update to [num1, num2] if pair found

i1 = 0                          # Index for the first number, starts at 0
while i1 < len(nums):           # Loop through each possible first number
    i2 = 0                      # Index for the second number, resets to 0 for each i1
    while i2 < len(nums):       # Loop through each possible second number
        if i1 != i2 and nums[i1] + nums[i2] == 10:  # Check if indices differ and sum is 10
            result = [nums[i1], nums[i2]]           # Store the pair in result
            break                                   # Exit inner loop once pair is found
        i2 += 1                  # Move to the next second number
    if result:                   # If a pair was found (result is no longer False, result is truthy)
        break                    # Exit outer loop to stop searching
    i1 += 1                      # Move to the next first number

# print(result)                    # Print the result: [3, 7] or False if no pair exists


# 10. Use a nested loop to convert an array of string arrays into a single string.
#     For example, [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]] becomes "amanaplanacanalpanama".

strings = [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]]
#         "amanaplanacanalpanama"
result = ""

i1 = 0


# print(result)


# Solution
strings = [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]]
#         "amanaplanacanalpanama"
result = ""

i1 = 0
while i1 < len(strings):
    pair = strings[i1]
    i2 = 0
    while i2 < len(pair):
        result += pair[i2]
        i2 += 1
    i1 += 1

# print(result)

